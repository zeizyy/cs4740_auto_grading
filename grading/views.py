from django.shortcuts import render, HttpResponse, \
	render_to_response
import os
import subprocess
import random

# Create your views here.
def index(request):
	return HttpResponse('Welcome to the autograding system.')

def upload(request):
	if request.method == "POST":
		submission = request.FILES['homework']
		content = handle_uploaded_file(submission)
		# return HttpResponse(content)
		subprocess.call("rm -f ./a.out", shell=True) 
		retcode = subprocess.call("/usr/bin/g++ walk.cc", shell=True)
		if retcode:
			return HttpResponse("failed to compile walk.cc")
		name1 = str(random.random())
		name2 = str(random.random())
		correct = 0
		output = subprocess.check_output("echo "+name1+"'\n'"+name2+" | ./a.out", shell=True)
		output = str(output)
		if name1 in output:
			correct += 1
		if name2 in output:
			correct += 1
		return render_to_response('score.html',{'submission':content,\
			'correct':correct})
	return render_to_response('upload.html')

def handle_uploaded_file(f):
	content = []
	with open('walk.cc', 'wb+') as destination:
		for line in f:
			destination.write(line)
			content += [line.decode('utf-8')]
	return content
