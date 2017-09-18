import pytest
from fixture import Application
from fixture import DBFixture
from fixture import ORMFixture
import json
import os.path
import importlib
import jsonpickle

webfixture = None
target = None


def load_config(file):
    global target
    if target is None:
        with open(file) as targetfile:
            target = json.load(targetfile)
    return target


@pytest.fixture
def app(request):
    global webfixture
    browser = request.config.getoption("--browser")
    web_config = load_config(request.config.getoption("--target"))["web"]

    if webfixture is None or not webfixture.is_valid():
        webfixture = Application(browser=browser, base_url=web_config["baseUrl"])

    webfixture.session.ensure_login(
        username=web_config["username"],
        password=web_config["password"]
    )
    return webfixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    global webfixture

    def fin():
        if webfixture:
            webfixture.session.ensure_logout()
            webfixture.destroy()
    request.addfinalizer(fin)
    return webfixture


@pytest.fixture(scope="session")
def db_pure(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    dbfixture = DBFixture(
        host=db_config["host"],
        database=db_config["database"],
        user=db_config["user"],
        password=db_config["password"]
    )

    def fin():
        dbfixture.destroy()
    request.addfinalizer(fin)

    return dbfixture


@pytest.fixture(scope="session")
def db(request):
    db_config = load_config(request.config.getoption("--target"))["db"]
    ormfixture = ORMFixture(
        host=db_config["host"],
        database=db_config["database"],
        user=db_config["user"],
        password=db_config["password"]
    )

    return ormfixture


@pytest.fixture
def check_ui(request):
    return request.config.getoption("--check_ui")


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="firefox")
    parser.addoption(
        "--target",
        action="store",
        default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "target.json")
    )
    parser.addoption("--check_ui", action="store_true")


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
