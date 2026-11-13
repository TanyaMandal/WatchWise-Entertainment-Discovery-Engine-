# WatchWise-Entertainment-Discovery-Engine-
# WatchWise

A movie and TV show recommendation app built with Python and Streamlit. Instead of scrolling endlessly through categories, you can describe the kind of mood, plot, or vibe you're looking for and get tailored suggestions.

## How it works
- `app.py` handles the backend logic and API calls for generating recommendations.
- `streamlit_ui.py` runs the frontend web interface.

## Setup

1. **Clone the repo**
   ```bash
   git clone [https://github.com/TanyaMandal/WatchWise-Entertainment-Discovery-Engine-.git](https://github.com/TanyaMandal/WatchWise-Entertainment-Discovery-Engine-.git)
   cd WatchWise-Entertainment-Discovery-Engine-

## Create a virtual environment and install dependencies
```bash
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

## Add your API key
Create a .env file in the root folder and add your key:
```bash
YOUR_API_KEY_NAME=your_key_here
```
## Run the app
```bash
streamlit run streamlit_ui.py ```