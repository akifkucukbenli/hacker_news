import requests

url = "https://news.ycombinator.com/"

response = requests.get(url)

if response.status_code == 200:
    top_story_urls = response.json()
    for story_url in top_story_urls:
        print(story_url)

