from django.shortcuts import render
import random
from django.conf import settings
from .models import MyUsers
from .forms import SignInForm, SignUpForm

# Create your views here.
def home(request):
#     form = ReviewForm(request.POST)
#     print(form)
    if request.COOKIES.get('mycookie'):
        user_name = request.COOKIES['mycookie']
        response = render(request, 'home.html', {'user_name': user_name, 'title' : 'D06'})
    else:
        #s'il n'y a pas de cookie ou le précédent est périmé
        user_name = random.choice(settings.USER_NAMES)
        response = render(request, 'home.html', {'user_name': user_name, 'title' : 'D06'})
        response.set_cookie('mycookie', user_name, max_age=settings.SESSION_COOKIE_DURATION)
    return response    

def sign_in(request):
    users = MyUsers.objects.all()
    if (request.method == "POST"):
        form = SignInForm(request.POST)
        if form.is_valid():
            form.save()
            form = SignInForm()
    else:
        form =  SignInForm()
    return render(request, 'form.html', {'users' : users, 'form': form })

def sign_up(request):
    if (request.method == "POST"):
        form = SignUpForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            password_verif = form.cleaned_data["password_verif"]
            if password == password_verif:
                user = auth.authenticate(username=username, 
                                        password=password) 
                if user and user.is_active:  # Si l'objet renvoyé n'est pas None,  par défaut is_active est False
                    auth.login(request, user)  # nous connectons l'utilisateur
                else: # sinon une erreur sera affichée
                    form._errors["username"] = ["This user doesn't exist."]
            else:
                form._errors["password"] = ["les mots de passe ne sont pas semblables"]
    else:
        form = SignUpForm()
    return render(request, 'ex/form.html', {'form': form })