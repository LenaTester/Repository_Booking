def test_launching_app(get_home_page):
    """user is redirected to booking page"""
    launch = get_home_page.click_accept().click_enter_via_google().click_user_option(). \
        click_switch_on().get_appartments_text()
    assert launch == "Жилье", \
        f'\nUser is not redirected to booking page\nActual: {launch}' \
        f'\nExpected: Жилье'