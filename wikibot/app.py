import requests
from bs4 import BeautifulSoup as bs
import re, json

#return a single random wikipedia page
def fetch_wiki_HTML(page_name=None):
    assert (page_name), 'you must include a valid wikipedia page name'
    page_url = f'https://en.wikipedia.org/w/api.php?action=parse&page={page_name}&format=json'
    response = requests.get(page_url, timeout=10)
    if response.status_code == 200:
        data = response.json()
        html = data['parse']['text']['*']
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
        print(len(paragraph))
        just_text = re.sub(r"\(([\(].?)+\)", "", paragraph.text.lower())
        print(just_text)
        links = paragraph.findAll("a")
        for link in links:
            try:
                text = link.text        
                url = link['href']
                if '/wiki/' in url and ':' not in url and '#cite-note' not in url and text.lower() in just_text:
                    all_links.append([url, text])
            except Exception as ee:
                print(ee)
    return all_links

def collect_data(random_words=100, depth_per_search=20):
    #{'Germany':['Central_Europe','Europe','Continent','Land#Land_mass',...]}
    #Key is the randomly visited page, list contains all the terms in order they were collected
    #stop collecting words when a loop is discovered
    words_collected = {}
    while len(words_collected.keys()) < random_words:
        wiki_page_titles = fetch_random_pages()
        for title in wiki_page_titles:
            words_collected[title] = [] #create a new entry with empty list to hold results
            new_wiki_link = extract_links(title)
            if len(words_collected[title]) < depth_per_search: #check if words collected == depth_per_search
                words_collected[title].append(new_wiki_link)
            else:
                pass
    return words_collected

if __name__ == "__main__":
    result = collect_data(5, 3)
    print(result)