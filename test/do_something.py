import allure

def test_do_something(orm):
    with allure.step("Given the nothing, do the something"):
        orm.do_something()
