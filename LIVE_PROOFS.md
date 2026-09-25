# StudioNet lifecycle proofs

Contract: [0x55BeEC78b334bCB0c55A033Edfd965a349826423](https://explorer-studio.genlayer.com/address/0x55BeEC78b334bCB0c55A033Edfd965a349826423)

All listed transactions were checked as `FINALIZED` with `MAJORITY_AGREE`; the leader execution for each succeeded. `genlayer code` matched `contracts/AutonomousDecisionGarden.py` exactly (9,056 non-trailing-whitespace characters).

| Step | Explorer | State or outcome |
| --- | --- | --- |
| Deploy | [0x452466…](https://explorer-studio.genlayer.com/tx/0x452466e03d022a2a25123455d97ac9289226a96a6ec0bd053238e6a809ec71df) | Contract code and schema readable |
| Invite second wallet | [0xef0ae8…](https://explorer-studio.genlayer.com/tx/0xef0ae87bfe7c5958c21a3bab39faa9f1ba3cddfffaac67605dcc9739a0104c22) | Owner invited `0xdf247b…1ec4a` |
| Explicit acceptance | [0x0f2e99…](https://explorer-studio.genlayer.com/tx/0x0f2e99197965a6ef9cfd9ddeb0c362be700283bd8eb2cb20b21e18585b1ebad3) | Invited wallet accepted |
| Browser-cache proposal | [0x65d657…](https://explorer-studio.genlayer.com/tx/0x65d657afd456476d58d3cd8dfa4cae727c441baafd2f8368ef1c2eab5d289c03) | Submitted by second wallet |
| Static-archive proposal | [0x1ae035…](https://explorer-studio.genlayer.com/tx/0x1ae035096cb44a1bc3b511a26c5da4d4e6d713ef92c03bca1c68b5308b96b4f3) | Submitted by owner wallet |
| Round 0 comparison | [0xdc1d44…](https://explorer-studio.genlayer.com/tx/0xdc1d44192e560d340664c41df664f85a977871200c1e4d6f3a62a92f91ec5dd6) | Pair `browser`/`archive` → `DISTINCT`; both `ADMITTED`; frontier `archive,browser`; root `a26f3726…bb26` |
| Kiosk proposal | [0xc56d8e…](https://explorer-studio.genlayer.com/tx/0xc56d8eb555ed3ac866d02c14eb59628a4438c3540e734243ef541748dc2bb72f) | Submitted by second wallet |
| Reworded archive | [0xeb80c8…](https://explorer-studio.genlayer.com/tx/0xeb80c8ce10d0e293105961c53fe9e0e7c74079e9399b1aa9ce94cea6140ef337) | Deliberate semantic duplicate submitted by owner |
| Round 1 comparison | [0x68ea9f…](https://explorer-studio.genlayer.com/tx/0x68ea9f2ebc5fac2b852b52567ff0ccbef0256a46478160652f29d0778c32d6c8) | Exact vector `SAME,DISTINCT,DISTINCT,DISTINCT,DISTINCT`; archive reword `REDUNDANT`, kiosk `ADMITTED`; frontier `archive,browser,kiosk`; state `FROZEN`; root `798c23e0…3d89` |

The live comparison proves GenLayer consensus over pairwise semantic relations and deterministic frontier admission. It does **not** prove that any plan will work in reality. Seven direct tests passed; direct mode does not execute validator comparison.
