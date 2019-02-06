import pytest
import sys
sys.path.append('../')
from fixtures.CKB_app import Checkout


@pytest.fixture()
def app():
    app = Checkout()
    yield app
    app.close()
