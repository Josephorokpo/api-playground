from django.shortcuts import render
import requests


def index(request):
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

    return render(request, 'templates/index.html', {'fact': fact, 'advice': advice, 'dog_image': message})
