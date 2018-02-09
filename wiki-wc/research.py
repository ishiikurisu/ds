import urllib.request
from bs4 import BeautifulSoup
import document
import calculator

class Researcher:
    def __init__(self, limit):
        """Starts the main variables that will be used in this process"""
        self.limit = limit
        self.debug = False
        self.pages = []
        self.visited = set()

    # MAIN ENTRY POINT
    def study_from(self, start_point):
        """Starts the main study loop from a starting wikipedia page"""
        self.docs = []
        self.register = document.Document('')
        self.how_many = 1
        self.study(start_point)
        processes = []

        # IDEA Make this loop run on parallel
        # downloading and extracting information
        while len(self.pages) > 0:
            page = self.pages[0]
            del self.pages[0]
            self.study(page)

        # generating final files
        self.analyze()

    def study(self, page):
        """Study a page by parsing its HTML, adding the next pages to be followed
        and analyzing the current page text."""
        html = urllib.request.urlopen(page).read()
        soup = BeautifulSoup(html, 'html.parser')
        div = soup.find('div', {'id': 'mw-content-text'})
        self.visited.add(page)

        links = div.find_all('a')
        for link in links:
            try:
                next_page = self.get_link(link)
                if next_page is not None:
                    self.try_to_add(next_page)
            except UnicodeEncodeError:
                pass

        all_p = div.find_all('p')
        content = ''
        for p in all_p:
            text = self.get_text(p)
            content += '\n' + text
        self.include(content)

    def try_to_add(self, page):
        """Tries to add another page to the study process."""
        if (self.how_many < self.limit) and (page not in self.visited):
            self.pages.append(page)
            self.how_many += 1
            self.visited.add(page)

    def get_link(self, a):
        """Gets a link from a Beautiful Soup anchor element."""
        outlet = None
        try:
            href = a['href']
            if href.startswith('/wiki'):
                outlet = 'https://wikipedia.org%s' % href
        except KeyError:
            pass
        return outlet

    def get_text(self, p):
        """Gets the text from a beautiful soup paragraph element."""
        return ' '.join(text.strip() for text in p.find_all(text=True, recursive=True))

    def include(self, text):
        """Studies the content of the text as proposed in this study."""
        doc = document.Document(text)
        self.docs.append(doc)
        self.register.include(doc)

    def analyze(self):
        """Analyzes all the documents after the download is completed."""
        terms, td_matrix = calculator.build_term_frequency_matrix(self.docs)
        if self.debug:
            print('--- # Analysis')
            print('how many: %d' % (self.how_many))
            print('terms: >')
            print(terms)
            print('td_matrix: >')
            print(td_matrix)
        # TODO Build TF.IDF matrix
        # TODO Calculate D*D matrix
        # TODO Export D*D matrix to CSV
