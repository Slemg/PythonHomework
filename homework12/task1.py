def restaurant():
    time = input('Здравствуйте! На какое время хотите забронировать столик? ')
    guests = int(input('Сколько будет людей?: '))
    number = int(input("Номер столика? "))
    guests_list = []
    visitors_pizza_name = []
    visitors_pizza_size = []
    for i in range(guests):
        a = f'гость номер {i+1}'
        guests_list.append(a)
    for i in guests_list:
        pizza_type = input(f'Какую пиццу будет {i}?: ')
        pizza_size = int(input(f'Длина пиццы {pizza_type} в сантиметрах?: '))
        visitors_pizza_name.append(pizza_type)
        visitors_pizza_size.append(pizza_size)
    print('Всё верно?\n')
    i = -1
    print(f'Ожидаем вас в {time}')
    print(f'За столиком номер {number}')
    print(f'На {len(guests_list)} места/о')
    while i <= len(guests_list):
        if i+1 == len(guests_list):
            break
        i += 1
        print(f'{guests_list[i].capitalize()} Заказал пиццу {visitors_pizza_name[i]} размером {visitors_pizza_size[i]}')
        


restaurant()