from selene import Browser, by
from .google_results_page import GoogleResultsPage

class GoogleSearchPage:
    """
    This class represents the Google search page.
    """
    def __init__(self, b: Browser):
        self.browser = b
        self.query = self.browser.element(by.name('q'))

    def search(self, text: str) -> GoogleResultsPage:
        self.query.type(text)
        self.query.press_enter()
        return GoogleResultsPage(self.browser)