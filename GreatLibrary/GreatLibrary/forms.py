from django import forms

class SearchForm(forms.Form):
	content = forms.CharField()
	def __str__(self):
		return self.content