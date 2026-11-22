def ticket_total(count, price=12): #функция цены без скидки, по умолчанию 12 руб
    return count * price #умножаем билеты на цену

def final_price(count, is_school_group=False): #функция итоговой цены
    total = ticket_total(count) #вызываем первую функцию чтоб не считать заново
    if is_school_group: #если группа школьная
        return total * 0.75 #делаем скидку 25 процентов
    return total #если обычная группа возвращаем полную цену

print(f"3 обычных билета: {final_price(3)} руб.") #вызов по умолчанию без скидки
print(f"4 билета (школьная группа): {final_price(4, is_school_group=True)} руб.") #вызов со скидкой
print(f"2 билета по 15 руб.: {ticket_total(2, price=15)} руб.") #меняем цену через именованный аргумент


