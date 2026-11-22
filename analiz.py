def analyze_scores(*scores): #принимаем сколько угодно баллов
    if not scores: #если баллы не передали
        return 0, 0, 0 #сразу возвращаем нули чтоб не делить на 0
    summa = sum(scores) #считаем сумму
    kolvo = len(scores) #считаем сколько всего оценок
    sredniy = summa / kolvo #находим среднее
    return summa, kolvo, sredniy #отдаем все 3 значения

def print_report(team_name, **info): #принимаем имя команды и остальные данные
    print(f"Команда: {team_name}") #выводим название
    for key, value in info.items(): #перебираем словарик с инфой
        print(f"{key}: {value}") #печатаем ключ и значение

print("Набор (8, 10, 7, 9):", analyze_scores(8, 10, 7, 9)) #проверка 1
print("Набор (5, 5):", analyze_scores(5, 5)) #проверка 2
print("Без аргументов:", analyze_scores()) #проверка когда пусто
print_report("Комета", coach="Иванов И.И.", city="Минск", league="Высшая") #вывод отчета




