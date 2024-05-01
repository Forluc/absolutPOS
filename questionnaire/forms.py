from django import forms

from .models import Profile, User


class ProfileForm(forms.ModelForm):
    DIRECTION_CHOICES = [
        ('', 'Выберите тип компании'),
        ('bar', 'Бар'),
        ('restaurant', 'Ресторан'),
        ('cafe', 'Кафе'),
        ('other', 'Другое'),
    ]
    company = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-8 mb-4 py-3 px-5 border-0 fs_24 SelfStorage__bg_lightgrey',
        'placeholder': 'Укажите название компании'
    }))
    address = forms.CharField(widget=forms.TextInput(attrs={
        'class': 'form-control border-8 mb-4 py-3 px-5 border-0 fs_24 SelfStorage__bg_lightgrey',
        'placeholder': 'Укажите адрес компании'
    }))
    direction = forms.ChoiceField(choices=DIRECTION_CHOICES, widget=forms.Select(attrs={
        'class': 'form-control border-8 mb-4 py-3 px-5 border-0 fs_24 SelfStorage__bg_lightgrey'
    }))
    is_new = forms.BooleanField(label='Is New', required=False)

    class Meta:
        model = Profile
        fields = ('company', 'address', 'is_new', 'direction')


class UserForm(forms.ModelForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={
        'class': 'form-control border-8 mb-4 py-3 px-5 border-0 fs_24 SelfStorage__bg_lightgrey',
        'placeholder': 'Укажите ваш электронный адрес'}))

    class Meta:
        model = User
        fields = ('email',)


class SurveyForm(forms.Form):
    def __init__(self, *args, **kwargs):
        survey = kwargs.pop('survey')
        super(SurveyForm, self).__init__(*args, **kwargs)

        for question in survey.question.all():
            choices = [(answer.name, answer.name) for answer in question.answer.all()]
            choices.append(('', 'Выберите ответ из списка'))
            self.fields[question.name] = (
                forms.ChoiceField(label=question.name, choices=choices,
                                  widget=forms.Select(
                                      attrs={
                                          'class': 'form-control border-8 mb-4 py-3 px-5 border-0 fs_24 SelfStorage__bg_lightgrey'
                                      })))
