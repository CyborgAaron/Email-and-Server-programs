#!/usr/bi/pyhton3
import urllib.request
import lxml.etree
from lxml.cssselect import CSSSelector
url = 'https://www.yahoo.com/news/weather/united-kingdom/england/london-44418'
response = urllib.request.urlopen(url)
html = response.read()
parser = lxml.etree.HTMLParser(encoding='utf-8')
doctree = lxml.etree.fromstring(html, parser)
span = CSSSelector("span.num")
temp = span(doctree)[1].text
print('The current temperature in London is:', temp)
