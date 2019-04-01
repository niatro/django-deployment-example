from django.shortcuts import render
from appAlone.models import User

# Create your views here.

def index(request):
    return render(request,'appAlone/index.html')

def users(request):
    user_list = User.objects.order_by('first_name')
    user_dict = {'users':user_list}
    return render(request,'appAlone/users.html',context=user_dict)
