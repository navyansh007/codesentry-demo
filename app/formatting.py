def display_name(first: str, last: str) -> str:
    """Return a user's display name, e.g. 'Ada Lovelace'."""
    return f"{first.strip()} {last.strip()}".strip()


def initials(first: str, last: str) -> str:
    """Return upper-case initials, e.g. 'AL'."""
    parts = [p for p in (first.strip(), last.strip()) if p]
    return "".join(p[0].upper() for p in parts)
