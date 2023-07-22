import base64
from itertools import cycle

message = """enter encrypted message here"""

key = bytes("enter your username", "utf8")

print(bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key))))