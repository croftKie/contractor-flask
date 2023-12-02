import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup as bs

def contractCheck(jobs_basic_info):
    def checkForContract(element):
        if element.text == "Contract":
            return element.text
    
    isContractJob = filter(checkForContract, job.find(".company"))
    if(len(list(isContractJob)) == 1):
        basic_info["contract"] = True
    else:
        basic_info["contract"] = False

    return basic_info

def urlCheck(jobs_basic_info, job):
    print(job.attrs)
    if("href" in job.attrs):
        return job.attr["href"]
    else:
        return ""

session = HTMLSession()

url = "https://weworkremotely.com/categories/remote-full-stack-programming-jobs#job-listings"
page = session.get(url)
page.html.render()

# jobs = page.html.find(".feature>a")
# job_titles = page.html.find(".title")
# job_links = [job.attrs for job in jobs]
# job_descriptions = []

# # for title in job_titles:
# #     print(title.text)
# for link in job_links:
#     job_url = "https://weworkremotely.com/" + link["href"]
#     job_listing = session.get(job_url)
#     job_listing.html.render()
#     description = job_listing.html.find("#job-listing-show-container>div")
#     job_descriptions = description

# for x in job_descriptions:
#     print(x.text)

jobs_basic_info = []

jobs = page.html.find(".feature")

for job in jobs:
    basic_info = {}
    basic_info["contract"] = contractCheck(basic_info)
    basic_info["url"] = urlCheck(basic_info, job)
    jobs_basic_info.append(basic_info)

print(jobs_basic_info)


# job_types = [job.find(".company") for job in jobs]
# for item in job_types:
#     for el in item:
#         if(el.text == "Contract"):
#             print(el.text)


