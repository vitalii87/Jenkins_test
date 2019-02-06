import pytest
from test_for_CB.CB_app import Checkout


@pytest.fixture()
def app():
    app = Checkout()
    yield app
    app.close()
