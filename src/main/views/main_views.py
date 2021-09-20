from django.shortcuts import render
from django.views.generic import RedirectView


def main_page(request):
    return render(request, 'main/main-page.html')


class RedirectToMainView(RedirectView):
    permanent = False
    query_string = True
    pattern_name = 'main'
