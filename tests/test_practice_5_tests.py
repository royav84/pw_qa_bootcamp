from pages import home_page


# def test_open_browser(page):
#     page.goto("https://playwright.dev")
#     pageTitle = page.title().lower()
#     assert "playwright" in pageTitle

# def test_correct_url(page):
#     gotoUrl = "https://playwright.dev"
#     page.goto(gotoUrl)
#     pageUrl = page.url
#     assert "playwright.dev" in pageUrl

# def test_click_get_started(home_page):
#     get_started_btn = home_page.page.get_by_role("link", name= "Get started")
#     get_started_btn.click()
    # assert "docs/intro" in home_page.page.url

# def test_checking_js_code_dropdown(home_page):
#     get_started_btn = home_page.page.get_by_role("link", name= "Get started")
#     get_started_btn.click()
#     node_js_dropdown = home_page.page.get_by_role("button", name="Node.js")
#     assert not home_page.page.get_by_role("banner").get_by_role("link", name="Python").is_visible()
#     node_js_dropdown.hover()
#     assert home_page.page.get_by_role("banner").get_by_role("link", name="Python").is_visible()

def test_checking_search_box_is_visible_and_function(home_page):
    home_page.open_search()

    search_box = home_page.page.get_by_role("searchbox", name="Search")
    search_box.click()
    search_box.fill("locator")
    search_box.press("Enter")

    assert home_page.page.get_by_text("locator").first.is_visible()