from .models import My_Blog
from django.forms import ModelForm


class ModelForm(ModelForm):
	class Meta:
		model = My_Blog
		fields = ['author','image','description']