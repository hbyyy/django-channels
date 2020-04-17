import requests
from django.shortcuts import render


# Create your views here.


def index(request):
    context = {
        'client_id': '935204026920614',
    }
    return render(request, 'members/index.html', context)


def hello(request):
    code = request.GET['code']
    print(code)
    params = {
        'client_id': '935204026920614',
        'redirect_uri': "http://localhost:8000/test/",
        'client_secret': "b7c004f382e0a999ecf4c1e119645dd7",
        'code': code
    }

    url = "https://graph.facebook.com/v6.0/oauth/access_token"
    request_url = "{url}?{params}".format(
        url=url,
        params='&'.join([f'{key}={value}' for key, value in params.items()])
    )
    print(request_url)
    response = requests.get(request_url)
    print(response.json())
    print(type(response.json()))
    return render(request, 'members/hello.html', context={'response': response.text})
