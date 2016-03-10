from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from questions.models import DayScore
# Create your views here.

def dashboard(request):
	user = User.objects.get(username=request.user)
	# need to figure out how to get multiple objects, for now using test data
	#dayscores = DayScore.objects.get(user=user)
	test = {
		('2016, 03, 01', 2),
		('2016, 03, 02', 10),
		('2016, 03, 03', 0),
		('2016, 03, 04', 5),
	}
	context = {}
	context['dates'] = test
	context['question_url'] = reverse('simple_question')
	return render(request, 'dashboard.html', context=context)