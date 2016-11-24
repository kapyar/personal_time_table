from django.http import HttpResponse

import random

def hellow_world(request):
	return HttpResponse("Hello world")