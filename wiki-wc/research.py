import urllib.request
from bs4 import BeautifulSoup

class Researcher:
    def __init__(self, qty):
        self.limit = qty
        self.debug = False
        self.pages = []
        self.how_many = 0

    def study_from(self, start_point):
        self.pages.append(start_point)
        self.how_many = 1
        while len(self.pages) > 0:
            page = self.pages[0]
            del self.pages[0]
            self.study(page)

    def study(self, page):
        html = urllib.request.urlopen(page).read()
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', {'id': 'mw-content-text'})

        links = div.find_all('a')
        for link in links:
            try:
                next_page = self.get_link(link)
                if self.is_valid(next_page):
                    self.work_with(next_page)
            except UnicodeEncodeError:
                pass

        # TODO Study current page

        if self.debug:
            print('---')
            print('page: %s' % (page))

    def work_with(self, page):
        if self.how_many < self.limit:
            self.pages.append(page)
            self.how_many += 1

    def is_valid(self, page):
        return page is not None

    def get_link(self, a):
        outlet = None
        try:
            href = a['href']
            if href.startswith('/wiki'):
                outlet = 'https://wikipedia.org%s' % href
        except Exception:
            pass
        return outlet
