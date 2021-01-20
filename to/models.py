from django.db import models

# Create your models here.



class MasterList(models.Model):
	TODO = 'TO-DO'
	TODL = 'TO-DL'
	TBUY = 'TOBUY'
	category = [
	('TODO', 'Do'),
	('TODL', 'DL'),
	('TBUY', 'Buy'),
	]
	name = models.CharField(max_length=250)
	url = models.CharField(max_length=250)
	category = models.CharField(
		max_length=4, 
		choices=category,
		default=TBUY
		)