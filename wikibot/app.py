import requests
from bs4 import BeautifulSoup as bs
import re, json

#return a single random wikipedia page
def fetch_wiki_HTML(page_name=None):
    html = ""
    assert (page_name), 'you must include a valid wikipedia page name'
    page_url = f'https://en.wikipedia.org/w/api.php?action=parse&page={page_name}&format=json'
    response = requests.get(page_url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        try:
            html = data["parse"]["text"]["*"]
            assert type(html) == str
        except KeyError as ke:
            html = str(data)
    return html

#return a single random wikipedia page title
def fetch_random_pages(page_name=None):
    page_url = 'https://en.wikipedia.org/w/api.php?action=query&list=random&rnlimit=10&format=json'
    response = requests.get(page_url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        assert(data), 'error processing json file'
        list_of_titles = [a['title'] for a in data['query']['random']]
        return list_of_titles

#extract the first sensible link
#ignore links related to the pronunciation of the term:`Germany (German: Deutschland German pronunciation: [ˈdɔʏtʃlant])`
#select the first word that links to a Wikipedia page that is not the page itself
def extract_links(page_title):
    all_links = []
    raw_html = fetch_wiki_HTML(page_title)
    soup = bs(raw_html, 'html.parser')
    paragraphs = [a for a in soup.findAll("p") if '<b>' in str(a)]
    for paragraph in paragraphs:
        just_text = re.sub(r"\(([\(].?)+\)", "", paragraph.text.lower())
        links = paragraph.findAll("a")
        for link in links:
            try:
                text = link.text
                url = link['href']
                if '/wiki/' in url and ':' not in url and '#cite-note' not in url and text.lower() in just_text:
                    short_url = url.replace('/wiki/',"")
                    #all_links.append([url, text])
                    all_links.append(short_url)
            except Exception as ee:
                print(ee)
    return all_links[0]

def fetch_all_links(topic,depth=20):
    collected = [topic]
    while len(collected) < depth:
        try:
            target = collected[-1]
            next_link = extract_links(target)
            collected.append(next_link)
            print(next_link)
        except Exception as ee:
            print(ee, "line 62")

if __name__ == "__main__":
    fetch_all_links('Germany',10)
