from django.http import HttpResponse

# Create your views here.


def index(request):
    return HttpResponse("Hello, world!")


def febIndex(request):
    return HttpResponse("Hello february")
