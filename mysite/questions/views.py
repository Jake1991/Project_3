from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from questions.utils import generate_problem, check_solution
from questions.forms import QuestionForm, InputQuestionForm
from questions.models import UserSession, DayScore, SimpleQuestion


import datetime
# Create your views here.

@login_required
def question(request):
	problem_data = generate_problem('simple_question')
	problem = problem_data.get('problem_1').get('data').get('problem')
	solutions = problem_data.get('problem_1').get('data').get('solutions')
	form = QuestionForm(problem, solutions[0], solutions[1], solutions[2])
	context = {	'problem': problem,
				'solutions': solutions,
				'forms': [(problem, form)]}
	return render(request, 'questions.html', context=context)
import datetime

from django import forms
from django.forms import formset_factory
@login_required
def multi_stage_question(request):
	#multi stage solutions not currently randomised
	problem_data = generate_problem('multi_stage_question')
	forms = []
	
	for index, problem in enumerate(problem_data.get('problems')):
		problem_text = problem.get('problem_{0}'.format(index)).get('data').get('problem')
		solutions = problem.get('problem_{0}'.format(index)).get('data').get('solutions')
		# import pdb; pdb.set_trace()
		forms.append((problem_text, QuestionForm(problem_text, solutions[0], solutions[1], solutions[2])))
	context = { 'problem': 'Placeholder Problem Title',
				'forms': forms,}
	######
	QuestionFormSet = formset_factory(QuestionForm, extra=2)
	formset = QuestionFormSet(initial=[
    	{'problem': 'Jake',
    	'answers': 'hello',}
	])
	context = { 'problem': 'Placeholder Problem Title',
				'formset': formset,}	
	return render(request, 'questions.html', context=context)

@login_required
def solution(request):
	correct = check_solution(request.POST.get('problem'), request.POST.get('answers'))
	user = get_user(request)
	update_score(user, correct)
	context = {'correct' : correct, 'score': get_score(user)}
	return render(request, 'verify.html', context=context)

def get_user(request):
	return User.objects.get(username=request.user)

def get_score(user):
	day_score = DayScore.objects.get_or_create(user=user, date=datetime.date.today())[0]
	return day_score.score

def update_score(user, is_correct):
	if is_correct:
		dayscore = DayScore.objects.get_or_create(user=user, date=datetime.date.today())[0]
		dayscore.score += 1
		dayscore.save()

def input_question(request):
	if request.method == 'POST':
		data = request.POST
		SimpleQuestion.objects.create(
			question_text=data['question_text'],
			answer=data['answer'],
			dummy_answer_a=data['dummy_answer_a'],
			dummy_answer_b=data['dummy_answer_b'],
			)
		question_created = True

	else:
		question_created = False
	form = InputQuestionForm()
	return render(request, 'input.html', {'form': form, 'question_created': question_created})