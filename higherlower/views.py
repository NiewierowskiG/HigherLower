from django.shortcuts import render

def higherlower(request):
    context = {}
    try:
        print(request.url1)
    except AttributeError:
        print("ejoooo")
    request.url1 = "eoooooooo"
    return render(request, "higherlower/higherlower.html", context)
