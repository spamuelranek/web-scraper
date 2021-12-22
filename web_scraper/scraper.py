import requests
from bs4 import BeautifulSoup

## located inside li tag
url = "https://en.wikipedia.org/wiki/List_of_demons_in_the_Ars_Goetia"

## located inside p tag
url_two = "https://en.wikipedia.org/wiki/Demon"
page = requests.get(url_two)

soup = BeautifulSoup(page.content, "html.parser")
body = soup.find(id="bodyContent")

# # counter for the amount of citation needed
# body_two = soup.find_all(title="Wikipedia:Citation needed")
# print(len(body_two))
# # print(body_two)

# for citation in body_two:
#   parent = citation.find_parent("p")
#   print(f"{parent.text}\n")

def get_citations(url):
  page = requests.get(url)

  soup = BeautifulSoup(page.content, "html.parser")
  body = soup.find(id="bodyContent")

  body_two = soup.find_all(title="Wikipedia:Citation needed")
  return body_two

def get_citations_needed_count(url):
  body_two = get_citations(url)
  return len(body_two)

def get_citations_needed_report(url):
  body_two = get_citations(url)
  return_string = ''
  for citation in body_two:
    parent = citation.find_parent("p")
    return_string += f"{parent.text}\n"

  return return_string

cite_count  = get_citations_needed_count(url_two)
cite_report = get_citations_needed_report(url_two)
print(cite_count)
print(cite_report)