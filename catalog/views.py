from django.shortcuts import render
# Create your views here.

def home(request):
    return render(request, 'catalog/home.html')

def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(name, phone,'\n',message)
    return render(request, 'catalog/contacts.html')

def catalog(request):
    return render(request,'catalog/catalog.html')