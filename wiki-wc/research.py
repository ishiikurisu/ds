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
            
        if self.debug:
            print('...')

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

        all_p = div.find_all('p')
        content = ''
        for p in all_p:
            text = self.get_text(p)
            content += '\n' + text
        # TODO Analyze page content
        self.analyze(content)

        if self.debug:
            try:
                print('---')
                print('page: %s' % (page))
                print('content:')
                print(content)
            except UnicodeEncodeError:
                pass

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
        except KeyError:
            pass
        return outlet

    def get_text(self, p):
        text = ' '.join(text.strip() for text in p.find_all(text=True, recursive=True))
        return text

    def analyze(self, text):
        # IDEA Create an analyzer class that will count words per document and give an opinion.
        pass