from django.db import models
import datetime
from django.contrib.auth.models import User

class UserSession(models.Model):
	user_id = models.IntegerField(default=0)
	score = models.IntegerField(default=0)
	last_updated = models.DateField(default=datetime.date(2015,1,1))

class DayScore(models.Model):
	user = models.ForeignKey(User)
	date = models.DateField(default=datetime.date.today())
	score = models.IntegerField(default=0)

class SimpleQuestion(models.Model):
	def __str__(self):
		return self.question_text
	question_text = models.TextField()
	answer = models.CharField(max_length=100)
	dummy_answer_a = models.CharField(max_length=100)
	dummy_answer_b = models.CharField(max_length=100)
	
	def get_solutions(self):
		return [self.answer, self.dummy_answer_a, self.dummy_answer_b]


class MultiStageQuestion(models.Model):
	'''
	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	part_one = GenericForeignKey('content_type', 'object_id')
	'''
    #NEEDS A TITLE FIELD, some 'callsign', a quick unique human-readable identifier

	part_1 = models.ManyToManyField(SimpleQuestion, default=None, related_name='part_1', blank=True)
	InterText1 = models.TextField(default='', blank=True)
	part_2 = models.ManyToManyField(SimpleQuestion, default=None, related_name='part_2', blank=True)
	InterText2 = models.TextField(default='', blank=True)
	part_3 = models.ManyToManyField(SimpleQuestion, default=None, related_name='part_3', blank=True)
	InterText3 = models.TextField(default='', blank=True)	
	part_4 = models.ManyToManyField(SimpleQuestion, default=None, related_name='part_4', blank=True)
	InterText4 = models.TextField(default='', blank=True)
	part_5 = models.ManyToManyField(SimpleQuestion, default=None, related_name='part_5', blank=True)

	def get_subquestions(self):
		return [self.part_1, self.part_2, self.part_3, self.part_4, self.part_5]

	def get_intertext(self):
		return [self.InterText1, self.InterText2, self.InterText3, self.InterText4]




