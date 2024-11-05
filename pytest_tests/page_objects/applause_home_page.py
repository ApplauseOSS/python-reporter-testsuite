from selene import Browser, by

class ApplauseHomePage:
    """
    This class represents the Applause home page.
    """
    def __init__(self, b: Browser):
        self.browser = b
        self.why_applause = self.browser.element(by.css("li.why_applause"))
        self.our_solutions = self.browser.element(by.css("li.our_solutions"))
        self.get_demo_button = self.browser.element(by.css("li.get-demo-button"))
        self.resources = self.browser.element(by.css("li.resources"))
        self.get_started_button = self.browser.element(by.css("li.get-started-button"))