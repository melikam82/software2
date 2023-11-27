import requests

def get_random_chuck_norris_joke():
    api_url = "https://api.chucknorris.io/jokes/random"
    response = requests.get(api_url)

    if response.status_code == 200:
        joke_data = response.json()
        joke_text = joke_data["value"]
        return joke_text
    else:
        return "Failed to fetch Chuck Norris joke. Please try again later."

def main():
    chuck_norris_joke = get_random_chuck_norris_joke()
    print("Chuck Norris Joke:")
    print(chuck_norris_joke)

if __name__ == "__main__":
    main()

