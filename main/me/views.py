from django.shortcuts import render, render_to_response
from datetime import date

def main(request):
    main_info = {
        'name': 'Алексей',
        'lastname': 'Шаталин',
        'date': date(1989, 10, 26),
        'sity': 'Иркутск',
        'gender':'M'
    }
    main_hobby = {'Гитара','тренажерный зал','Кулинария'}
    return render_to_response("main.html", {'main_info': main_info, 'main_hobby': main_hobby})

def work(request):
    work = {'img':'stoika.jpg'}

    return render_to_response("work.html", work)


def study(request):
     learn = {
        'type':'univer',
        'univer': 'Иркутский Государственный Технический Университет',
        'faculty':'Кибернетики',
        'special':'ЭВМ'}
     return render_to_response("study.html", learn)