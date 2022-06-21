from django.shortcuts import render


def main_page(request):
    return render(request, 'main/main-page.html')


def about_page(request):
    return render(request, 'main/about.html')
