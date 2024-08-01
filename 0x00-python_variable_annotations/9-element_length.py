#!/usr/bin/env python3

element_length = __import__('9-element_length').element_length

print(element_length.__annotations__)
lst = ["hello", [1, 2, 3], ("a", "b", "c")]
print(element_length(lst))

