import os
from hindsight_client import Hindsight

BANK_ID = "projectpulse-demo"

# Railway will use the Cloudflare tunnel URL.
# Locally, it falls back to Hindsight running on localhost:8888.
HINDSIGHT_URL = os.getenv(
    "HINDSIGHT_URL",
    "http://localhost:8888"
)


def get_client():
    return Hindsight(
        base_url=HINDSIGHT_URL,
        timeout=600
    )


def retain_memory(content):
    """Store a project event or decision in Hindsight."""
    client = get_client()

    try:
        client.retain(
            bank_id=BANK_ID,
            content=content
        )
        return True

    finally:
        try:
            client.close()
        except Exception:
            pass


def recall_memory(query):
    """Retrieve relevant project memories from Hindsight."""
    client = get_client()

    try:
        return client.recall(
            bank_id=BANK_ID,
            query=query
        )

    finally:
        try:
            client.close()
        except Exception:
            pass