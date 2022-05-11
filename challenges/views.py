from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect

# Create your views here.

monthly_challenges = {
    "january": "This is january challenge",
    "february": "This is february challenge",
    "march": "This is march challenge",
    "april": "This is april challenge",
    "may": "This is may challenge",
    "june": "This is june challenge",
    "july": "This is july challenge",
    "august": "This is august challenge",
    "september": "This is september challenge",
    "october": "This is october challenge",
    "november": "This is november challenge",
    "december": "This is december challenge",
}


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This month aint supported!")


def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('This number month aint supported!')
    redirect_month = months[month - 1]
    return HttpResponseRedirect('/challenges/' + redirect_month)
