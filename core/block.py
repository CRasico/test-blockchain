from typing import Any, List
from hashlib import sha256
from uuid import uuid4
from core.serialization.block_json_encoder import BlockJSONEncoder
import json

class Block:
    def __init__(
        self, 
        transactions: List[int], 
        timestamp: float,
        previous_hash: str,
        nonce: int,
        identifier: Any = uuid4()
    ) -> None:
        self.identifier = identifier
        self.transactions = transactions
        self.timestamp = timestamp
        self.previous_hash = previous_hash
        self.hash = None
        self.nonce = nonce

    def __str__(self) -> str:
        return json.dumps(self.__dict__, sort_keys=True, cls=BlockJSONEncoder)
    
    def compute_hash(self) -> str:
        json_buffer = self.__str__().encode()
        return sha256(json_buffer).hexdigest()

