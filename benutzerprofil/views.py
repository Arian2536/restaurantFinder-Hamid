from django.http import HttpResponse

def languages(requeset):
    # body

    return  HttpResponse('<h1><u>Please select your language :</u></h1>')


def home(request):
    return HttpResponse('<h3> Welcome to your Restaurant...</h3>')