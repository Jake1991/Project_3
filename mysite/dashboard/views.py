from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from questions.models import DayScore
# Create your views here.

def dashboard(request):
	user = User.objects.get(username=request.user)
	dayscores = DayScore.objects.filter(user=user)
	dates = [(str(dayscore.date), dayscore.score) for dayscore in dayscores]
	context = {}
	context['dates'] = dates
	context['question_url'] = reverse('simple_question')
	return render(request, 'dashboard.html', context=context)