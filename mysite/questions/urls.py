from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'hello', views.question),
	url(r'verify', views.solution),
	url(r'input', views.input_question),
]