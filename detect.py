import re

#patterns that are used to detect email and password
email_regex = r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b"
password_regex = r"(?i)\b(password|pwd|passwd|secret|passphrase|pass)\b\s*[:=]\s*(\".*?\"|\S+)"

def detection_sensitive(data):
    matches = []

    for match in re.finditer(email_regex, data): 
        matches.append(("email", match.group())) 

    for match in re.finditer(password_regex, data):
        matches.append(("password", match.group(2)))

    #the code above looks for a match (using the pattern rules) , then adds it to the end of matches variable and returns it.
    return matches
