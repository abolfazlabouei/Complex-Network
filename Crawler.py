import logging
from urllib.parse import urljoin
import requests
from bs4 import BeautifulSoup

logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

class Crawler:

    def __init__(self, urls=[]):
        self.visited_urls = []
        self.urls_to_visit = urls
        self.base_url = "https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=complex+network+&btnG=&oq=comp"
        self.index = 0

    def download_url(self, url):
        return requests.get(url).text

    def get_linked_urls(self, url, html):
        soup = BeautifulSoup(html, 'html.parser')
        # body = soup.select_one('html')
        for link in soup.select('a'):
            path = link.get('href')
            if path and path.startswith('/'):
                path = urljoin(url, path)
            yield path

    def add_url_to_visit(self, url):
        
        if url not in self.visited_urls and url not in self.urls_to_visit:
            self.urls_to_visit.append(url)
        
        

    def crawl(self, url):
        html = self.download_url(url)
        f = open("googleschoolar2.txt",'a')


        for url1 in self.get_linked_urls(self.base_url, html):
            if url1 and not url1.startswith('#'):
                self.add_url_to_visit(url1 )
                f.write(str(self.index)) 
                f.write(' ')
                f.write(str(self.urls_to_visit.index(url1)))
                f.write('\n')
        f.close()      


    def run(self):
        while self.urls_to_visit:
            url = self.urls_to_visit[self.index]
            logging.info(f'Crawling: {url}')
            try:
                self.crawl(url)
            except Exception:
                logging.exception(f'Failed to crawl: {url}')
            finally:
                self.visited_urls.append(url)
                self.index += 1

if __name__ == '__main__':
    crawler = Crawler(urls=['https://scholar.google.com/scholar?hl=en&as_sdt=0%2C5&q=complex+network+&btnG=&oq=comp']).run()
    