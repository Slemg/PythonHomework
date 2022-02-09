language = {
    "aleksey":"python",
    "ilya":"c++",
    "xlebich":"js",
    "vanya":"python(crutoy)",
    "nikiton":"php",
    }
participants = {
    "aleksey",
    "ilya",
    "xlebich",
    "vanya",
    "nikiton",
    "artem"
}
for key in participants:
    if key in language:
            print(f"{key} спасибо за участие! ")
    else:
        print(f"{key} пройдите опрос!")


