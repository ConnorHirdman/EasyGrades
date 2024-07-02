import json

classInfo = json.load(open('Classes.JSON'))


def getPercent(maximum, value):
    x = (100/maximum)*value
    return x


def getWeight(weight, percent):
    x = round((weight/100)*percent, 2)
    return x


def progressBar(class_code, class_pass_mark, class_current_grade):
    progress = "    ----"+str(class_code)+"----\n["
    for count in range(20):
        if count <= round((20 / class_pass_mark) * class_current_grade):
            progress += chr(0x2588)
        else:
            progress += "."
    progress += "] Progress till Pass."
    return progress


for i in classInfo:
    code = i["Code"]
    pass_mark = i["Pass_Mark"]
    current_grade = 0
    completed = 0
    for j in i["Summative"]:
        current_grade += getWeight(j["Weight"], getPercent(j["Max"], j["Grade"]))
        completed += j["Weight"]

    if current_grade < pass_mark:
        need = round(pass_mark - current_grade, 2)
        remaining = 100 - completed

        if need > remaining:
            print("\nSorry you can no longer pass this course from the remaining", remaining, "%.")
            print("Your Maximum Grade is", current_grade + remaining, "%. The pass mark is", i["Pass_Mark"], "%.")

        else:
            print("\n"+progressBar(code, pass_mark, current_grade))
            print("You have so far got", current_grade, "% out of", completed, "%.")
            print("You still need", need, "% from the remaining", remaining, "% in order to pass", code, ".")

    elif completed < 100:
        print("\nCongrats, you have already passed", code, "with", current_grade, "% out of", completed, "%")


