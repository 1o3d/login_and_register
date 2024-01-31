from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user
from .forms import PersonalQuestionsForm, ClipboardForm
from .models import PersonalQuestions, Clipboard
from django.contrib.auth.decorators import login_required


# Create your views here.

def register(response):
    if response.method == 'POST':
        form = RegistrationForm(response.POST)
        if form.is_valid():
            form.save()
            return redirect('/login')
    else:
        form = RegistrationForm()
    return render(response, 'register/register.html', {'form': form})


def login(request):
    return render(request, 'registration/login.html')


def home(response):
    return render(response, 'register/home.html')


def get_personal_answer(response):
    question = PersonalQuestions.question
    answer = PersonalQuestions.answer
    user = PersonalQuestions.user
    return render(response, 'register/home.html', {'question': question, 'answer': answer, 'user': user})


# def profile(request, user):
#     if request.user.is_authenticated:
#         return render(request, 'profile.html', {'user': user})
#     else:
#         return render(request, 'profile.html', {'user': user})
#         return redirect('/login')

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user.username})


@login_required
def your_profile(request):
    username = request.user.username
    email = request.user.email
    first_name = request.user.first_name
    last_name = request.user.last_name
    form = PersonalQuestionsForm(request.POST)

    if request.method == 'POST':
        model_form = PersonalQuestionsForm(request.POST)
        mod = PersonalQuestions.objects.create(user=request.user, question=model_form.question, answer=model_form.answer)
        if model_form.is_valid():
            mod.save()
    else:
        form = PersonalQuestionsForm()
    context = {'username': username, 'email': email, 'first_name': first_name, 'last_name': last_name, 'form': form}
    return render(request, 'register/your_profile.html', context)


def submit_personal_question(req):
    if req.method == 'POST':
        mod = PersonalQuestions(req.POST)
        form = PersonalQuestionsForm(req.POST)
        if form.is_valid():
            mod.save()


@login_required
def log_out_view(request):
    logout(request)
    return render(request, 'logout.html')


@login_required()
def clipboard(request):
    form = ClipboardForm()
    if request.method == 'POST':
        form = ClipboardForm(request.POST)
        if form.is_valid():
            form.save(commit=False)

    info = Clipboard.objects.filter(user=request.user).values()
    context = {'form': form, 'info':info}
    return render(request, 'register/clipboard.html', context)


def clipboard_to_db(req):
    form = ClipboardForm(req)
    if form.is_valid():
        form.save()
        pass


def contact_view(request):
    return render(request, 'register/contactme.html')
