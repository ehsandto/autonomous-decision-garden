import json


QUESTION = "How should a small team provide offline access to its public documentation?"
BOUNDARIES = "The output is a set of possible strategies, not a claim about cost or success."
LOCAL = "Ship a downloadable static archive of the documentation for users to store on a device."
CACHE = "Make the website a progressive web app that caches pages in a browser service worker."
LOCAL_REWORD = "Provide a downloadable static copy of the documentation for local device storage."
PRINT = "Create a printable document bundle that can be read without an internet connection."


def setup(direct_vm, direct_deploy, direct_alice, direct_bob, capacity=3):
    direct_vm.sender = direct_alice
    contract = direct_deploy("contracts/AutonomousDecisionGarden.py", "offline-docs", QUESTION, BOUNDARIES, capacity)
    contract.invite(direct_bob)
    direct_vm.sender = direct_bob
    contract.accept()
    direct_vm.sender = direct_alice
    return contract


def mock(direct_vm, *relations):
    direct_vm.mock_llm(r".*fictional decision-exploration space.*",
                       json.dumps({"relations": list(relations)}))


def submit_pair(direct_vm, contract, alice, bob, left_id, left, right_id, right, round_number):
    direct_vm.sender = alice
    contract.propose(left_id, left, round_number)
    direct_vm.sender = bob
    contract.propose(right_id, right, round_number)


def test_distinct_strategies_fill_frontier(direct_vm, direct_deploy, direct_alice, direct_bob):
    contract = setup(direct_vm, direct_deploy, direct_alice, direct_bob, 2)
    submit_pair(direct_vm, contract, direct_alice, direct_bob, "archive", LOCAL, "browser", CACHE, 0)
    mock(direct_vm, "DISTINCT")
    contract.resolve_round(0)
    state = contract.get_space()
    assert state["frontier"] == ["archive", "browser"]
    assert state["status"] == "FROZEN"
    assert contract.get_candidate("browser")["status"] == "ADMITTED"
    assert contract.get_round(0)["relations"] == ["DISTINCT"]


def test_semantic_duplicate_rejected(direct_vm, direct_deploy, direct_alice, direct_bob):
    contract = setup(direct_vm, direct_deploy, direct_alice, direct_bob)
    submit_pair(direct_vm, contract, direct_alice, direct_bob, "archive", LOCAL, "archive2", LOCAL_REWORD, 0)
    mock(direct_vm, "SAME")
    contract.resolve_round(0)
    assert contract.get_space()["frontier"] == ["archive"]
    assert contract.get_candidate("archive2")["status"] == "REDUNDANT"
    assert contract.get_space()["status"] == "EXPLORING"


def test_unknown_fails_closed_for_second_candidate(direct_vm, direct_deploy, direct_alice, direct_bob):
    contract = setup(direct_vm, direct_deploy, direct_alice, direct_bob)
    submit_pair(direct_vm, contract, direct_alice, direct_bob, "archive", LOCAL, "browser", CACHE, 0)
    mock(direct_vm, "UNKNOWN")
    contract.resolve_round(0)
    assert contract.get_space()["frontier"] == ["archive"]
    assert contract.get_candidate("browser")["status"] == "UNCERTAIN"


def test_later_round_uses_prior_frontier(direct_vm, direct_deploy, direct_alice, direct_bob):
    contract = setup(direct_vm, direct_deploy, direct_alice, direct_bob)
    submit_pair(direct_vm, contract, direct_alice, direct_bob, "archive", LOCAL, "archive2", LOCAL_REWORD, 0)
    mock(direct_vm, "SAME")
    contract.resolve_round(0)
    direct_vm.clear_mocks()
    submit_pair(direct_vm, contract, direct_alice, direct_bob, "browser", CACHE, "print", PRINT, 1)
    mock(direct_vm, "DISTINCT", "DISTINCT", "DISTINCT")
    contract.resolve_round(1)
    assert contract.get_space()["frontier"] == ["archive", "browser", "print"]
    assert contract.get_space()["status"] == "FROZEN"
    assert len(contract.get_round(1)["pairs"]) == 3


def test_unauthorized_duplicate_and_stale_rejected(direct_vm, direct_deploy, direct_alice, direct_bob, direct_charlie):
    contract = setup(direct_vm, direct_deploy, direct_alice, direct_bob)
    direct_vm.sender = direct_charlie
    with direct_vm.expect_revert("active member required"):
        contract.propose("unauthorized", LOCAL, 0)
    direct_vm.sender = direct_alice
    contract.propose("archive", LOCAL, 0)
    with direct_vm.expect_revert("one proposal per agent"):
        contract.propose("second", PRINT, 0)
    direct_vm.sender = direct_bob
    contract.propose("browser", CACHE, 0)
    mock(direct_vm, "DISTINCT")
    contract.resolve_round(0)
    with direct_vm.expect_revert("stale or exhausted round"):
        contract.propose("later", PRINT, 0)
    with direct_vm.expect_revert("new id and bounded plan"):
        contract.propose("archive", PRINT, 1)


def test_malformed_model_output_is_uncertain(direct_vm, direct_deploy, direct_alice, direct_bob):
    contract = setup(direct_vm, direct_deploy, direct_alice, direct_bob)
    submit_pair(direct_vm, contract, direct_alice, direct_bob, "archive", LOCAL, "browser", CACHE, 0)
    mock(direct_vm, "MAYBE")
    contract.resolve_round(0)
    assert contract.get_candidate("browser")["status"] == "UNCERTAIN"


def test_owner_freeze_is_terminal(direct_vm, direct_deploy, direct_alice, direct_bob):
    contract = setup(direct_vm, direct_deploy, direct_alice, direct_bob)
    contract.freeze()
    with direct_vm.expect_revert("active member required"):
        contract.propose("archive", LOCAL, 0)
    with direct_vm.expect_revert("active current round required"):
        contract.resolve_round(0)
