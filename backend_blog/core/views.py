from django.shortcuts import render

# Create your views here.


def item_list(request):
    context ={
        "item" : item.objects.all()
    }
    return render(request, "item_list.html",context)
