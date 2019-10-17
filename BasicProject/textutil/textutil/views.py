from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    # use_anchor_tag = '''
    # <h1>Navigation Bar</h1><br>
    # <a href="https://www.youtube.com/watch?v=AepgWsROO4k&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=7" target="_blank">Google</a><br>'''
    # return HttpResponse(use_anchor_tag)
    params = {'name':'vikas','place':'Meerut'}
    return render(request,'index.html',params)


def caps(request):
    return HttpResponse('''
  <a href="/">Back</a>
  <br>
  Caps page
  ''')

def removepunc(request):
    djtext = request.GET.get('text','default')
    removepunch = request.GET.get('removepunc','Off')
    output = ""
    if removepunch == "on":
        punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        for char in djtext:
            if char not in punctuations:
                output += char
        param = {'purpose':'Removed Punctuation', 'analyzed':output}
        return render(request,'removepunch.html',param)
    else:
        return HttpResponse('Error!!')