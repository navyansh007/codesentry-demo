def average_age(users: list) -> float:
    """Return the mean age across all users."""
    total = 0
    for user in users:
        total += user["age"]
    return total / len(users)


def oldest_user(users: list) -> dict:
    """Return the user with the highest age."""
    oldest = users[0]
    for user in users:
        if user["age"] > oldest["age"]:
            oldest = user
    return oldest
