from django.http import HttpResponse, HttpResponseNotFound

# Create your views here.


def monthly_challenge(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "This is jan challenge"
    elif month == 'february':
        challenge_text = "This is feb challenge"
    elif month == 'march':
        challenge_text = "This is march challenge"
    else:
        return HttpResponseNotFound("This month aint supported!")
    return HttpResponse(challenge_text)


def monthly_challenge_by_num(request, month):
    challenge_text = None
    if month == 'january':
        challenge_text = "This is 1 challenge"
    elif month == 'february':
        challenge_text = "This is 2 challenge"
    elif month == 'march':
        challenge_text = "This is 3 challenge"
    else:
        return HttpResponseNotFound("This number month aint supported!")
    return HttpResponse(challenge_text)
