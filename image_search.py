import requests
import webbrowser

from bs4 import BeautifulSoup
from time import sleep

# takes in a path to an image and returns google search results for that image
def reverse_image_search( image_path ):
    # add header
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/54.0.2840.71 Safari/537.36'
    }

    searchUrl = 'http://www.google.com/searchbyimage/upload'
    multipart = {'encoded_image': (image_path, open(image_path, 'rb')), 'image_content': ''}
    # do the image search with a POST request
    response = requests.post(searchUrl, files=multipart, allow_redirects=False)
    url = response.headers['Location']

    # parse the html using beautiful soup and store in variable `html`
    # html = BeautifulSoup(url, 'html.parser')

    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content)
    links = soup.findAll("a")   
    for link in links:
        print(link.get('href'))

    #print(links)
    #webbrowser.open(url)

# main method
def main():
    filePath = './images/couch.jpg'
    amazon_url = 'http://www.amazon.com/dp/B00VUTAFR8'
    reverse_image_search(filePath)
    #get_product_price()

if __name__ == '__main__':
    main()