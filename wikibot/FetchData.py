import requests
from bs4 import BeautifulSoup as bs
import spacy 

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

def findNearestWord(sentence, list_of_strings):
    matches = []
    nlp = spacy.load('en')
    target = nlp(sentence)
    for sent in list_of_strings:
        sen = nlp(sent[0])
        result = [sen.similarity(target), sent[1]]
        print(result)
        matches.append(result)
    sorted(matches, key=lambda x: x[0],reverse=True)
    return matches[0]

if __name__ == "__main__":
    pass
