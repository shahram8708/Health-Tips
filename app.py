from flask import Flask, render_template, request
import requests
import logging
import os
import markdown

app = Flask(__name__, static_url_path='/static')
logging.basicConfig(level=logging.DEBUG)

API_KEY = os.getenv('API_KEY')
if not API_KEY:
    raise ValueError("API_KEY environment variable is not set")

API_ENDPOINT = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={API_KEY}"

DEFAULT_TEXT = "Provide comprehensive information on health tips and treatments."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['POST'])
def search():
    query = request.form['search_query']
    if query:
        combined_query = DEFAULT_TEXT + " " + query
        response = generate_story(combined_query)
        logging.debug(f"API response: {response}")
        if response and 'candidates' in response:
            story_content, safety_ratings = extract_story_and_safety(response)
            if story_content:
                if is_safe_content(safety_ratings):
                    story_content_html = markdown.markdown(story_content)
                    return render_template('result.html', story_content=story_content_html)
                else:
                    error_msg = "Failed to retrieve content due to safety concerns. Please try again with a different query."
                    return render_template('index.html', error=error_msg)
        error_msg = "Failed to retrieve content. Please try again."
        return render_template('index.html', error=error_msg)
    else:
        error_msg = "Please enter a valid health-related query."
        return render_template('index.html', error=error_msg)

def generate_story(prompt):
    data = {
        "contents": [{"parts": [{"text": prompt}]}]
    }
    response = requests.post(API_ENDPOINT, json=data)
    if response.status_code == 200:
        return response.json()
    else:
        return None

def extract_story_and_safety(response):
    candidates = response.get('candidates', [])
    if candidates:
        candidate = candidates[0]
        content = candidate.get('content', {}).get('parts', [])
        if content:
            story_content = content[0].get('text', '')
        else:
            story_content = None
        safety_ratings = candidate.get('safetyRatings', [])
        return story_content, safety_ratings
    return None, None

def is_safe_content(safety_ratings):
    for rating in safety_ratings:
        if rating['probability'] == 'HIGH':
            return False
    return True

if __name__ == '__main__':
    app.run(debug=True)
