# Threat model

The system makes no real-world truth claim. Plans are untrusted creative artifacts. Its only semantic decision is whether two plans have the same primary mechanism for the registered question.

| Attack or failure | Boundary |
| --- | --- |
| Unauthorized wallet proposes | Only invited-and-accepted member wallets can submit |
| A member floods a round | One proposal per member; at most three proposals per round |
| Candidate or round replay | Globally unique candidate IDs and exact expected round |
| Same plan reworded | Independent pairwise semantic comparison against frontier and earlier candidates |
| Ambiguous comparison | `UNKNOWN` prevents admission; malformed model output normalizes to `UNKNOWN` |
| Leader fabricates relation vector | Validators rerun complete comparison and require exact equality |
| Prompt injection in plan text | Prompt treats candidate text as untrusted data; deterministic code also enforces all structural invariants. Prompt-injection risk is not eliminated. |
| Infinite growth | Frontier at most four, rounds at most 32, invitees at most seven, plans at most 600 characters |

The first candidate is admitted without a peer comparison and is not a quality signal. Exact validator agreement improves reproducibility but does not guarantee good semantic judgment. The frontier must not be used to authorize spending, execute a plan or assert external feasibility.
