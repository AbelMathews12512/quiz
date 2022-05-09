from django.shortcuts import render

# Create your views here.
def index(request):
	return render(request, 'todo/home.html')
	
def question(request):
	return render(request, 'todo/question.html')
	
def result(request):
	res = request.POST['ABC']
	return render(request, 'todo/result.html', {'result':res})
	
def answer(request):
	return render(request, 'todo/answer.html')