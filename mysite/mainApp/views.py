from django.shortcuts import render


def index(request):
    return render(request, 'mainApp/homePage.html')

def contact(request):
    return render(request, 'mainApp/basic.html', {'values': ['Если у вас остались вопросы, то задавайте их мне по телефону', '(+7775) 303 57 77', 'bekzat-dulat@mail.ru']})
