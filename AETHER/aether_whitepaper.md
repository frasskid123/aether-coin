# Aether – A Peer-to-Peer Electronic Cash System (2026 Edition)

**Abstract**  
A purely peer-to-peer version of electronic cash would allow online payments to be sent directly from one party to another without going through a financial institution. Digital signatures provide part of the solution, but the main benefits are lost if a trusted third party is still required to prevent double-spending.

We propose a solution using a peer-to-peer network and proof-of-work to record a public history of transactions that quickly becomes computationally impractical for an attacker to change. The system is secure as long as honest nodes control the majority of computational power.

## 1. Introduction

Commerce on the Internet has come to rely almost exclusively on financial institutions serving as trusted third parties. This system suffers from high costs, reversals, and the need for trust. Aether solves this by providing a purely peer-to-peer electronic cash system based on cryptographic proof.

## 2. Transactions

An electronic coin is defined as a chain of digital signatures. Each owner transfers the coin by signing a hash of the previous transaction and the public key of the next owner.

## 3. Timestamp Server & Proof-of-Work

Transactions are timestamped by hashing them into a chain of proof-of-work blocks. The longest chain represents the accepted history and the largest pool of computational power.

## 4. Network & Incentive

The network runs on simple broadcast rules. Nodes mine blocks and are rewarded with new AETHER. The total supply is strictly capped at 21 million coins.

## 5. Tokenomics

| Era          | Block Reward | Blocks per Era | Total AETHER Mined in Era | Approximate Years |
|--------------|--------------|----------------|---------------------------|-------------------|
| 1 (Genesis)  | 50 AETHER    | 210,000        | 10,500,000                | 4 years           |
| 2            | 25 AETHER    | 210,000        | 5,250,000                 | 4 years           |
| 3            | 12.5 AETHER  | 210,000        | 2,625,000                 | 4 years           |
| ...          | ...          | ...            | ...                       | ...               |
| Final        | 0 AETHER     | -              | 21,000,000                | ~2140             |

- **Total Supply**: Exactly 21,000,000 AETHER (never more)  
- **Halving**: Every 210,000 blocks (~4 years)  
- **Inflation**: Ends completely after the final halving

## 6. Smart Contracts (2026 Feature)

Aether includes basic smart contract support for simple programmable logic:

- **Escrow contracts**: Lock AETHER until conditions are met (time-lock or manual release)
- **Time-locked payments**: Automatically release funds after a set date
- **Simple voting / DAOs**: Basic on-chain decision making

All contracts are stored directly on the blockchain and executed automatically.

## 7. Privacy

Public keys are anonymous by default. New keys are used for each transaction. Optional zero-knowledge proofs can be added for stronger privacy.

## 8. Reclaiming Disk Space & Simplified Payment Verification

Old transactions can be pruned using Merkle Trees. Light clients can verify payments without downloading the full chain.

## 9. Calculations & Security

The probability of an attacker catching up drops exponentially as more blocks are added. The system remains secure as long as honest nodes control the majority of computational power.

## 10. Roadmap (2026–2027)

- Q2 2026: Launch + basic node
- Q3 2026: Smart contract support
- Q4 2026: Mobile wallet prototype
- 2027: Layer-2 scaling and exchange listings

## 11. Conclusion

Aether is a true peer-to-peer electronic cash system — simple, secure, and built for the universe. The longest chain wins. Nodes vote with computational power. No trusted third parties.

**Genesis Block** mined March 28, 2026  
“The Times 03/28/2026 Aether launches peer-to-peer electronic cash for the universe.”

**Total Supply**: 21,000,000 AETHER (immutable)