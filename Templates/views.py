# i have created this file - dj
from django.http import HttpResponse
from django.shortcuts import render

# def index(request):
#     return HttpResponse("<h1>dhanu</h1>")
#
# def about(request):
#     return HttpResponse("About dhanu bhau")
# tut 7 code

def index(request):
    return render(request, 'index.html',)
    # return HttpResponse("Home")

def analyze(request):
    # get the text
    djtext = request.POST.get('text', 'default')
    # check checkbox values
    removepunc = request.POST.get('removepunc', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    newlineremover = request.POST.get('newlineremover', 'off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    # print(removepunc)
    # print(djtext)

    # check which checkbox is on
    if removepunc == "on":
        punctuations = '''!()-[]{};:'",<>./?@#$%^&*_~'''
        analyzed = ""
        for char in djtext:
            if char not in punctuations:
                analyzed = analyzed + char

        params = {'purpose': 'Removed punctuations', 'analyzed_text': analyzed}

        return render(request, 'analyze.html', params)

    elif(fullcaps=="on"):
        analyzed = ""
        for char in djtext:
            analyzed = analyzed + char.upper()

        params = {'purpose': 'Changed to Uppercase', 'analyzed_text':
 analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif(extraspaceremover=="on"):
        analyzed = ""
        for index, char in enumerate(djtext):
            if not(djtext[index] == " "and djtext[index+1]==" "):
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text':
            analyzed}
        # Analyze the text
        return render(request, 'analyze.html', params)

    elif (newlineremover == "on"):
        analyzed = ""
        for char in djtext:
            if char != "\n" and char!="\r":
                analyzed = analyzed + char

        params = {'purpose': 'Removed NewLines', 'analyzed_text':
            analyzed}
        return render(request, 'analyze.html', params)

    else:
        return HttpResponse("Error")

# def capfirst(request):
#     return HttpResponse("capitalize first")
#
# def newlineremove(request):
#     return HttpResponse("new line")
#
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</sa>")
#
# def charcount(request):
#     return HttpResponse("char count")
#
# def spaceremove(request):
#     return HttpResponse("space remover <a href='/'>back</sa>")



