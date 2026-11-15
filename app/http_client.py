import requests


def fetch_profile(url: str) -> dict:
    """Download a remote user profile as JSON."""
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    return response.json()
