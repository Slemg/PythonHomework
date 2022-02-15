def make_shirt(size,text):
    mess = f"Размер футболки {size}. Текст на футболке: {text}."
    return mess
size = input('Размер футболки?(S/M/L) ---> ')
text = input('Текст на футболке? ---> ')
y = make_shirt(size,text)
print(y)

