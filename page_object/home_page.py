from appium.webdriver.common.appiumby import AppiumBy
from pythonProject.Repository_Booking.web_ui.base_page import BasePage

class HomePage(BasePage):
    __accept_button = (AppiumBy.ID, "com.booking:id/bt_accept")
    __enter_via_google = (AppiumBy.ID, "com.booking:id/auth_bui_button")
    __user_option = (AppiumBy.ID, "com.google.android.gms:id/account_display_name")
    __switch_on_button = (AppiumBy.ID, "com.booking:id/action_primary")
    __appartments = (AppiumBy.ID, "com.booking:id/facet_entry_point_item_label")

    def __init__(self, driver):
        super().__init__(driver)

    def click_accept(self):
        self.click(self.__accept_button)
        return self

    def click_enter_via_google(self):
        self.click(self.__enter_via_google)
        return self

    def click_user_option(self):
        self.click(self.__user_option)
        return self

    def click_switch_on(self):
        self.click(self.__switch_on_button)
        return self

    def get_appartments_text(self):
        notification = self.wait_for_element_located(self.__appartments)
        return self.get_text(notification)
