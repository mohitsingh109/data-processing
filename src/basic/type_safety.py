from typing import Dict
from typing import List
from typing import Any

def add(a: int, b: int) -> int:
    return a + b

def some_dummy() -> dict:
    return {"key": "value"}


def some_dummy1() -> Dict[str, Any]:
    return {"key": "value", "key1": 123, "key2": [1, 2, 3]}

print(add(1, 3))
#print(add("Mohit", "Singh"))