from json import JSONEncoder
from typing import Any
from uuid import UUID

class ComplexObjectEncoder(JSONEncoder):
    def default(self, obj: Any) -> Any:
        if isinstance(obj, UUID): return str(obj)
        if hasattr(obj, "as_json"): return obj.as_json()

        return super().default(obj)