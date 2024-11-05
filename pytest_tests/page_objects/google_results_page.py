from selene import Browser, Element

class GoogleResultsPage:
    """
    This class represents the Google results page.
    """
    def __init__(self, b: Browser):
        self.browser = b
        self.results = self.browser.all('#rso>div')
        self.first_result_header = self.results.first.element('h3')

    def result(self, number: int) -> Element:
        return self.results[number - 1]

    def follow_link_of_result(self, number: int) -> None:
        self.result(number).element('h3').click()