from django.shortcuts import render
import requests


def index(request):
    try:
        access_key = 'f3EpnOsudMgghd4ork8hUNs8HTYcZ0mTTInxi10LsyA'
        url = f'https://api.unsplash.com/photos/random?client_id={access_key}'
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        if response.status_code == 200:
            data = response.json()
            image_url = data['urls']['regular']  # Example: get the regular size image URL
        else:
            image_url = "https://via.placeholder.com/500"  # Provide a fallback image URL
    except requests.RequestException as e:
        image_url = "https://via.placeholder.com/500"

    try:
        r1 = requests.get('https://uselessfacts.jsph.pl/random?language=en')
        r1.raise_for_status()  # Check if the request was successful
        res1 = r1.json()
        fact = res1['text']
    except (requests.RequestException, KeyError) as e:
        fact = "Could not retrieve a fact at this time."

    try:
        r2 = requests.get('https://api.adviceslip.com/advice')
        r2.raise_for_status()  # Check if the request was successful
        res2 = r2.json()
        advice = res2['slip']['advice']
    except (requests.RequestException, KeyError) as e:
        advice = "Could not retrieve advice at this time."

    try:
        r3 = requests.get('https://dog.ceo/api/breeds/image/random')
        r3.raise_for_status()  # Check if the request was successful
        res3 = r3.json()
        message = res3['message']
    except (requests.RequestException, KeyError) as e:
        message = "Could not retrieve a dog image at this time."

    photo = request.POST.get('photo') if request.method == 'POST' else None

    return render(request, 'index.html', {'fact': fact, 'advice': advice, 'dog_image': message, 'photo': photo, 'image_url': image_url})
