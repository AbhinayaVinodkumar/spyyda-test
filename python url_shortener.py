URL Shortner Logic
import random
import string
import json
import os
STORAGE_FILE = "url_mapping.json"
if os.path.exists(STORAGE_FILE):
    with open(STORAGE_FILE, "r") as f:
        url_to_code = json.load(f)
else:
    url_to_code = {}

code_to_url = {v: k for k, v in url_to_code.items()}
def save_mapping():
        with open(STORAGE_FILE, "w") as f:
        json.dump(url_to_code, f)
def generate_code(length=6):
    characters = string.ascii_letters + string.digits
    while True:
        code = ''.join(random.choice(characters) for _ in range(length))
        if code not in code_to_url:
            return code
def shorten(url):
    if url in url_to_code:
        return url_to_code[url]
    code = generate_code()
    url_to_code[url] = code
    code_to_url[code] = url
    save_mapping()
    return code
def redirect(code):
    return code_to_url.get(code)
if __name__ == "__main__":
    original_url = "https://www.example.com"
    code = shorten(original_url)
    print("Shortened code:", code)
    restored_url = redirect(code)
    print("Original URL:", restored_url)
How to run code?
Open a terminal or command prompt.
Navigate to the folder where your file is saved.
cd path_to_your_file
Run the Python file:
python url_shortener.py

Logical explanation
The URL shortener works by assigning each long URL a unique 6-character code. Two dictionaries store the mappings: url_to_code for URL → code and code_to_url for code → URL. When shorten(url) is called, it first checks if the URL already has a code; if not, it generates a random alphanumeric 6-character code and stores it in both dictionaries. The mappings are saved in a JSON file for persistence across program runs. When redirect(code) is called, the original URL is retrieved from code_to_url. This ensures fast lookups, uniqueness, and permanent storage of shortened URLs.


