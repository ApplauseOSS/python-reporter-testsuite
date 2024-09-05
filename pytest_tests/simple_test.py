from applause.pytest_applause_reporter import ApplauseResult, EmailHelper
from selene import Browser
import pytest

@pytest.mark.applause_test_case_id("371940")
@pytest.mark.test_rail_test_case_id(149007)
def test_simple_case(applause_result: ApplauseResult, driver: Browser, email_helper: EmailHelper):
    applause_result.log("This is a test log")
    assert 1 == 1, "my failure"
