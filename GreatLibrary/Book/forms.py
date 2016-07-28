from django import forms

class ReviewForm(forms.Form):
	content = forms.CharField(widget=forms.Textarea)
	def __str__(self):
		return self.content

class ShowReviewForm(forms.Form):
	content = forms.CharField()
	starnum = forms.IntegerField()
	username = forms.CharField()
	def __str__(self):
		return self.content