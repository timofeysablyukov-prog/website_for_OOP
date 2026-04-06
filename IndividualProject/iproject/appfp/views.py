from django.shortcuts import render, redirect
from .forms import Form

def index(request):
    return render(request, 'appfp/index.html')

def page1(request):
    error = ''
    form = Form()
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            field = request.POST.get('field')
            try:
                exec(field)
            except Exception:
                error = 'Ошибка в коде'
            else:
                if "def" in field and ':' in field and "return" in field:
                    try:
                        exec(field + "\n" + f"def checking(x):\n    if x == None:\n        raise TypeError()\nchecking({field.splitlines()[-1]})")
                    except Exception:
                        error = 'Ошибка при вызове функции: скорее всего функция ничего не выводит. Если ваша функция не предусматривает вывод тогда выведите 1(return 1). Также возможно вы забыли вызвать функцию.'
                    else:
                        error = 'Отличная работа!'
                else:
                    error = 'Вы не написали пользовательскую функцию'

    data = {'error': error, 'form': form}
    return render(request, 'appfp/page1.html', data)

def page2(request):
    error = ''
    form = Form()
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            field = request.POST.get('field')
            try:
                exec(field)
            except Exception:
                error = "Ошибка в коде"
            else:
                if "class" in field and ':' in field and "def" in field:
                    error = 'Отличная работа!'
                else:
                    error = 'Что-то не так'
    data1 = {'error': error, 'form': form}
    return render(request, 'appfp/page2.html', data1)

def page3(request):
    return render(request, 'appfp/page3.html')

def page4(request):
    error = ''
    form = Form()
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            field = request.POST.get('field')
            try:
                exec(field)
            except Exception:
                error = "Ошибка в коде"
            else:
                if "class" in field.splitlines()[0] and '_' in field.splitlines()[2] and ":" in field:
                    error = 'Отличная работа!'
                else:
                    error = 'Что-то не так'
    data2 = {'error': error, 'form': form}
    return render(request, 'appfp/page4.html', data2)

def page5(request):
    error = "error"
    form = Form()
    if request.method == "POST":
        form = Form(request.POST)
        if form.is_valid():
            field = request.POST.get('field')
            try:
                exec(field)
            except Exception as e:
                error = f"Ошибка в коде: {e}"
            else:
                lines = field.splitlines()
                classes = []
                for i, line in enumerate(lines):
                    stripped_line = line.strip()
                    if stripped_line.startswith("class"):
                        classes.append(i)
                if len(classes) != 2:
                    error = 'Должно быть ровно два класса: родительский и дочерний'
                else:
                    parent_class = lines[classes[0]:classes[1]]
                    child_class = lines[classes[1]:]
                    class_parent = any("class" and ":" in line for line in parent_class)
                    has_def_parent = any("def" in line for line in parent_class)
                    class_child = any("class" and ":" in line for line in child_class)
                    has_def_child = any("def" in line for line in child_class)
                    has_super_child = any("super()" in line for line in child_class)
            if class_parent and has_def_parent and class_child and has_def_child and has_super_child:
                error = "Отличная работа!"
            else:
                error = 'Вы не выполнили задание. Перечитайте и попробуйте ещё.'

    data3 = {'error': error, 'form': form}
    return render(request, 'appfp/page5.html', data3)

def page6(request):
    return render(request, 'appfp/page6.html')