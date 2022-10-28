from django.shortcuts import render
from Login_app.forms import UserForm, UserInfoForm


# Create your views here.
def index(request):
    diction = {}
    return render(request, 'Login_app/index.html', context=diction)

def register(request):
    user_form = UserForm()
    user_info_form = UserInfoForm()

    diction = {'user_form':user_form, 'user_info_form':user_info_form}
    return render(request, 'Login_app/register.html', context=diction)
