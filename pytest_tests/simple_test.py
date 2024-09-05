from applause.pytest_applause_reporter import ApplauseResult


def test_simple_case(applause_result: ApplauseResult):
    assert 1 == 1
