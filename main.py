"""Intent to creat an AI powered cover letter writting algorithm"""

import urllib.request as ul
from bs4 import BeautifulSoup as soup

url = 'https://www.linkedin.com/jobs/search/?currentJobId=2720228430&distance=25&f_E=1&f_JT=F%2CC%2CI&f_PP=106967730&f_WT=1%2C3&geoId=101282230&keywords=Full%20Stack%20Developer'
req = ul.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
client = ul.urlopen(req)
htmldata = client.read()
client.close()


pagesoup = soup(htmldata, "html.parser")
itemlocator = pagesoup.findAll('a', {"class":"disabled ember-view job-card-container__link job-card-list__title"})

# <h1 class="top-card-layout__title font-sans text-lg papabear:text-xl font-bold leading-open text-color-text mb-0 topcard__title">Praktikant Developer Full-Stack Python Finanz- &amp; Rechnungswesen (w/m/d)</h1>

offersTitle = []

for item in itemlocator:
    # print(item)
    # offer = item.findAll("span",{"class":"sr-only"})[0]
    title = item.text.strip()
    # print(title)
    offersTitle.append(title)

print(offersTitle)


# <div id="ember900" class="full-width artdeco-entity-lockup__title ember-view">
#             <a data-control-id="WivV+9DYUHbtKQVgzneNjA==" tabindex="0" href="/jobs/view/2720224983/?eBP=CwEAAAGEE8AcYFi6JV-hYuW0HEOCu7PvN_ZoJPSAX01FSLHVlx8jTQWQCHUhWhih-jjBAo7hwDtFv6t9ipucCkZVVXlGTH8fvBwm9x93qDOXrAb0XVUPHys_cVwUGDvy0Yn2sMMs__IMW1qsEPBQIVDzQrdq3ZxR9NOsB7hLrwoCmHUPSXS8k9b2hOqlvXucMhLtotfvHbdVQbIGYe2FkZmvAS2YRHJbNhiRNxMlmmmXlEkGtsyVg8_tPy6rh0XvXC1xsVSfkDjMXk-ipKj7c84YAnK3NPlPpLKBTBIm8Mx0hl61FLG1npVSQO-U6GjVH15pNYTE4OnomTp8RnD96DegwdWl9w&amp;refId=t1BpSBueZt5XKDX78ZRwiA%3D%3D&amp;trackingId=WivV%2B9DYUHbtKQVgzneNjA%3D%3D&amp;trk=flagship3_search_srp_jobs" id="ember901" class="disabled ember-view job-card-container__link job-card-list__title">
#               Werkstudent Developer (w/m/d)
#             </a>
      
# </div>

msg="Hello"
print(msg)