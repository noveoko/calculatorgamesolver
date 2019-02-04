import requests 
from bs4 import BeautifulSoup as bs
import time
import re

def get_fresh_proxy():
    url = 'http://pubproxy.com/api/proxy'
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        return {'ip':result['data'][0]['ip'],
                'type':result['data'][0]['type']}

def extract_solution(html):
    soup = bs(html, 'html.parser')
    solution = soup.select("center > strong")[0].find_next().text
    return solution

def get_solutions(start=None,stop=None):
    solutions = {}
    with open('links_to_solutions.txt') as linkfile:
        links = [a.strip() for a in linkfile.readlines()]
        for count, link in enumerate(links[start:stop]):
            skey = re.search(r"\-(\d+)\-", link).group(1)
            try:
                proxy = get_fresh_proxy()
                proxies = {
                str(proxy['type']): str(proxy['ip'])
                }
                response = requests.get(link, proxies=proxies)
                if response.status_code == 200:
                    solution = extract_solution(response.content)
                    solutions[skey] = solution
                    text = f"{skey}\t{solution}\n"
                    with open('solutions.txt','a') as writesol:
                            writesol.write(text)
                            print(text)
                else:
                    print(response.status_code)
            except Exception as ee:
                print(ee)
    return solutions

if __name__ == "__main__":
    parse_all_solutions('solutions.txt')
