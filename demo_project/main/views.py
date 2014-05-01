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

# thanks waynesword.palomar.edu
dnaToAminoAcid = {
    # Dictionary of DNA codons to amino Acids
    'CGA': 'alanine',
    'CGG': 'alanine',
    'CGT': 'alanine',
    'CGC': 'alanine',
    'GCA': 'arginine',
    'GCG': 'arginine',
    'GCT': 'arginine',
    'GCC': 'arginine',
    'TCT': 'arginine',
    'TCC': 'arginine',
    'TTA': 'asparagine',
    'TTG': 'asparagine',
    'CTA': 'aspartate',
    'CTG': 'aspartate',
    'ACA': 'cysteine',
    'ACG': 'cysteine',
    'CTT': 'glutamate',
    'CTC': 'glutamate',
    'GTT': 'glutamine',
    'GTC': 'glutamine',
    'CCA': 'glycine',
    'CCG': 'glycine',
    'CCT': 'glycine',
    'CCC': 'glycine',
    'GTA': 'histidine',
    'GTG': 'histidine',
    'TAA': 'isoleucine',
    'TAG': 'isoleucine',
    'TAT': 'isoleucine',
    'AAT': 'leucine',
    'AAC': 'leucine',
    'GAA': 'leucine',
    'GAG': 'leucine',
    'GAT': 'leucine',
    'GAC': 'leucine',
    'TTT': 'lysine',
    'TTC': 'lysine',
    'TAC': 'methionine',
    'AAA': 'phenylalanine',
    'AAG': 'phenylalanine',
    'GGA': 'proline',
    'GGG': 'proline',
    'GGT': 'proline',
    'GGC': 'proline',
    'AGA': 'serine',
    'AGG': 'serine',
    'AGT': 'serine',
    'AGC': 'serine',
    'TCA': 'serine',
    'TCG': 'serine',
    'ATG': 'STOP',
    'ATT': 'STOP',
    'ACT': 'STOP',
    'TGA': 'threonine',
    'TGG': 'threonine',
    'TGT': 'threonine',
    'TGC': 'threonine',
    'ACC': 'tryptophan',
    'ATA': 'tyrosine',
    'ATG': 'tyrosine',
    'CAA': 'valine',
    'CAG': 'valine',
    'CAT': 'valine',
    'CAC': 'valine'
}


def converter(baseSequence):

    # Converts DNA codon to amino acid according to dictionary.
    counter = 1
    codon = ''
    returnedSequence = ''
    for x in baseSequence:

        codon += x
        if counter != 0 and counter % 3 == 0:
            returnedSequence += dnaToAminoAcid[codon]
            returnedSequence += ' '
            codon = ''
        counter += 1
    return returnedSequence

print converter('ACCCAGTGA')


def home(request):
    context = {}

    # Check whether this request includes a query string to translate.
    query_string = request.GET.get('query', None)
    if query_string:
        query_string = query_string.upper()
        reverse_complement = ''

        for base in query_string:

            # checks if base in allowed bases; returns error message if not.
            if base not in BASE_PAIRING:
                context[
                    'reverse_complement'] = "Not-bases detected. Here's a good link to learn more: http://en.wikipedia.org/wiki/DNA_bases"
                return render(request, 'home.html', context)

            else:

                # quick base pairing.
                reverse_complement += BASE_PAIRING[base]

                # runs converter on converted bases.
                aa = converter(reverse_complement)
                if aa == '':
                    context['amino_acids'] = 'Sorry, not enough bases.'
                else:
                    context['amino_acids'] = aa

        context['query_string'] = query_string
        context['reverse_complement'] = reverse_complement

    return render(request, 'home.html', context)
