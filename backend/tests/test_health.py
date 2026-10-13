import pytest


# ATOMIC_REQUESTS wraps every request in a transaction, so even a view that
# touches no models needs database access.
@pytest.mark.django_db
def test_health_returns_ok(client):
    response = client.get("/api/health/")

    assert response.status_code == 200
    assert response.json() == {"status": "ok"}
