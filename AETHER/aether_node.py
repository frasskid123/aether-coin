import hashlib
import time
import json
import os

WALLET_FILE = "aether_wallet.json"

class AetherBlock:
    def __init__(self, index, prev_hash, transactions, timestamp=None, nonce=0):
        self.index = index
        self.prev_hash = prev_hash
        self.transactions = transactions
        self.timestamp = timestamp or time.time()
        self.nonce = nonce
        self.hash = self.mine_block()

    def mine_block(self, target_zeros=6):
        target = "0" * target_zeros
        nonce = 0
        while True:
            header = str(self.index) + self.prev_hash + self.transactions + str(self.timestamp) + str(nonce)
            block_hash = hashlib.sha256(header.encode()).hexdigest()
            if block_hash.startswith(target):
                self.nonce = nonce
                return block_hash
            nonce += 1

class AetherChain:
    def __init__(self):
        self.chain = []
        self.pending_transactions = []
        self.load_chain()

    def create_genesis(self):
        genesis_tx = "The Times 03/28/2026 Aether launches peer-to-peer electronic cash for the universe."
        return AetherBlock(0, "0", genesis_tx)

    def load_chain(self):
        if os.path.exists("aether_chain.json"):
            with open("aether_chain.json", "r") as f:
                data = json.load(f)
                self.chain = [AetherBlock(b["index"], b["prev_hash"], b["transactions"], b["timestamp"], b["nonce"]) for b in data]
            print(f"Loaded existing chain with {len(self.chain)} blocks!")
        else:
            self.chain = [self.create_genesis()]
            print("Created new genesis block!")

    def save_chain(self):
        data = [{"index": b.index, "prev_hash": b.prev_hash, "transactions": b.transactions, 
                 "timestamp": b.timestamp, "nonce": b.nonce, "hash": b.hash} for b in self.chain]
        with open("aether_chain.json", "w") as f:
            json.dump(data, f)
        print("Chain saved to aether_chain.json")

    def add_block(self):
        last_block = self.chain[-1]
        new_block = AetherBlock(len(self.chain), last_block.hash, json.dumps(self.pending_transactions))
        self.chain.append(new_block)
        self.pending_transactions = []
        self.save_chain()
        print(f"✅ Block #{new_block.index} mined! Hash: {new_block.hash[:16]}...")
        return new_block

    def mine(self):
        if self.pending_transactions:
            return self.add_block()
        print("No pending transactions to mine.")
        return None

class Wallet:
    def __init__(self):
        if os.path.exists(WALLET_FILE):
            with open(WALLET_FILE, "r") as f:
                data = json.load(f)
                self.private_key = data["private_key"]
                self.address = data["address"]
            print("Loaded existing wallet!")
        else:
            self.private_key = hashlib.sha256(str(time.time()).encode()).hexdigest()[:64]
            self.address = hashlib.sha256(self.private_key.encode()).hexdigest()[:40]
            with open(WALLET_FILE, "w") as f:
                json.dump({"private_key": self.private_key, "address": self.address}, f)
            print("Created and saved new wallet!")

        print("🪪 Your AETHER Wallet:")
        print("Address:", self.address)
        print("(Keep your private key safe!)")

if __name__ == "__main__":
    print("🚀 AETHER Node Starting...\n")
    chain = AetherChain()
    wallet = Wallet()
    print("\nMining your next personal block...\n")
    chain.pending_transactions.append("Reward to " + wallet.address + ": 50 AETHER")
    chain.mine()
    print("\n✅ Success! Your chain is saved permanently.")
    input("\nPress ENTER to close this window...")