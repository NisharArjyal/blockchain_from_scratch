import json       #syntax for storing and exchanging data(javascript object notation)
import random     #अनियमित सन्ख्या दिन्छ।

from datetime import datetime  #समयको लागि ।
from hashlib import sha256     #hash value निकाल्ने मोड्युल ् ।


class Blockchain(object):                    #ब्लकचेनको ब्लु पृन्ट ।
    def __init__(self):
        self.chain = []                       #
        self.pending_transactions = []

        # Create the genesis block
        print("Creating genesis block")
        self.chain.append(self.new_block())

    def new_block(self):
        block = {
            'index': len(self.chain),
            'timestamp': datetime.utcnow().isoformat(),
            'transactions': self.pending_transactions,
            'previous_hash': self.last_block["hash"] if self.last_block else None,
            'nonce': format(random.getrandbits(64), "x"),
        }

        # Get the hash of this new block, and add it to the block
        block_hash = self.hash(block)
        block["hash"] = block_hash

        # Reset the list of pending transactions
        self.pending_transactions = []

        return block

    @staticmethod
    def hash(block):
        # We ensure the dictionary is sorted or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return sha256(block_string).hexdigest()

    @property
    def last_block(self):
        # Returns the last block in the chain (if there are blocks)
        return self.chain[-1] if self.chain else None

    @staticmethod
    def valid_block(block):
        # Checks if a block's hash starts with 0000
        return block["hash"].startswith("0000")

    def proof_of_work(self):
        while True:
            new_block = self.new_block()
            if self.valid_block(new_block):
                break

        self.chain.append(new_block)
        print("Found a new block: ", new_block)
print("नेपाली")
