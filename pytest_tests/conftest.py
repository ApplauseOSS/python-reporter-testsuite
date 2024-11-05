from .applause_config import applause_config, proxy_url
from applause.pytest_applause_reporter import ApplausePytestPlugin
from .plugins import ApplauseProxyDriverPlugin
import pytest

# This configures the applause pytest plugin and registers it with pytest
def pytest_configure(config: pytest.Config):
    config.pluginmanager.register(ApplausePytestPlugin(applause_config), 'applause-pytest-plugin')
    config.pluginmanager.register(ApplauseProxyDriverPlugin(applause_config, selenium_proxy_url=proxy_url), 'applause-proxy-driver-plugin')