import re, json
from bs4 import BeautifulSoup as bs

with open('test_files/example.json') as f:
    all_links = []
    data = json.load(f)
    html = data['parse']['text']['*']
    soup = bs(html, 'html.parser')
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
                    all_links.append(url, text)
            except Exception as ee:
                print(ee)
    return all_links