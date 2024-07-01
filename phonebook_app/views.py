from django.shortcuts import render


def index(request):
    return render(request, 'phonebook_app/index.html')
