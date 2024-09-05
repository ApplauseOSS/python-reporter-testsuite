import pytest
from applause.pytest_applause_reporter import ApplausePytestPlugin, ApplauseConfig


def pytest_configure(config: pytest.Config):
    app_config = ApplauseConfig(
        api_key="api_key", 
        product_id=123)
    config.pluginmanager.register(ApplausePytestPlugin(app_config), "applause-pytest-plugin")
