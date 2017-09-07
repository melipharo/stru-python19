import pytest
from fixture import Application
import json
import os.path
import importlib
import jsonpickle

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


def pytest_generate_tests(metafunc):
    for fixture in metafunc.fixturenames:
        if fixture.startswith("data_"):
            test_data = load_from_module(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])
        elif fixture.startswith("json_"):
            test_data = load_from_json(fixture[5:])
            metafunc.parametrize(fixture, test_data, ids=[str(x) for x in test_data])


def load_from_module(name):
    return importlib.import_module("data.{}".format(name)).test_data


def load_from_json(name):
    datafile = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data/{}.json".format(name))
    with open(datafile, "r") as f:
        return jsonpickle.decode(f.read())
