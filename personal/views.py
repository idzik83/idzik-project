from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class PersonalView(TemplateView):
	template_name = "my_cv.html"
		