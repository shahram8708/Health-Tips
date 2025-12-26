# Health Tips Web Application

Health Tips is a Flask-based web application that provides health-related guidance using the Google Generative Language API (Gemini-Pro). Users can submit a health query, and the application returns comprehensive health tips and treatment-related information. Generated content is safety-checked, converted from Markdown to HTML, and displayed in a readable modern interface with additional copy and text-to-speech support.

---

## Overview

The application runs a Flask backend that:

* Serves a simple, well-styled web interface
* Accepts a health-related text query
* Sends the request to the Gemini-Pro API
* Applies safety filtering to AI responses
* Renders the AI response as readable HTML
* Provides copy and speech playback controls

An internal default helper prompt is combined with the user query to guide the AI toward providing useful health guidance.

---

## Features

* Submit any health-related query
* Uses Gemini-Pro to generate detailed health tips
* Safety evaluation to block unsafe responses
* Markdown to HTML conversion for clean presentation
* Copy to clipboard support
* Text-to-speech playback controls
* Error handling with user-friendly messages
* Responsive and readable UI with separate result page

---

## Tech Stack

* **Backend:** Python, Flask
* **HTTP Client:** Requests
* **Rendering:** markdown
* **Frontend:** HTML, CSS, JavaScript
* **API:** Google Generative Language API (Gemini-Pro)
* **Logging:** Python logging module

---

## Project Structure

```
Health-Tips-main/
│
├── app.py                     # Flask backend and AI handling
├── requirements.txt           # Dependencies
│
└── templates/
    ├── index.html             # Input page
    └── result.html            # Result display page
```

---

## Installation

1. Ensure Python is installed.
2. Extract the project folder.
3. Open a terminal in the project directory.
4. Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Configuration

The application requires a valid Google Generative Language API key.

Set the environment variable before running the app:

**Linux / macOS**

```bash
export API_KEY="YOUR_API_KEY"
```

**Windows (PowerShell)**

```powershell
setx API_KEY "YOUR_API_KEY"
```

If the environment variable is missing, the application will not start.

Internet access is required.

---

## Running the Application

Start the Flask server:

```bash
python app.py
```

The application runs in debug mode.
Open your browser and visit:

```
http://127.0.0.1:5000
```

---

## Usage

1. Open the web application.
2. Enter a health-related query in the input field.
3. Click **Get Tips**.
4. Wait for AI-generated guidance to appear on the results page.
5. Optionally:

   * Copy the generated content using the Copy button
   * Use Play and Stop to listen via text-to-speech

If the system detects unsafe content or cannot retrieve a response, a clear error message is shown.

---

## Notes

* Safety ratings with “HIGH” probability are rejected.
* Responses are converted from Markdown to HTML before display.
* Logging outputs useful debug details.
* Requires active internet connectivity.

---

## Dependencies

Defined in `requirements.txt`:

```
Flask
requests
markdown
gunicorn
```

---

## License

No license file is included in this project.
