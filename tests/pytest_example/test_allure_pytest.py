import allure

@allure.step('step 1')
def step_1():
    pass

@allure.step('step 2')
def step_2():
    pass

@allure.step('step 3')
def step_3():
    pass

def test_feature():
    # step_1()
    with allure.step('step 1'):
        pass

    # step_2()
    with allure.step('step 2'):
        pass

    # step_3()
    with allure.step('step 3'):
        pass