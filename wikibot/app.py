import requests
# 1. Choose a random phrase from Wikipedia
# 2. Follow the first link in the description
# 3. remember the new phrase
# 4. Repeat the process

#return a single random wikipedia page
def fetch_wiki_HTML(page_name=None):
    assert (page_name), 'you must include a valid wikipedia page name'
    if page_name: #get page
        page_url = f'https://en.wikipedia.org/w/api.php?action=parse&page={page_name}'
        response = requests.get(page_url, timeout=10)
        if response.status_code == 200:
            return response.text
        else:
            raise Exception('failure to reach page')

#return a single random wikipedia page title
def fetch_random_page(page_name=None):
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
def extract_first_link(html): 
    pass       


def collect_data(random_words=100, depth_per_search=20):
    #{'Germany':['Central_Europe','Europe','Continent','Land#Land_mass',...]}
    #Key is the randomly visited page, list contains all the terms in order they were collected
    #stop collecting words when a loop is discovered
    words_collected = {} 


if __name__ == "__main__":
    pass