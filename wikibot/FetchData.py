import requests
from bs4 import BeautifulSoup as bs
import spacy 

def extractValidLinksFromWikiPage(page_title):
    all_links = []
    raw_html = fetch_wiki_HTML(page_title)
    #before extraction verify that target page is NOT a disambiguation page
    if not FetchData.checkIfDisambiguation(raw_html) and not isList(page_title): #not a DISAMBIGUATION page and Not a list
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
    elif FetchData.checkIfDisambiguation(raw_html): #choose best answer
        potential_matches = fetchDisambiguationLinks(raw_html)
        all_links.append(findNearestWord())
    elif isList(page_title): #return first link in list

    else:
        pass

    return all_links[0]


def randomWikipediaPages(page_name=None,allowDisambiguation=True):
    params = {
        'action':'query',
        'list':'random',
        'rnlimit':10,
        'format':'json',
        'prop':'pageprop',
        'ppprop':'disambiguation'
    }

    articles = []
    response = s.get('https://en.wikipedia.org/w/api.php', params=params, timeout=10)
    if response.status_code == 200:
        data = response.json()
        print(data)
        assert(data), 'error processing json file'
        pageCandidates = data['query']['random']
        for candidate in pageCandidates:
            if 'pageprops' in candidate.keys():
                pass
            else:
                articles.append(candidate['title'])
    return articles

def fetchSingleSectionWikipedia(page_name,rawHtml,section=1,htype=only_alpha):
        params = {
        'format':'json',
        'action':'parse',
        'page':page_name,
        'section':section
    }

    html = ""
    assert (page_name), 'you must include a valid wikipedia page name'
    s = requests.session()
    response = s.get('https://en.wikipedia.org/w/api.php', params=params, timeout=10)
    if response.status_code == 200:
        data = response.json()
        try:
            html = data["parse"]["text"]["*"]
            assert type(html) == str
        except KeyError as ke:
            print(ke)
            html = str(data)
    if htype == only_alpha:
        soup = bs(html, 'html.parser') 
        return " ".join([re.sub("[^A-Za-z\s]", "", a.text) for a in soup.find_all("p")])
    else:
        return html

def fetchWikipediaHTML(page_name=None):
    params = {
        'format':'json',
        'action':'parse',
        'page':page_name
    }

    html = ""
    assert (page_name), 'you must include a valid wikipedia page name'
    s = requests.session()
    response = s.get('https://en.wikipedia.org/w/api.php', params=params, timeout=10)
    if response.status_code == 200:
        data = response.json()
        try:
            html = data["parse"]["text"]["*"]
            assert type(html) == str
        except KeyError as ke:
            print(ke)
            html = str(data)
    return html

def checkIfDisambiguation(title='Germany'):
    params = {
    'format':'json',
    'action':'query', #parse
    'prop':'pageprops',
    'ppprop':'disambiguation',
    'titles':title
    }

    s = requests.session()
    response = s.get('https://en.wikipedia.org/w/api.php', params=params)

    if response.status_code == 200:
        #check if disambiguation
        result = response.json()
        pages = result['query']['pages']
        for k,v in pages.items():
            for k, v in v.items():
                if k == 'pageprops':
                    if 'disambiguation' in v:
                        return 'disambiguation_page'
   
def isList(url):
    if url.startswith('List_of_') or url.startswith('Lists_of_'):
        return 'list_page'

def findNearestWord(target, data):
    #data[url] = {'title':title,'page_content':page}
    matches = []
    best_score = ['term', 0.0]
    nlp = spacy.load('en')
    target = nlp(sentence)
    for url, info in data.items():
        title = info[1]
        string = info[2]
        stringToScore = nlp(string) 
        score = sen.similarity(target)
        data[url]['score'] = score
    return data

def topicCrumbtrail(topic,depth=20):
    collected = [topic]
    while len(collected) < depth:
        try:
            target = collected[-1]
            next_link = extract_links(target)
            collected.append(next_link)
            print(next_link, f"PREVIOUS:{target}")
        except Exception as ee:
            print(ee)
    return collected

def markupToString(raw_html):
    soup = bs(raw_html, 'html.parser')
    string = " ".join([re.sub("[^A-Za-z\s]", "", a.text) for a in soup.find_all("p")])
    return string

def grabDLinks(html):
    linksoup = bs(html, 'html.parser')
    list_div = linksoup.find("div" ,{"class":"mw-parser-output"})
    return [(a['href'],a.title) for a in list_div.find_all("ul") if '/wiki/' in a['href']]

def chooseNearestLink(target_html, disambiguation_html): #target_page is the page before the disambiguation page
    #convert target_html into alpha string
    target_ready = markupToString(target_html)
    #extract disambiguation links from disambiguation_html
    links_ready = grabDLinks(disambiguation_html)
    #for each extracted link convert text into alpha string
    best = ['','', 0.0]
    data = {}
    for link in links:
        url = link[0].replace('/wiki/',"")
        title = link[1]
        page_content = fetchSingleSectionWikipedia(url)
        if url and title and page_content:
            data[url] = {'title':title,'page_content':page}
    return findNearestWord(target_ready, data)

if __name__ == "__main__":
    pass
