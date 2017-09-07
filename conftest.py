import pytest
from fixture import Application
import json
import os.path

fixture = None
target = None

@pytest.fixture
def app(request):
    global fixture
    global target
    browser = request.config.getoption("--browser")
    if target is None:
        with open(request.config.getoption("--target")) as targetfile:
            target = json.load(targetfile)

    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser, base_url=target["baseUrl"])

    fixture.session.ensure_login(
        username=target["username"],
        password=target["password"]
    )
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    global fixture
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption(
        "--target",
        action="store",
        default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "target.json")
    )
