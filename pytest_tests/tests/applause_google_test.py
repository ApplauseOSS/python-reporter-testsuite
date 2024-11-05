from applause.pytest_applause_reporter import ApplauseResult
from selene import Browser, by
from pytest_tests.page_objects import GoogleSearchPage, ApplauseHomePage
import pytest


class TestApplauseGoogleSearch:

    def navigate_to_applause_home_page(self, applause_result: ApplauseResult, driver: Browser) -> ApplauseHomePage:
        search_page = GoogleSearchPage(driver)
        applause_result.log("Searching for Applause on Google")
        results_page = search_page.search("Applause")
        results_page.results.wait_until(lambda c: c.size > 0)
        for i in range(10):
            if results_page.result(i).element(by.css("cite")).locate().text == "https://www.applause.com":
                applause_result.log("Found Applause Search Result - Clicking on it")
                results_page.follow_link_of_result(i)
                break
        if driver.driver.current_url != "https://www.applause.com/":
            assert False, "Could not find the correct link"
        return ApplauseHomePage(driver)


    @pytest.mark.applause_test_case_id("TEST_CASE_ID")
    @pytest.mark.test_rail_test_case_id("TEST_CASE_ID")
    def test_why_applause_button(self, applause_result: ApplauseResult, driver: Browser):
        applause_home_page = self.navigate_to_applause_home_page(applause_result, driver)

        applause_result.log("Checking the 'Why Applause' Button")
        applause_home_page.why_applause.should(lambda e: e.locate().is_displayed())
        assert applause_home_page.why_applause.locate().is_displayed(), "'Why Applause' Button is not displayed"
        assert applause_home_page.why_applause.locate().is_enabled(), "'Why Applause' Button is not enabled"
        applause_home_page.why_applause.click()

    @pytest.mark.applause_test_case_id("TEST_CASE_ID")
    @pytest.mark.test_rail_test_case_id("TEST_CASE_ID")
    def test_our_solutions_button(self, applause_result: ApplauseResult, driver: Browser):
        applause_home_page = self.navigate_to_applause_home_page(applause_result, driver)

        applause_result.log("Checking the 'Our Solutions' Button")
        applause_home_page.our_solutions.should(lambda e: e.locate().is_displayed())
        assert applause_home_page.our_solutions.locate().is_displayed(), "'Our Solutions' Button is not displayed"
        assert applause_home_page.our_solutions.locate().is_enabled(), "'Our Solutions' Button is not enabled"
        applause_home_page.our_solutions.click()

    @pytest.mark.applause_test_case_id("TEST_CASE_ID")
    @pytest.mark.test_rail_test_case_id("TEST_CASE_ID")
    def test_resources_button(self, applause_result: ApplauseResult, driver: Browser):
        applause_home_page = self.navigate_to_applause_home_page(applause_result, driver)

        applause_result.log("Checking the 'Resources' Button")
        applause_home_page.resources.should(lambda e: e.locate().is_displayed())
        assert applause_home_page.resources.locate().is_displayed(), "'Resources' Button is not displayed"
        assert applause_home_page.resources.locate().is_enabled(), "'Resources' Button is not enabled"
        applause_home_page.resources.click()

    @pytest.mark.applause_test_case_id("TEST_CASE_ID")
    @pytest.mark.test_rail_test_case_id("TEST_CASE_ID")
    def test_get_demo_button(self, applause_result: ApplauseResult, driver: Browser):
        applause_home_page = self.navigate_to_applause_home_page(applause_result, driver)

        applause_result.log("Checking the 'Get Demo' Button")
        applause_home_page.get_demo_button.should(lambda e: e.locate().is_displayed())
        assert applause_home_page.get_demo_button.locate().is_displayed(), "'Get Demo' Button is not displayed"
        assert applause_home_page.get_demo_button.locate().is_enabled(), "'Get Demo' Button is not enabled"
        applause_home_page.get_demo_button.click()

    @pytest.mark.applause_test_case_id("TEST_CASE_ID")
    @pytest.mark.test_rail_test_case_id("TEST_CASE_ID")
    def test_get_started_button(self, applause_result: ApplauseResult, driver: Browser):
        applause_home_page = self.navigate_to_applause_home_page(applause_result, driver)

        applause_result.log("Checking the 'Get Started' Button")
        applause_home_page.get_started_button.should(lambda e: e.locate().is_displayed())
        assert applause_home_page.get_started_button.locate().is_displayed(), "'Get Started' Button is not displayed"
        assert applause_home_page.get_started_button.locate().is_enabled(), "'Get Started' Button is not enabled"
        applause_home_page.get_started_button.click()
    