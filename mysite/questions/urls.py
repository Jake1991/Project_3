from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'simple_question', views.question),
	url(r'multi_stage_question', views.question),
	url(r'verify', views.solution),
	url(r'input', views.input_question),
]