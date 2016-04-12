from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

from questions.utils import generate_problem, check_solution
from questions.forms import QuestionForm, MultiStageQuestionForm, InputQuestionForm
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
				'image_path': problem_data.get('problem_1').get('data').get('image_path'),
				'solutions': solutions,
				'forms': [(problem, form)]}
	return render(request, 'questions.html', context=context)
import datetime

from django import forms
from django.forms import formset_factory
@login_required
def multi_stage_question(request, stage=None):
	#multi stage solutions not currently randomised
	#{'problems': [{'problem_0': {'data': {'solutions': ['2', '3', '4'], 'problem': '1+1 ='}}},
	#			   {'problem_1': {'data': {'solutions': ['4', '5', '6'], 'problem': '2+2 = '}}},
	#			   {'problem_2': {'data': {'solutions': ['6', '7', '8'], 'problem': '3 + 3 = '}}}],
	#'intertext': [['Some text here', 'Some text there', '', '']]}
	if stage:
		stage = int(stage) + 1
		#import pdb; pdb.set_trace()
	else:
		stage=0
	problem_data = generate_problem('multi_stage_question')
	problem = problem_data.get('problems')[stage].get('problem_{}'.format(stage)).get('data').get('problem')
	solutions = problem_data.get('problems')[stage].get('problem_{}'.format(stage)).get('data').get('solutions')
	if stage == len(problem_data.get('problems'))-1:
		stage = 'final'
	form = MultiStageQuestionForm(
		problem,
		solutions[0],
		solutions[1],
		solutions[2],
		stage,
		problem_data['question_id'])
	context = {	'problem': problem,
				'solutions': solutions,
				'forms': [(problem, form)]}
	return render(request, 'questions.html', context=context)

@login_required
def solution(request):
	correct = check_solution(request.POST.get('problem'), request.POST.get('answers'))
	user = get_user(request)
	update_score(user, correct)
	context = {'correct' : correct, 'score': get_score(user)}
	if request.POST.get('stage') and request.POST.get('stage') != 'final':
		return multi_stage_question(request, request.POST.get('stage'))
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