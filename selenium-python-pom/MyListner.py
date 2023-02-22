from selenium.webdriver.support.events import AbstractEventListener


class MyListner(AbstractEventListener):
    def before_navigate_to(self, url: str, driver):
        print("Before navigation executed")

    def after_navigate_to(self, url: str, driver) -> None:
        print("After navigation executed")

    def before_find(self, by, value, driver) -> None:
        print(f"Before find element {value}")

    def after_find(self, by, value, driver) -> None:
        print(f"After find element {value}")

    def before_click(self, element, driver) -> None:
        print(f"Before click on element {element}")

    def after_click(self, element, driver) -> None:
        print(f"After click element {element}")
