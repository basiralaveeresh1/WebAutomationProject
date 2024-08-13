from selenium import webdriver
import pytest
import allure

class Test_Pytest_Mark:
    @allure.title("TC#1 Verify the Method1")
    @allure.description("Verifying the Method1 description")
    @allure.label("Owner","Veeresh")
    @pytest.mark.smoke
    def test_Method1(self):
        print("Method1")
        assert 1 == 1

    @allure.title("TC#2 Verify the Method1")
    @allure.description("Verifying the Method2 description")
    @allure.label("Owner", "Veeresh")
    @pytest.mark.regression
    def test_Method2(self):
        print("Method2")
        assert 2 == 2

    @allure.title("TC#3 Verify the Method3")
    @allure.description("Verifying the Method3 description")
    @allure.label("Owner", "Veeresh")
    @pytest.mark.skip
    def test_Method3(self):
        print("Method3")
        assert 3==3

    @allure.title("TC#4 Verify the Method4")
    @allure.description("Verifying the Method4 description")
    @allure.label("Owner", "Veeresh")
    @pytest.mark.skip
    def test_Method4(self):
        print("Method4")
        assert 4 == 4

    @allure.title("TC#5 Verify the Method5")
    @allure.description("Verifying the Method5 description")
    @allure.label("Owner", "Veeresh")
    @pytest.mark.skip
    def test_Method5(self):
        print("Method5")
        assert 5 == 5

