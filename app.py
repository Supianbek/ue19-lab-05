import requests

def fetch_joke():
    url = "https://v2.jokeapi.dev/joke/Any"
    try:
        response = requests.get(url)
        response.raise_for_status()
        joke_data = response.json()
        
        if joke_data["type"] == "single":
            return joke_data["joke"]
        elif joke_data["type"] == "twopart":
            return f"{joke_data['setup']} ... {joke_data['delivery']}"
        else:
            return "Pas de blague trouvée."
    except requests.exceptions.RequestException as e:
        return f"Erreur lors de l'accès à l'API : {e}"

if __name__ == "__main__":
    joke = fetch_joke()
    print(f"Voici une blague pour vous :\n{joke}")
