from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "Bad request"
    elif month == 'february':
        challenge_text = "Not found"
    elif month == 'march':
        challenge_text = "I'm a teapot"
    else:
        return HttpResponseNotFound("This month aint supported!")
    return HttpResponse(challenge_text)
