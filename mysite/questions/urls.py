from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'simple_question', views.question, name='simple_question'),
	url(r'multi_stage_question', views.multi_stage_question, name='multi_question'),
	url(r'verify', views.solution),
	url(r'input', views.input_question),
]