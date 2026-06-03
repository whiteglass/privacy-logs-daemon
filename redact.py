#three redaction modes will be here: mask using *, hash and full redaction

import hashlib

def mask(value):
    return value[:3] + "*" * (len(value) - 3)

def hash_value(value):
    hashed = hashlib.sha256(value.encode()).hexdigest()
    return f"[HASH:{hashed}]"

def redact(value):
    return "[REDACTED]"