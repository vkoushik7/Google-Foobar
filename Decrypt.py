import base64
from itertools import cycle

message = """DUwBHBALCxIYSFVJSE4MRRMKBk5fSEkCBAMZFgkOHlJRS0hJVA0dFQ4KGBYMTkcXUQ4UDxwaGhJM T09TTwAFVAQOFgARBAtGR09SEgsBAlIADh8MHRxJQVFPUgYGBQRUHQ4WTl9ISRMKDRcaHBpMF0xL VRoSDgtGR09SFQcGTBdMS1UeGgZPRhY="""

key = bytes("vkrishnakoushik7", "utf8")

print(bytes(a ^ b for a, b in zip(base64.b64decode(message), cycle(key))))