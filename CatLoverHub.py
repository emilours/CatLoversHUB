import os
from dotenv import load_dotenv
import requests
from flask import Flask, render_template, request, url_for

load_dotenv()
api_key = os.getenv('CAT_API_KEY')

headers = {
    'x-api-key': api_key
}

app = Flask(__name__)

def get_cats():
    url = f"https://api.thecatapi.com/v1/images/search?api_key={api_key}"
    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        data = response.json()
        
        if data:
            image_url = data[0]['url']
            
            breed_info = data[0].get('breeds', [])
            if breed_info:
                breed_info = breed_info[0]
            else:
                breed_info = None

            return image_url, breed_info
        else:
            return None, None
    else:
        print(f"Error: {response.status_code}, {response.text}")
        return None, None


def get_joke(category="Programming"):
    url = f"https://v2.jokeapi.dev/joke/{category}?type=single"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return data.get("joke", "Sorry, no joke found!")
    else:
        return "Sorry, something went wrong."

@app.route("/", methods=["GET", "POST"])
def index():
    image_url = None
    breed_info = None
    error_message = None
    joke = None
    display_joke = False

    if request.method == "POST":
        image_url, breed_info = get_cats()

        if not breed_info:
            joke = get_joke()
            display_joke = True
    
        if image_url is None:
            error_message = "Sorry, something went wrong. Please try again later."
    
    return render_template("index.html", image_url=image_url, breed_info=breed_info, error_message=error_message, joke=joke, display_joke=display_joke)

if __name__ == "__main__":
    app.run(debug=True)
