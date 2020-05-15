import requests
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
import string

def soupcreator(xml_news_url):

    req = Request(xml_news_url, headers={'User-Agent': 'Mozilla/5.0'})
    parse_xml_url = urlopen(req)
    xml_page = parse_xml_url.read()
    parse_xml_url.close()

    soup_page = BeautifulSoup(xml_page, "xml")
    return soup_page

def dictionary(link):
    soup = soupcreator(link)

    words = []
    for word in soup.find_all("a", {'rel': 'bookmark'}):
        words.append(word.text)

    definitions = []
    for definition in soup.find_all("div", {'class': 'entry-content'}):
        definitions.append(definition.text)

    return dict(zip(words, definitions))

finaldictionary = {}
for letter in list(string.ascii_lowercase):
    finaldictionary.update(dictionary('https://politicaldictionary.com/words/category/' + letter))