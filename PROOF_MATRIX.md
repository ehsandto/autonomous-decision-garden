# Proof matrix

| Claim | Local result | StudioNet result |
| --- | --- | --- |
| Pinned runner and SDK syntax | `genvm-lint check` passed | [Finalized deployment](https://explorer-studio.genlayer.com/tx/0x452466e03d022a2a25123455d97ac9289226a96a6ec0bd053238e6a809ec71df) |
| Distinct strategies enter frontier | Direct test passed | [Finalized round 0](https://explorer-studio.genlayer.com/tx/0xdc1d44192e560d340664c41df664f85a977871200c1e4d6f3a62a92f91ec5dd6): `DISTINCT`, two admitted |
| Equivalent plan rejected | Direct test passed | [Finalized round 1](https://explorer-studio.genlayer.com/tx/0x68ea9f2ebc5fac2b852b52567ff0ccbef0256a46478160652f29d0778c32d6c8): reworded archive `REDUNDANT` |
| Unknown relationship fails closed | Direct test passed | Not yet exercised live |
| Invitation, acceptance, replay and freeze | Direct tests passed | [Invite](https://explorer-studio.genlayer.com/tx/0xef0ae87bfe7c5958c21a3bab39faa9f1ba3cddfffaac67605dcc9739a0104c22), [accept](https://explorer-studio.genlayer.com/tx/0x0f2e99197965a6ef9cfd9ddeb0c362be700283bd8eb2cb20b21e18585b1ebad3), final state `FROZEN`; replay not yet exercised live |
| Exact validator relation-vector recomputation | Not exercised in direct mode | Both finalized rounds reached `MAJORITY_AGREE` |

See [live proofs](LIVE_PROOFS.md). Deployed source matches the local contract file exactly. Do not treat these transactions or caller-provided plan text as evidence of real-world plan quality.
