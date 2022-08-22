# I have created this file-mirfandev

from cgi import print_arguments
from string import punctuation
from django.http import HttpResponse
from django.shortcuts import render

# Code up to Exercise_1
# def index(request):
#     return HttpResponse("Home Page")


# def about(request):
#     return HttpResponse('''About Page
#     <a href = "https://www.youtube.com/">Youtube</a>
#     ''')
# # Code up to Exercise_1


# code_video_7
def index(request):
    # dic = {'name': 'irfan', 'degree': 'Bachelors'}
    # return render(request, 'index.html', dic)
    return render(request, 'index.html')
    # return HttpResponse("Home")


# def removepunc(request):
#     djtext = (request.GET.get('text', 'default value'))
#     # get the text
#     print(djtext)
#     # analyse the text
#     return HttpResponse("Remove_Punc<a href = '/'>Back</a>")


def analyze(request):

    djtext = request.GET.get('text', 'default')
    removepunc = request.GET.get('removepunc', 'off')
    print('removepunc')
    print(djtext)
    if removepunc == "on":
        punctuations = '''!()-[]{}: '"\, <> . /?@  # $%^&*_~'''
        analyzed = ""

        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char
        params = {'purpose': 'Remove Punctutations', 'analyzed_text': analyzed}
        return render(request, 'analyze.html', params)
    else:
        return HttpResponse("Error")
# get the text
# print(removepunc)

# def capfirst(request):
#     return HttpResponse("Capitalize First")


# def newlineremove(request):
#     return HttpResponse("newlineremove")


# def spaceremove(request):
#     return HttpResponse("spaceremove")


# def charcount(request):
#     return HttpResponse("charcount")
