#three redaction modes will be here: mask using *, hash and full redaction

import hashlib

def mask(value):
    return value[:3] + "*" * (len(value) - 3)

def hash_value(value):
    hashed = hashlib.sha256(value.encode()).hexdigest()
    return f"[HASH:{hashed}]"

def redact(value):
    return "[REDACTED]"

def apply_redact(value,mode):
    if mode == "mask":
        return mask(value)
    elif mode == "hash":
        return hash_value(value)
    elif mode == "redact":
        return redact(value)
    else:
        print(f"[ERROR]: '{mode}' is not recognised, defaulting to hash.")
        return hash_value(value)