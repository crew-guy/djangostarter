from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

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


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())
    for month in months:
        capitalized_month = month.capitalize()
        list_items += f"<li><a href=\"{month}\" >{capitalized_month}</a></li>"
    response_data = f"<ul>{list_items}</ul>"
    return HttpResponse(response_data)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        challenge_data = f"<h1>{challenge_text}</h1>"
        return HttpResponse(challenge_data)
    except:
        return HttpResponseNotFound("<h1>This month aint supported!</h1>")


def monthly_challenge_by_num(request, month):
    months = list(monthly_challenges.keys())
    if month > len(months):
        return HttpResponseNotFound('This number month aint supported!')
    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)
