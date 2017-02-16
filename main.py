import requests
import timeit
import numpy as np

from lxml import html
from pprint import pprint

start = timeit.default_timer()

all_page1  = requests.get("http://www.uio.no/studier/emner/matnat/ifi/")
all_tree1 = html.fromstring(all_page1.content)

all_page2 = requests.get("http://www.uio.no/studier/emner/matnat/ifi/?page=2&u-page=2")
all_tree2 = html.fromstring(all_page2.content)

all_courses1 = all_tree1.xpath('//tbody/tr/td/a/@href')
all_courses2 = all_tree2.xpath('//tbody/tr/td/a/@href')

all_courses = all_courses1 + all_courses2

url_stem = "http://www.uio.no"

courses = {}

for url_ending in all_courses:
    complete_url = url_stem + url_ending

    page = requests.get(complete_url)
    tree = html.fromstring(page.content)

    title = "".join(tree.xpath('//h1/text()')).strip("\t\n")
    about = "".join(tree.xpath('//div[@id="course-content"]/*/text()')).strip("\t\n")
    outcome = "".join(tree.xpath(
        '//div[@id="learning-outcomes"]/*/text()|//div[@id="learning-outcomes"]/ul/*/text()')).strip("\t\n")

    courses[title] = {"about": about, "outcome": outcome}

end = timeit.default_timer()

np.save('courses.npy', courses)
print("File saved!")
print("\nCompleted in", end-start, "seconds.")