from core.block import Block
import time
import json

from core.serialization.block_json_encoder import BlockJSONEncoder

class Blockchain:
    def __init__(self) -> None:
        self.chain = []
        self.waiting_transactions = []
        self.difficulty = 2

        self.create_genesis_block()

    def create_genesis_block(self) -> None:
        genesis_block = Block([], time.time(), "", 0)
        genesis_block.hash = genesis_block.compute_hash()
        self.chain.append(genesis_block)

    def __str__(self) -> str:
        return json.dumps(self.__dict__, sort_keys=True, cls=BlockJSONEncoder)

    @property
    def last_block(self) -> Block:
        return self.chain[-1]

    # TODO: guess we'll just start with a POW model, maybe split this in the future
    def proof_of_work(self, block: Block) -> str:
        computed_hash = block.compute_hash()
        while not computed_hash.startswith('0', self.difficulty):
            block.nonce += 1
            computed_hash = block.compute_hash()
        return computed_hash
    
    def try_add_block(self, block: Block, proof: str) -> bool:
        previous_hash = self.last_block.hash
        if previous_hash != block.previous_hash:
            return False
        if not self.is_valid_proof(block, proof):
            return False
        self.chain.append(block)
        return True
    
    def is_valid_proof(self, block: Block, block_hash: str) -> bool:
        return (block_hash.startswith('0' * self.difficulty) and 
            block_hash == block.compute_hash()) 

    def add_new_transaction(self, transaction: Block):
        self.waiting_transactions.append(transaction)

    def mine(self) -> str:
        if not self.unconfirmed_transactions:
            return False
        
        last_block = self.last_block
        new_block = Block([], time.time(), last_block.hash)

        proof = self.proof_of_work(new_block)
        self.add_block(new_block, proof)
        self.waiting_transactions.pop(0)
        return new_block.hash