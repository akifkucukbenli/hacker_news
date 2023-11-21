

import requests
def get_top_news():

    url = "https://hacker-news.firebaseio.com/v0/topstories.json?print=pretty"

    response = requests.get(url)

    if response.status_code == 200:
        top_story_ids = response.json()[:30]
        for story_id in top_story_ids:
            story_url = f"https://hacker-news.firebaseio.com/v0/item/{story_id}.json?print=pretty"
            story_response = requests.get(story_url)
            if story_response.status_code == 200:
                story_data = story_response.json()
                print(f"Title: {story_data['title']}")
                print(f"URL: {story_data.get('url', 'N/A')}")
                print(f"Score: {story_data.get('score', 'N/A')}")
                print("-" * 30)
            else:
                print(print(f"Failed to fetch story with ID {story_id}. Status Code: {story_response.status_code}"))
    else:
        print(f"Failed to fetch top stories. Status Code: {response.status_code}")


if __name__ == "__main__":
    get_top_news()