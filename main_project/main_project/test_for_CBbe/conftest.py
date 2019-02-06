import pytest
import sys
sys.path.append('../')
from fixtures.CBbe_app import Checkout



@pytest.fixture()
def app():
    app = Checkout()
    yield app
    app.close()
