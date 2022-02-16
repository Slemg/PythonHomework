def make_album(name, surname, age) :
    r = f"Первая характеристика {name}\nВторая характеристика {surname}\nТретья характеристика {age}\n"
    return r

x = input("Исполнитель?")
y = input("Альбом?")
a = input("Исполнитель?")
b = input("Альбом?")
c = input("Исполнитель?")
d = input("Альбом?")
music_album1 = {}
music_album2 = {}
music_album3 = {}
music_album1[f"{x}"]=f"{y}"
music_album2[f"{a}"]=f"{b}"
music_album3[f"{c}"]=f"{d}"


result = make_album(music_album1, music_album2, music_album3)
print(result)
