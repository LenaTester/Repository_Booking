from appium import webdriver
import pytest
from pythonProject.Repository_Booking.page_object.home_page import HomePage

@pytest.fixture()
def create_driver():
    desired_cap = {
        "platformName": "Android",
        "platformVersion": "10.0",
        "deviceName": "Redmi Note 8 Pro",
        "automationName": "UiAutomator2",
        "app": "D:\\Booking.com_ Hotels and more_34.7.1.1_Apkpure.apk"
    }

    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_cap)
    return driver

@pytest.fixture()
def get_home_page(create_driver):
    return HomePage(create_driver)
