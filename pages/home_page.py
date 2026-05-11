print("home_page loaded")

class HomePage:
    def __init__(self, page):
        self.page = page

    def open(self, path: str = "/"):
        self.page.goto(path)

    def title(self) -> str:
        return self.page.title()
    
    def open_search(self):
        self.page.get_by_role("button", name="Search (Ctrl+K)").click()

    def search(self, text):
        search_box = self.page.get_by_role("searchbox", name="Search")
        search_box.fill(text)
        search_box.press("Enter")