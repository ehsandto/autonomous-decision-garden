# AutonomousDecisionGarden

A GenLayer primitive for maintaining a small frontier of **semantically distinct candidate plans**. This is a decision-exploration tool, not a recommendation, outcome verifier, or certificate issuer.

## Problem

Multi-agent brainstorming often fills a shared list with rewordings of the same strategy. A deterministic graph can store branches and prevent cycles, but cannot determine whether two differently worded plans use the same primary mechanism. The contract admits alternatives only after GenLayer leader and validators independently derive the same pairwise semantic relation matrix.

## Protocol

1. A creator opens one decision space with a bounded question, boundaries and frontier capacity of 2–4.
2. The creator invites up to seven other wallets; each must explicitly accept.
3. Each member submits at most one 40–600-character plan per round. A round contains 2–3 plans.
4. Leader and validators compare every new plan against the current frontier and earlier plans in the round. They independently return `SAME`, `DISTINCT` or `UNKNOWN` for each exact pair. The validator reruns the complete task and requires exact equality of the context hash and full relation vector.
5. A deterministic frontier algorithm admits the first candidate, rejects semantic duplicates, fails closed on uncertain relationships, and stops at capacity. It records every disposition and an immutable round root.
6. The frontier freezes automatically at capacity or round 32; the creator can freeze it earlier.

```text
EXPLORING → invited agents accept → bounded candidate batch
          → independent pairwise semantic comparison
          → exact consensus vector → deterministic frontier update
          → immutable round root → EXPLORING or FROZEN
```

Unlike a knowledge graph, the contract does not maintain arbitrary nodes, edges, parent versions or claim content. Unlike WorldForge, it does not simulate agent actions. Its state is a versioned antichain-like set of non-redundant strategies, with round-local pairwise decisions. It never selects a winning plan or executes an option.

## Security and limitations

Plan text is the object being compared, **not evidence that a plan works**. The contract does not acquire real-world evidence or assert feasibility, cost, safety, or success. Unknown semantic relationships prevent admission. Candidate IDs, rounds, one-proposal-per-agent limits and wallet membership prevent replay and unauthorized submissions. An accepted first candidate has no semantic peer to compare against and is **not** an endorsement. See [threat model](docs/threat-model.md).

## API

`invite`, `accept`, `propose`, `resolve_round`, `freeze`, `get_space`, `get_candidate`, `get_round`.

## Test and deploy

The first contract line pins a concrete GenVM runner. In a Python environment with `genvm-linter` and `genlayer-test`:

```powershell
genvm-lint check contracts/AutonomousDecisionGarden.py
pytest tests/direct -q
genlayer network set studionet
genlayer deploy --contract contracts/AutonomousDecisionGarden.py --args offline-docs "How should a small team provide offline access to its public documentation?" "Explore possible mechanisms; do not claim feasibility or outcomes." 3
genlayer schema <CONTRACT_ADDRESS>
genlayer code <CONTRACT_ADDRESS>
```

Direct tests exercise the leader path and deterministic state machine, **not** validator consensus. Two finalized StudioNet rounds demonstrate live comparison: [contract](https://explorer-studio.genlayer.com/address/0x55BeEC78b334bCB0c55A033Edfd965a349826423), [proof matrix](PROOF_MATRIX.md), [full lifecycle](LIVE_PROOFS.md). The deployed source matches this repository's contract source exactly.
