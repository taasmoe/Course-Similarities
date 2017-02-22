import timeit
import requests
import pickle
from lxml import html

start = timeit.default_timer()

all_page1 = requests.get("http://www.uio.no/studier/emner/matnat/ifi/")
all_tree1 = html.fromstring(all_page1.content)

all_page2 = requests.get("http://www.uio.no/studier/emner/matnat/ifi/?page=2&u-page=2")
all_tree2 = html.fromstring(all_page2.content)

all_courses_urls1 = all_tree1.xpath('//tbody/tr/td/a/@href')
all_courses_urls2 = all_tree2.xpath('//tbody/tr/td/a/@href')

all_courses_urls = all_courses_urls1 + all_courses_urls2

url_stem = "http://www.uio.no"

courses = {}

for url_ending in all_courses_urls:
    complete_url = url_stem + url_ending

    page = requests.get(complete_url)
    tree = html.fromstring(page.content)

    title = "".join(tree.xpath('//h1/text()')).strip("\t\n")
    about = " ".join(tree.xpath('//div[@id="course-content"]/*//text()')).strip("\t\n")
    outcome = " ".join(tree.xpath('//div[@id="learning-outcomes"]/*//text()')).strip("\t\n")

    courses[title] = {"about": about, "outcome": outcome, "url": complete_url}


with open('Data/courses.pkl', 'wb') as f:
    pickle.dump(courses, f, protocol=pickle.HIGHEST_PROTOCOL)

print("File saved!")

end = timeit.default_timer()

print("\nCompleted in", end - start, "seconds.")
