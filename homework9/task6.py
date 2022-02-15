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
    "artem",
    "artem1",
    "artem2"
}
for key in participants:
    if key in language:
            print(f"{key} спасибо за участие! ")
    else:
        print(f"{key} пройдите опрос!")


