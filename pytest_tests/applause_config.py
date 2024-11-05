from applause.common_python_reporter import ApplauseConfig, TestRailOptions

api_key = "API_KEY" # update this with your api key
product_id = 0 # update this with your product id

auto_api_url = 'https://prod-auto-api.cloud.applause.com:443/'
proxy_url = f'https://prod-auto-proxy-new.cloud.applause.com:443/wd/hub'

applause_config = ApplauseConfig(
    api_key=api_key,
    product_id=product_id,
    auto_api_base_url=auto_api_url,
    test_rail_options=TestRailOptions(
        run_name='My Test Run',
        project_id=0,
        suite_id=0,
        plan_name='My Test Plan',
    )
)