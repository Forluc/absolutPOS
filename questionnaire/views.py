from django.shortcuts import redirect, render

from questionnaire.forms import ProfileForm, SurveyForm, UserForm
from questionnaire.models import Question, Survey, User
from questionnaire.saving_to_google_form import save_response


def index(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user_form.save()
            request.session['email'] = user_form.cleaned_data['email']
            return redirect('create_company')
        else:
            return redirect('index')
    else:
        user_form = UserForm()
    return render(request, 'index.html', {'user_form': user_form})


def create_company(request):
    if request.method == 'POST':
        profile_form = ProfileForm(data=request.POST)
        if profile_form.is_valid():
            user_email = request.session.get('email')
            user = User.objects.get(email=user_email)
            profile = profile_form.save(commit=False)
            profile.email = user
            profile.save()

            request.session['company'] = profile_form.cleaned_data['company']
            request.session['address'] = profile_form.cleaned_data['address']
            request.session['direction'] = profile_form.cleaned_data['direction']
            request.session['is_new'] = profile_form.cleaned_data['is_new']

            return redirect('company_response', survey_id=Survey.objects.get(name=profile.direction).id)
        else:
            return redirect('index')
    else:
        user_email = request.session.get('email')
        user = User.objects.get(email=user_email)
        profile_form = ProfileForm(initial={'email': user.email})
    return render(request, 'create_company.html', {'profile_form': profile_form})


def company_response(request, survey_id):
    survey = Survey.objects.get(id=survey_id)

    if request.method == 'POST':
        survey_form = SurveyForm(request.POST, survey=survey)
        if survey_form.is_valid():
            save_response(survey_form.cleaned_data, request.session)
            return redirect('index')
    else:
        survey_form = SurveyForm(survey=survey)

    return render(request, 'company_response.html', {'survey_from': survey_form, 'survey': survey})


def questionnaire(request):
    return render(request, 'questionnaire.html', {'questionnaires': Survey.objects.all()})


def questions(request):
    return render(request, 'questions.html', {'questions': Question.objects.all()})
