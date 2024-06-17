import time
from selenium import webdriver
from bs4 import BeautifulSoup
# import pywhatkit as kit # no need to use pywhatkit here

def scrape_youtube_results(query):
    # Initialization
    driver = webdriver.Chrome()

    driver.get(f"https://www.youtube.com/results?search_query={query}")

    # Give time for the page to load this time is in seconds
    time.sleep(50)

    # Get the HTML content of the page
    html_content = driver.page_source 

    # print(html_content) # ---> uncomment if wanna view what content is stored in html_content, its mad large
    
    driver.quit() # Close the driver

    # Parse
    soup = BeautifulSoup(html_content, 'html.parser')

    video_titles = soup.find_all('a', {'id': 'video-title'}) # Find all video titles and timestamps
    video_timestamps = soup.find_all('span', {'class': 'style-scope ytd-thumbnail-overlay-time-status-renderer'})

    # Extract and print the title and timestamp of the first 10 videos
    for i in range(min(10, len(video_titles))):
        title = video_titles[i].get('title')
        timestamp = video_timestamps[i].text.strip()
        print(f"Title: {title}, Timestamp: {timestamp}")

search_query = input("Enter your search query : ")
scrape_youtube_results(search_query)