from json import JSONEncoder
from typing import Any
from core.block import Block

class BlockchainJSONEncoder(JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, Block):
            return str(obj)
        return JSONEncoder.default(self, obj)