"""
Views.
"""

from django.shortcuts import render

BASE_PAIRING = {
    'A': 'T',
    'C': 'G',
    'G': 'C',
    'T': 'A',
}

def home(request):
    context = {}

    # Check whether this request includes a query string to translate.
    query_string = request.GET.get('query', None)
    if query_string:
        query_string = query_string.upper()
        reverse_complement = ''
        if query_string not in base:
            context ['query_string'] = query_string
            context ['reverse_complement'] = "Here's a good link to learn more: http://en.wikipedia.org/wiki/DNA_bases"
        else:
            for base in query_string:
                reverse_complement += BASE_PAIRING[base]
            context['query_string'] = query_string
            context['reverse_complement'] = reverse_complement

    return render(request, 'home.html', context)
