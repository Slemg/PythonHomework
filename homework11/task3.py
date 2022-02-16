music_album1= {}
def infinite_information(name):
    info = f"{name}"
    return info

while True:
    print("Если тебе надоели,введи out")    
    n = input("Исполнитель?")
    if n == "out":
        break
    s = input("Альбом?")
    music_album1[f"{n}"]=f"{s}"
    y = infinite_information(music_album1)
    print(y)