import pytest
import sys
sys.path.append('../')
from fixtures.CS_app import CScheckout



@pytest.fixture()
def app():
    app = CScheckout()
    yield app
    app.close()

@pytest.fixture()
def init_login(app):
    app.login("vitalii+test@nxte.nl", "vitalii+test@nxte.nl")
    # yield
    # app.logout() #logout not implemented func
    # Fashion giftcart quan testing
