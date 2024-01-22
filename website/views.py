from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .forms import SignUpForm
from .models import Person

def home(request):
	persons = Person.objects.all()

	#check  to see if logging in 
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		#autenticate
		user = authenticate(request, username = username, password= password)
		if user is not None:
			login(request,user)
			messages.success(request,"you have been loged in")
			return redirect('home')
		else : 
			messages.success(request, "there was an error logging, please try again")
			return redirect('home')
	
	else:
		return render(request, 'home.html', {'persons': persons})

'''#def login(request):
	pass
'''
def logout_user(request):
	logout(request)
	messages.success(request, "you have been loged out!")
	return redirect('home')

def register(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			form.save()
			# Authenticate and login
			username = form.cleaned_data['username']
			password = form.cleaned_data['password1']
			user = authenticate(username= username, password=password)
			login(request,user)
			messages.success(request,"you have successsfully login")
			return redirect('home')
	else:
		form = SignUpForm ()
		return render(request, 'register.html', {'form': form})	

	return render(request, 'register.html', {'form': form})			