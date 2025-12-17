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

# *args and **kwargs

def cal_total(*args):
    total = 0
    for num in args:
        total += num
    return total

print(cal_total(1,2,3,4))

def print_details(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="Mohit", age=25, city="New York")