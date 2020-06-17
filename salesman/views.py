from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.http import HttpResponseRedirect
from django.shortcuts import render
from salesman.forms import UserRegisterForm, UploadFileForm
from django.shortcuts import redirect
from salesman.models import Files
from django.views.generic.list import ListView
import datetime
from background_task import background
from subprocess import PIPE, STDOUT, Popen
import subprocess

path = ""


def index(request):
    if request.user.is_authenticated:
        ifiles = Files.objects.filter(user=request.user)
        context = {
            'Files': ifiles
        }
        return render(request, 'salesman/index.html', context)
    else:
        return render(request, 'salesman/index.html')


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()

            new_user = authenticate(username=form.cleaned_data['username'],
                                    password=form.cleaned_data['password1'],
                                    )
            login(request, new_user)

            username = form.cleaned_data.get('username')

            messages.success(request, f'Account {username} created succesfully')

            return HttpResponseRedirect('/')
        else:
            messages.warning(request, f"Check data, account not created")
    else:
        form = UserRegisterForm()
        print('blad')

    return render(request, 'salesman/register.html', {'form': form})


def test(request):
    return render(request, 'salesman/templatetest.html')


def new_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():

            f = form.save(commit=False)
            f.user = request.user
            f.date_uploaded = datetime.datetime.now()
            f.save()
            current_id = f.id
            print(current_id)

            file = Files.objects.get(id=current_id).get_dir()

            background(file, current_id)

            #subprocess.run(["python","manage.py","process_tasks"])

            return redirect('index')
    else:
        print("nie")
        form = UploadFileForm()

    return render(request, 'salesman/new.html', {'form': form})


@background(schedule=1)
def background(file, curr_id):
    print("start f")
    p = Popen("python salesman/simulation.py " + file, stdout=PIPE, stderr=STDOUT, shell=True)
    line = p.stdout.readline().decode('utf-8')
    print(line[:-2])
    Files.objects.filter(id=curr_id).update(finished=True, result=line[:-2])



class ComputeListView(ListView):
    model = Files
    template_name = 'salesman/index.html'
    context_object_name = 'list'
    ordering = ['-date_uploaded']

    def get_queryset(self):
        return Files.objects.filter(user=self.request.user)
