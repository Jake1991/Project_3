from random import choice, shuffle
import copy

from .models import SimpleQuestion

multiple_choice = {
                     "Differentiate x^2": ["2x", "x", "3x"],
                     "Integrate x^2": ["x^3/3 + c", "2x", "pi"],
                     "Differentiate x^3/3": ["x^2", "x", "3x"]
                     }

def generate_problem(problem_type=None):
	'''if problem_type == "multiple_choice":
		problem = choice(list(multiple_choice))
		solutions = copy.deepcopy(multiple_choice[problem])
		shuffle(solutions)
		return problem, solutions'''

	question_query = SimpleQuestion.objects.order_by('?').first()
	question = question_query.question_text
	solutions = [
		question_query.answer,
		question_query.dummy_answer_a,
		question_query.dummy_answer_b,
		]
	return question, solutions

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

