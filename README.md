# API Playground

API Playground is a Django application that integrates multiple APIs to display random facts, advice, dog images, and images from Unsplash based on user input. 

## Features

- Fetches a random fact from [uselessfacts.jsph.pl](https://uselessfacts.jsph.pl/random?language=en)
- Fetches a random advice from [api.adviceslip.com](https://api.adviceslip.com/advice)
- Fetches a random dog image from [dog.ceo](https://dog.ceo/api/breeds/image/random)
- Fetches a random image from [Unsplash](https://unsplash.com/) based on user input

## Getting Started

### Prerequisites

- Python 3.x
- Django 3.x or later
- Requests library
 
### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/api-playground.git
   cd api-playground

2. **Create and activate a virtual environment:
	python3 -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

3. **Install the required packages:
	pip install -r requirements.txt

4. **Set up the database:
	SQLite (default): python manage.py migrate

5. **Usage
#Access the application:
Open your browser and go to http://127.0.0.1:8000/.

#Interact with the application:

Enter a word in the search box to fetch an image from Unsplash.
View random facts, advice, and dog images displayed on the page.

6. **API Keys
	To use the Unsplash API, you need to set up the API keys:

Sign up at Unsplash and get your API credentials.
Add the UNSPLASH_ACCESS_KEY and UNSPLASH_SECRET_KEY to your environment variables.

7. **Project Structure
	api-playground/
├── api_playground/
│   ├── __init__.py
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── templates/
│   └── index.html
├── static/
│   └── styles.css
├── views.py
├── manage.py
└── requirements.txt

8.  **Acknowledgments
uselessfacts.jsph.pl
api.adviceslip.com
dog.ceo
Unsplash
https://randomapi.vidito.reple.co




