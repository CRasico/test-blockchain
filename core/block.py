import json
from typing import Any, List
from hashlib import sha256
from uuid import uuid4
from core.serialization.complex_object_encoder import ComplexObjectEncoder

class Block:
    def __init__(
        self, 
        transactions: List[int], 
        timestamp: float,
        previous_hash: str,
        nonce: int,
    ) -> None:
        self.identifier = uuid4() 
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = None
        self.nonce = nonce

    def as_json(self):
        return self.__dict__

    def __str__(self) -> str:
        return json.dumps(self.__dict__, sort_keys=True, cls=ComplexObjectEncoder)
    
    def compute_hash(self) -> str:
        json_buffer = self.__str__().encode()
        return sha256(json_buffer).hexdigest()

