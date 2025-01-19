import requests

# Fetch data from a public API
response = requests.get('https://jsonplaceholder.typicode.com/posts')  # Using a valid API URL

# Check if the request was successful
if response.status_code == 200:
    data = response.json()
    # Print part of the JSON response
    for post in data[:5]:  # Print the first 5 posts
        print(f"Title: {post['title']}")
else:
    print(f"Failed to retrieve data: {response.status_code}")
