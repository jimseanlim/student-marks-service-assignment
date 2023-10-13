import uuid
import pytest
from fastapi.testclient import TestClient
from starlette import status

from ..main import app
client = TestClient(app)

@pytest.mark.anyio
def test_echo():
    """
    Tests that echo route works.

    :param fastapi_app: current application.
    :param client: client for the app.
    """
    url = app.url_path_for("send_echo_message")
    message = uuid.uuid4().hex
    response = client.post(
        url,
        json={
            "message": message,
        },
    )
    assert response.status_code == status.HTTP_200_OK
    assert response.json()["message"] == message
