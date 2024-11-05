import pytest
from _pytest.nodes import Node
from selenium.webdriver.chrome.options import Options
from selene import Browser, Config
from typing import Generator, Any
from applause.pytest_applause_reporter import AssetType, ApplauseResult, ApplauseConfig
from urllib.parse import urlparse, urlunparse


class ApplauseProxyDriverPlugin:

    def __init__(self, config: ApplauseConfig, selenium_proxy_url: str = "https://prod-auto-proxy-new.cloud.applause.com:443/wd/hub"):
        
        self.config = config
        parsed_url = urlparse(selenium_proxy_url)
        domain = parsed_url.netloc.split("@")[-1]
        domain = f"ApplauseKey:{self.config.api_key}@{domain}"
        self.selenium_proxy_url = urlunparse((parsed_url[0], domain, parsed_url[2], parsed_url[3], parsed_url[4], parsed_url[5]))
        print(f"Using Selenium Proxy URL: {self.selenium_proxy_url}")

    # This fixture sets up the selenium connection
    @pytest.fixture(scope="function")
    def driver(self, request: pytest.FixtureRequest) -> Generator[Browser, Any, None]: # type: ignore

        options = Options()
        options.set_capability("applause:options", {
            "driverName": "Chrome",
            "provider": "SauceLabs US West",
            "productId": self.config.product_id,
            "apiKey": self.config.api_key
        })
        session = Browser(
            config=Config(
                driver_remote_url=self.selenium_proxy_url,
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
                provider_session_guid=session.driver.session_id
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