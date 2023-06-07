from mitrecve import crawler
from pprint import pprint
from pycvesearch import CVESearch

# Get the CVE details

if __name__ == "__main__":
  # cve = CVESearch('https://cve.circl.lu')
  print(crawler.get_main_page('CVE-2015-6420'))
  # print(cve.id('CVE-2014-0160'))
  # cve.search('spring-2.5.6')
1