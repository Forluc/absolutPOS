from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from questionnaire import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('create_company', views.create_company, name='create_company'),
    path('company_response/<int:survey_id>', views.company_response, name='company_response'),
    path('questionnaire', views.questionnaire, name='questionnaire'),
    path('questions', views.questions, name='questions'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
