from django.shortcuts import render
import datetime
# Create your views here.
def home(request):
    d = {'author' : 'Rahim', 'age' : 9, 'lst' : [1,2,3,4], 'strList' : ['python', 'is', 'best'],
         'date' : datetime.datetime.now(), 'courses' : [
        {
            'id' : 1,
            'name' : 'python',
            'fee' : 5000
        },
        {
            'id' : 2,
            'name' : 'django',
            'fee' : 9000
        },
        {
            'id' : 3,
            'name' : 'c++',
            'fee' : 2000
        }
    ]}
    return render(request, 'first_app/home.html', d)