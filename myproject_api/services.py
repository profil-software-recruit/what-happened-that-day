import requests


def get_fact(month, day):
    return requests.get(f'http://numbersapi.com/{month}/{day}/date').text
