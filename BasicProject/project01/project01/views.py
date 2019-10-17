# views.py
# I have created this file - Harry
from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

    # return HttpResponse("Home")

def analyzed(request):
    #Get the text
    djtext = request.GET.get('text', 'default')

    # Check checkbox values
    removepunc = request.GET.get('removepunc', 'off')
    fullcaps = request.GET.get('uppercase', 'off')
    newlineremover = request.GET.get('newlineremover', 'off')
    extraspaceremover = request.GET.get('extraspaceremover', 'off')
    # print(removepunc,fullcaps,newlineremover,extraspaceremover,sep=" ")

    return checking_fun(djtext,removepunc,fullcaps,newlineremover,extraspaceremover)
    #Check which checkbox is on
    # if removepunc == "on":
    #     punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    #     analyzed = ""
    #     for char in djtext:
    #         if char not in punctuations:
    #             analyzed = analyzed + char
    #     params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
    #     return render(request, 'analyzed.html', params)

    # else:
    #     return HttpResponse("Error")

def checking_fun(txt,rm,fcap,nline,espace):
    if rm == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed = ""
        for char in txt:
            if char not in punctuations:
                analyzed = analyzed + char
        if fcap = "on":
            params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed.upper()}
        else:
            params = {'purpose':'Removed Punctuations', 'analyzed_text': analyzed}
        return render(request, 'analyzed.html', params)
    else:
        return HttpResponse("Error")


# def removepunc(request):
#     djtext = request.GET.get('text', 'default')
#     return render (request,'views.analyzed')
    # return HttpResponse("remove punc")

# def capfirst(request):
#     return HttpResponse("capitalize first")

# def newlineremove(request):
#     return HttpResponse("newline remove first")


# def spaceremove(request):
#     return HttpResponse("space remover back")

# def charcount(request):
#     return HttpResponse("charcount ")