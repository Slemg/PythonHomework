names = ['denis', 'artem', 'andrei']
message0 = f"Привет {names[0].title()},ты приглашен на обед"
message1 = f"Привет {names[1].title()},ты приглашен на обед"
message2 = f"Привет {names[2].title()},ты приглашен на обед"
print(message0)
print(message1)
print(message2)
print(f"{names[1].title()} не сможет прийти на обед")
names[1] = 'danil'
message0 = f"Привет {names[0].title()},ты приглашен на обед"
message1 = f"Привет {names[1].title()},ты приглашен на обед"
message2 = f"Привет {names[2].title()},ты приглашен на обед"
print(message0)
print(message1)
print(message2)