from bs4 import BeautifulSoup
import requests
import os

def searchInURL():

    source= "https://en.wikipedia.org/wiki/Deep_learning"
    response= requests.get(source).text
    soup= BeautifulSoup(response, "lxml")
    # Printing the title
   # wikititle =soup.title
    Title = soup.title.text
    print("Title is:",Title)

    # Writing results into a file
    with open("output1.html", "a") as file:
        file.write(str(Title))


    #looping through the all a tags
    for links in soup.find_all('a'):
        # fetching href's
        hrefs=links.get('href')
        with open("output1.html", "a") as file:
            file.write(str(hrefs))
            file.write("\n")
        print(hrefs)



if __name__== '__main__':
    #function call
    searchInURL()
