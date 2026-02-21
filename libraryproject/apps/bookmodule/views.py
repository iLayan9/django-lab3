from django.shortcuts import render


from django.http import HttpResponse

#Task1:
#def index(request):
#    return HttpResponse("Hello world")

#Task2:
#def index(request):
#    name = request.GET.get("name") or "world"
#    return HttpResponse("Hello " + name)


#Task3:
def index2(request, val1=0):
    return HttpResponse("value1 = " + str(val1))

#task4:
def task4(request):
    return render(request, "bookmodule/index.html")



#def index2(request, val1=0):
#    return HttpResponse("value1 = " + str(val1))

#task5
def index(request):
    name = request.GET.get("name") or "world"
    return render(request, "bookmodule/index.html", {"name": name})

#def index2(request, val1=0):
#    return HttpResponse("value1 = " + str(val1))

#task7
def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}

    targetBook = None
    if book1['id'] == bookId:
        targetBook = book1
    if book2['id'] == bookId:
        targetBook = book2

    context = {'book': targetBook}  # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)
