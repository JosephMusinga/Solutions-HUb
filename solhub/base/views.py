from django.shortcuts import render

# Create your views here.
rooms=[
    {'id':1, 'name':'Dept1'},
    {'id':2, 'name':'Dept2'},
    {'id':3, 'name':'Dept3'},

]

def home(request):
    context = {'rooms':rooms}
    return render(request, 'base/home.html', context)

def room(request, pk):
    return render(request, 'base/room.html')