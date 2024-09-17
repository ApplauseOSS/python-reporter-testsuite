import pytest
from _pytest.nodes import Node
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from typing import Generator, Any
from applause.common_python_reporter.dtos import TestRailOptions
from applause.pytest_applause_reporter import ApplausePytestPlugin, ApplauseConfig, AssetType, ApplauseResult

api_key = "API_KEY" # update this with your api key
product_id = 123 # update this with your product id

auto_api_url = 'https://prod-auto-api.cloud.applause.com:443/'
proxy_url = f'https://ApplauseKey:{api_key}@prod-auto-proxy-new.cloud.applause.com:443/wd/hub'

applause_config = ApplauseConfig(
    api_key=api_key,
    product_id=product_id,
    auto_api_base_url=auto_api_url,
    test_rail_options=TestRailOptions(
        run_name='My Test Run',
        project_id=8,
        suite_id=453,
        plan_name='My Test Plan',
    )
)

# This fixture sets up the selenium connection
@pytest.fixture(scope="function")
def driver(request: pytest.FixtureRequest) -> Generator[Browser, Any, None]: # type: ignore

    options = Options()
    options.set_capability("applause:options", {
        "driverName": "Chrome",
        "provider": "SauceLabs US West",
        "productId": product_id,
        "apiKey": api_key
    })
    session = Browser(
        config=Config(
            driver_remote_url=proxy_url,
            driver_options=options
        )
    )
    session.open("https://www.google.com")

    yield session

    node: Node = request.node

    # If the Applause Pytest Plugin is configured, we can perform operations on the ApplauseResult
    if request._fixturemanager.getfixturedefs("applause_result", node):
        applause_result: ApplauseResult = request.getfixturevalue("applause_result")

        # Register the session ID with the ApplauseResult
        applause_result.register_session_id(session.driver.session_id)

        # If the test failed, attach the failure screenshot 
        if node.status is not None and node.status.failed:
            applause_result.log("Attaching failure screenshot")
            applause_result.attach_asset(
                asset_name="failure_screenshot.png",
                asset=session.driver.get_screenshot_as_png(),
                asset_type=AssetType.FAILURE_SCREENSHOT,
                provider_session_guid=session.driver.session_id
            )
        
        # Attach the page source and logs
        applause_result.log("Attaching page source and logs")
        applause_result.attach_asset(
            asset_name="page_source.html",
            asset=bytes(session.driver.page_source, encoding='utf-8'),
            asset_type=AssetType.PAGE_SOURCE,
            provider_session_guid=driver.driver.session_id
        )
        for log_type in session.driver.log_types:
            applause_result.attach_asset(
                asset_name=log_type + ".log",
                asset=bytes(str(session.driver.get_log(log_type)), encoding='utf-8'),
                asset_type=AssetType.UNKNOWN,
                provider_session_guid=session.driver.session_id
            )

    # Finally, quit the driver
    session.driver.quit()

# This configures the applause pytest plugin and registers it with pytest
def pytest_configure(config: pytest.Config):
    config.pluginmanager.register(ApplausePytestPlugin(applause_config), 'applause-pytest-plugin')