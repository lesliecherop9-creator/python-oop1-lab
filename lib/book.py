class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.current_page=1


def turn_pages(self):
    if self.current_page<self.pages:
        self.current_page += 1
        print(f"Turned to page {self.current_page}.")
    else:
        print("You are already at the last page of the book.")



        