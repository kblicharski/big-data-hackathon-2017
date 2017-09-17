from django.shortcuts import render


def index(request):
    return render(request, 'website/index.html')

def visualization(request):
    return render(request, 'website/texas.html')
