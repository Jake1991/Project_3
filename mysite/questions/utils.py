from random import choice, shuffle
import copy

from .models import SimpleQuestion, MultiStageQuestion

def generate_problem(problem_type=None):
	if problem_type == 'simple_question':
		question_query = SimpleQuestion.objects.order_by('?').first()
		question = question_query.question_text
		solutions = question_query.get_solutions()
		problem_data = {	'problem_1': {
						 	'data': {	'problem': question, 
						 				'solutions': solutions}}}
	elif problem_type == 'multi_stage_question':
		question_query = MultiStageQuestion.objects.order_by('?').first()
		problem_data = {}
		problem_data['problems'] = []
		problem_data['intertext'] = []
		intertext_list = []
		for index, problem in enumerate(question_query.get_subquestions()):
			problem_data['problems'].append({ 'problem_{0}'.format(str(index)): { 'data':
				 { 	'problem' : problem.question_text, 
							'solutions': problem.get_solutions }}
			})
		problem_data['intertext'].append(question_query.get_intertext())
	return problem_data


def check_solution(problem, subbed_solution, problem_type=None):

	solution = SimpleQuestion.objects.get(question_text=problem).answer

	if subbed_solution == solution:
		return True
	else:
		return False

def ask_for_solution():
	print("Enter 1,2,3 for solution")
	user_solution = input("Enter solution:")
	return user_solution

def give_problem(problem, solutions):
	print("hello")
	print("")
	print(problem)
	print("")
	solution_labels = list(range(1,len(solutions)+1))
	stored_solutions = copy.copy(solutions)
	for label in solution_labels:
		this_solution = random.choice(solutions)
		solutions.remove(this_solution)
		#Correct solution is always first in list
		print (stored_solutions)
		if this_solution == stored_solutions[0]:
			solution_index = label
		label = str(label) + ". " + this_solution
		print(label)
	return solution_index

