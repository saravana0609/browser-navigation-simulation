class WebPageNode:
    """Represents a single web page (Doubly Linked List Node)"""
    def __init__(self, url, title):
        self.url = url
        self.title = title
        self.prev = None  # Points to the previous page (Back button)
        self.next = None  # Points to the next page (Forward button)


class BrowserHistory:
    """Manages the browser session history and navigation pointers"""
    def __init__(self):
        self.head = None      # First page visited
        self.tail = None      # Latest page in history
        self.current = None   # Page currently being viewed
        self.total_pages = 0  # Total count of pages

    def visit_page(self, url, title):
        """Visits a new web page and appends it to the history"""
        new_page = WebPageNode(url, title)

        # If this is the very first page ever visited
        if self.head is None:
            self.head = new_page
            self.tail = new_page
            self.current = new_page
        else:
            # Link the new page to our current position
            new_page.prev = self.current
            self.current.next = new_page
            self.tail = new_page
            self.current = new_page  # Move current pointer to the new page

        self.total_pages += 1
        print(f"Visited: {title} ({url})")

    def go_back(self):
        """Goes back to the previous page using the prev pointer"""
        if self.current is None or self.current.prev is None:
            print("No previous page! You are at the start of your history.")
            return
        
        self.current = self.current.prev
        print(f"Went Back to: {self.current.title} ({self.current.url})")

    def go_forward(self):
        """Goes forward to the next page using the next pointer"""
        if self.current is None or self.current.next is None:
            print("No forward page! You are at the latest page.")
            return
        
        self.current = self.current.next
        print(f"Went Forward to: {self.current.title} ({self.current.url})")


# --- Testing the Browser Simulation ---
if __name__ == "__main__":
    my_browser = BrowserHistory()

    print("=== BROWSER NAVIGATION SIMULATION (PYTHON) ===\n")

    # 1. Visit web pages
    my_browser.visit_page("https://google.com", "Google Search")
    my_browser.visit_page("https://github.com", "GitHub Repository")
    my_browser.visit_page("https://stackoverflow.com", "Stack Overflow")

    print("\n--- Testing Navigation Controls ---")

    # 2. Test Going Back
    my_browser.go_back()  # Should move back to GitHub
    my_browser.go_back()  # Should move back to Google

    # 3. Test Going Forward
    my_browser.go_forward()  # Should move forward to GitHub

    # 4. Visit a new page while in the middle of history
    print("\n--- Visiting a new page from the middle ---")
    my_browser.visit_page("https://chatgpt.com", "ChatGPT AI")