from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login , logout
from django.contrib import messages
from .forms import SignUpForm, AddRecordForm
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




def customer_person(request, pk):
	if request.user.is_authenticated:
		customer_person = Person.objects.get(id=pk)
		return render(request, 'record.html', {'customer_person': customer_person })
	else:
		messages.success(request,"you must logged in to view that page ...!")
		return redirect('home')

def delete_customer(request, pk):
	if request.user.is_authenticated:
		delete_it = Person.objects.get(id=pk)
		delete_it.delete()
		messages.success(request,"Record deleted successsfully")
		return redirect('home')
	else: 
		messages.success(request,"You lust be logged in that ...")
		return redirect('home')


def Add_Record(request):
	form = AddRecordForm(request.POST or None)
	if  request.user.is_authenticated:
		if request.method  == "POST" :
			if form.is_valid():
				Add_Record =form.save()
				messages.success(request,'Record Add')
				return redirect('home')
		return render(request, 'add_record.html', {'form':form})
	else:
		messages.success(request,"You must be logged in ")
		return redirect('home')


def update_record(request, pk):
	if request.user.is_authenticated:
		current_person = Person.objects.get(id=pk)
		form = AddRecordForm(request.POST or None, instance = current_person)
		if form.is_valid():
			form.save()
			messages.success(request,"record has been updated ")
			return redirect('home')
		return render(request, 'update_record.html', {'form':form})
	else:
		messages.success(request,"You must be logged in  ")
		return redirect('home')

