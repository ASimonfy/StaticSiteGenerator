import re

def extract_title(markdown):
    match = re.search(r"^# (.+)\n?", markdown, re.MULTILINE)
    if not match:
        raise ValueError("No h1 heading found in markdown")
    return match.group(1)