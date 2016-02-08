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
	def __unicode__(self):
		return self.question_text
	question_text = models.TextField()
	answer = models.CharField(max_length=100)
	dummy_answer_a = models.CharField(max_length=100)
	dummy_answer_b = models.CharField(max_length=100)


class MultiStageQuestion(models.Model):
	part_one = models.ManyToManyField(SimpleQuestion, default=None, related_name='part_one')
	part_two = models.ManyToManyField(SimpleQuestion, default=None, related_name='part_two')
	part_three = models.ManyToManyField(SimpleQuestion, default=None, related_name='part_thre')
	part_four = models.ManyToManyField(SimpleQuestion, default=None, related_name='part_four')
	part_five = models.ManyToManyField(SimpleQuestion, default=None, related_name='part_five')




