from django.shortcuts import render
from django.contrib.auth import authenticate
from django.views.generic import View


from .forms import LoginForm

# Create your views here.
class LoginView(View):
    def get(self, request):
        return render(request, "user.html", {})

    def post(sefl, request):
        #login_form = LoginForm(request.POST)
        user_name = request.POST.get("username", "")
        pass_word = request.POST.get("password", "")
        user = authenticate(username=user_name, password=pass_word)
        if user is not None:
            #if User.objects.get()
            login(request, user)
            return render(request, "admin.html", {})
        else:
            return render(request, "login.html", {"msg": "用户名或密码错误"})

class AdminExamineView(View):
    def get(self, request):
        return render(request, 'examine.html', {})

    def post(self, request):
        pass

class RechargeView(View):
    def get(self, request):
        return render(request, 'recharge.html', {})

    def post(self, request):
        pass

class ModifyPasswordView(View):
    def get(self, request):
        return render(request, 'password.html', {})

    def post(self, request):
        pass

class ReleaseListView(View):
    def get(self, request):
        return render(request, 'home.html', {})

    def post(self, request):
        pass
