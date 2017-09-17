from django.shortcuts import render, redirect


def index(request):
    return redirect('about')

def about(request):
    return render(request, 'website/about.html')

def analysis(request):
    return render(request, 'website/analysis.html')

def visualization(request):
    return render(request, 'website/visualization.html')
