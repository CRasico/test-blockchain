from json import JSONEncoder
from typing import Any
from uuid import UUID

class BlockJSONEncoder(JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, UUID):
            return str(obj)
        if isinstance(obj, Block):
            return str(obj)
        return JSONEncoder.default(self, obj)