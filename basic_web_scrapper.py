import requests
from bs4 import BeautifulSoup
def scrap_the_webpage(url):
    page = requests.get(url)
    if page.status_code == 200:
       print("Page fetched successfully")
    else:
        print("Something went wrong")

    html_content = page.text
    soup = BeautifulSoup(html_content,'html.parser')
    headings = soup.find_all(['h1','h2','h3'])
    print("Major heading of this article are: ")
    for heading in headings:

        print(heading.text.strip())





def main():
    url = input("please give the url for scrapping\n")
    scrap_the_webpage(url)
if __name__ == '__main__':
    main()