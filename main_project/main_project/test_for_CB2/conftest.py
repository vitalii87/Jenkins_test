import pytest
# sys.path.append('../')
from main_project.test_for_CB2.CB2 import Checkout


# def pytest_addoption(parser):
#     parser.addoption("--base-url-key", action="store") #, default="http://localhost/")


@pytest.fixture() #scope='session'
def app(request):
    # base_url_key = request.config.getoption("--base-url")
    dict_url = {
        "dev": "http://localhost/en"
    }
    app2 = Checkout(base_url=dict_url['dev'])
    yield app2
    app2.close()



