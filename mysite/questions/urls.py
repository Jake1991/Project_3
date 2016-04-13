from django.conf.urls import url

from . import views

urlpatterns = [
	#TODO id should be number not word
	url(r'simple_question/(?P<q_id>[-\w]+)/', views.question),
	url(r'simple_question/', views.question, name='simple_question'),
	url(r'multi_stage_question', views.multi_stage_question, name='multi_question'),
	url(r'verify', views.solution),
	url(r'input', views.input_question),
]