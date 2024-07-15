from django.shortcuts import render
import requests
import logging

# Set up logging
logger = logging.getLogger(__name__)

def index(request):
    access_key = 'f3EpnOsudMgghd4ork8hUNs8HTYcZ0mTTInxi10LsyA'
    image_url = "https://example.com/default-image.jpg"  # Default image URL

    if request.method == 'POST':
        search_term = request.POST.get('image_url', '')
        if search_term:
            try:
                url = f'https://api.unsplash.com/photos/random?query={search_term}&client_id={access_key}'
                response = requests.get(url)
                response.raise_for_status()  # Check if the request was successful

                if response.status_code == 200:
                    data = response.json()
                    image_url = data['urls']['regular']  # Example: get the regular size image URL
                else:
                    logger.warning("Received a non-200 response from Unsplash API")
            except requests.RequestException as e:
                logger.error(f"Error fetching Unsplash image: {e}")

    try:
        r1 = requests.get('https://uselessfacts.jsph.pl/random.json?language=en')
        r1.raise_for_status()  # Check if the request was successful
        res1 = r1.json()
        fact = res1['text']
    except requests.RequestException as e:
        logger.error(f"Error fetching fact: {e}")
        fact = "Could not retrieve a fact at this time."
    except KeyError:
        logger.error("Error parsing fact response")
        fact = "Could not retrieve a fact at this time."

    try:
        r2 = requests.get('https://api.adviceslip.com/advice')
        r2.raise_for_status()  # Check if the request was successful
        res2 = r2.json()
        advice = res2['slip']['advice']
    except requests.RequestException as e:
        logger.error(f"Error fetching advice: {e}")
        advice = "Could not retrieve advice at this time."
    except KeyError:
        logger.error("Error parsing advice response")
        advice = "Could not retrieve advice at this time."

    try:
        r3 = requests.get('https://dog.ceo/api/breeds/image/random')
        r3.raise_for_status()  # Check if the request was successful
        res3 = r3.json()
        message = res3['message']
    except requests.RequestException as e:
        logger.error(f"Error fetching dog image: {e}")
        message = "Could not retrieve a dog image at this time."
    except KeyError:
        logger.error("Error parsing dog image response")
        message = "Could not retrieve a dog image at this time."

    if request.method == 'POST':
        photo = request.POST.get('photo')
    else:
        photo = None

    return render(request, 'index.html', {'fact': fact, 'advice': advice, 'dog_image': message, 'photo': photo, 'image_url': image_url})
