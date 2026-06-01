import re

email_regex = r"\b[A-Za-z0-9._%+_]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
password_regex = r"(?i)\b(password|pwd|passwd|secret|passphrase|pass)\b\s*[:=]\s*(\".*?\"|\S+)"

