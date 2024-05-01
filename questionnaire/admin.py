from django.contrib import admin

from .models import Answer, Profile, Question, Survey, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    pass


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    pass


@admin.register(Survey)
class SurveyAdmin(admin.ModelAdmin):
    pass


@admin.register(Question)
class SurveyAdmin(admin.ModelAdmin):
    pass


@admin.register(Answer)
class SurveyAdmin(admin.ModelAdmin):
    pass
