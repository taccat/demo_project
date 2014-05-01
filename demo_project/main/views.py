"""
Views.
"""

from django.shortcuts import render
# from django.http import HTTPResponse

BASE_PAIRING = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A',
}


def home(request):
    context = {}

    # Check whether this request includes a query string to translate.
    # query_string = request.GET.get('query', None)
    # if query_string:
    #     query_string = query_string.upper()
    #     reverse_complement = ''
    #     for base in query_string:
    #         reverse_complement += BASE_PAIRING[base]
    #     context['query_string'] = query_string
    #     context['reverse_complement'] = reverse_complement

    query_string = request.GET.get('query', None)
    if query_string:
        query_string = query_string.upper()
        reverse_complement = ''
        for base in query_string:
            if base not in BASE_PAIRING:
                context[
                    'reverse_complement'] = "Not-bases detected. Here's a good link to learn more: http://en.wikipedia.org/wiki/DNA_bases"
                return render(request, 'home.html', context)
            else:
                reverse_complement += BASE_PAIRING[base]
        context['query_string'] = query_string
        context['reverse_complement'] = reverse_complement

    return render(request, 'home.html', context)
