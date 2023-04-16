from django.shortcuts import render
# from django.views.decorators.http import require_http_methods


# @require_http_methods(["GET", "POST"])
def index(request):
    if request.method == 'POST':
        text = request.POST['text']
        mode = request.POST['mode']
        if mode.lower() == 'c':
            result = len(mode)
        elif mode.lower() == 'd':
            result = len(text.split())
        else:
            result =''
        return render(request,'index.html',{'result':result})
    else:
        return render(request,'index.html')



















    text1 = request.POST['text1']
    mode = request.POST['mode']
    if mode.lower == 'c':
        result = len(text1)
    elif(mode.lower == 'd'):
        result = len(text1.split())
    else:
        result = 'Wrong input Please try Again'
    return render(request,'index.html',{'result':result})
