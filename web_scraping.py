import timeit
import requests
import pickle
from lxml import html

start = timeit.default_timer()

# The first page of courses, containing 250 urls
all_page1 = requests.get("http://www.uio.no/studier/emner/matnat/ifi/")
all_tree1 = html.fromstring(all_page1.content)

# The second page of courses, containing 42 urls
all_page2 = requests.get("http://www.uio.no/studier/emner/matnat/ifi/?page=2&u-page=2")
all_tree2 = html.fromstring(all_page2.content)

# Retrieving all urls from the html elements
all_courses_urls1 = all_tree1.xpath('//tbody/tr/td/a/@href')
all_courses_urls2 = all_tree2.xpath('//tbody/tr/td/a/@href')

# Joining them to a single list
all_courses_urls = all_courses_urls1 + all_courses_urls2

url_stem = "http://www.uio.no"

courses = []

# For each url our list of urls, we retreive the title of the course, and the relevant content.
for url_ending in all_courses_urls:
    complete_url = url_stem + url_ending

    page = requests.get(complete_url)
    tree = html.fromstring(page.content)

    title = "".join(tree.xpath('//h1/text()')).strip("\t\n")
    about = " ".join(tree.xpath('//div[@id="course-content"]/*//text()')).strip("\t\n")
    outcome = " ".join(tree.xpath('//div[@id="learning-outcomes"]/*//text()')).strip("\t\n")

    # We join together the course description and its learing outcome
    courses.append((title, about + ' ' + outcome))


# Stores the retrieved data using pickle
with open('Data/courses.pkl', 'wb') as f:
    pickle.dump(courses, f, protocol=pickle.HIGHEST_PROTOCOL)

print("File saved!")

end = timeit.default_timer()

print("\nCompleted in", end - start, "seconds.")
