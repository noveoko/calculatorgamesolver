import requests 
from bs4 import BeautifulSoup as bs
import time

def get_fresh_proxy():
    url = 'http://pubproxy.com/api/proxy'
    response = requests.get(url)
    if response.status_code == 200:
        result = response.json()
        return {'ip':result['data'][0]['ip'],
                'type':result['data'][0]['type']}

def get_solutions(stop=None):
    unique_links = set()
    with open('links_to_solutions.txt') as linkfile:
        links = [a.strip() for a in linkfile.readlines()]
        for count, link in enumerate(links[0:stop]):
            print(link
            # print(count, link, len(links)-count)
            # try:
            #     proxy = get_fresh_proxy()
            #     proxies = {
            #     str(proxy['type']): str(proxy['ip'])
            #     }
            #     response = requests.get(link, proxies=proxies)
            #     if response.status_code == 200:
            #         soup = bs(response.content, 'html.parser')
            #         test_info = ",".join([a.text.strip() for a in soup.find_all("center")if a])
            #         print(test_info)
            #         unique_links.add(test_info)
            #         time.sleep(3)
            # except Exception as ee:
            #     print(ee)
    return links


if __name__ == "__main__":
    get_solutions()