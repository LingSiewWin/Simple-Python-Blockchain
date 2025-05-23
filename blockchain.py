import hashlib
import time
import json


class Block:
    def __init__(self, index, previous_hash, data, timestamp=None):
        self.index = index
        self.timestamp = timestamp or time.time()
        self.data = data
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        block_string = f"{self.index}{self.timestamp}{self.data}{self.previous_hash}"
        return hashlib.sha256(block_string.encode()).hexdigest()

    def to_dict(self):
        return {
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'hash': self.hash,
        }


class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block(0, "0", "Genesis Block")

    def get_latest_block(self):
        return self.chain[-1]

    def add_block(self, data):
        latest_block = self.get_latest_block()
        new_block = Block(
            index=latest_block.index + 1,
            previous_hash=latest_block.hash,
            data=data
        )
        self.chain.append(new_block)

    def is_chain_valid(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]

            if current.hash != current.calculate_hash():
                print("Invalid block hash at index", i)
                return False

            if current.previous_hash != previous.hash:
                print("Invalid previous hash at index", i)
                return False
        return True

    def display_chain(self):
        for block in self.chain:
            print(json.dumps(block.to_dict(), indent=4))


# Example usage:
if __name__ == "__main__":
    my_blockchain = Blockchain()
    my_blockchain.add_block("First real block")
    my_blockchain.add_block("Second real block")
    my_blockchain.add_block("Third real block")

    my_blockchain.display_chain()
    print("Is blockchain valid?", my_blockchain.is_chain_valid())
