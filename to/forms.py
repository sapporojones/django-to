from django import forms

class AddItemForm(forms.Form):
	category = [
	("TODO", "Do"),
	("TODL", "DL"),
	("TBUY", "Buy"),
	]
	name = forms.CharField(max_length=200, label="Task or Item Name ")
	url = forms.CharField(max_length=200, label="Task or Item URL ")
	choice = forms.ChoiceField(choices=category, label="Category ")