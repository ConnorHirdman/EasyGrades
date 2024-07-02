import json

classInfo = json.load(open('Classes.JSON'))


def getPercent(maximum, value):
    x = (100/maximum)*value
    return x


def getWeight(weight, percent):
    x = round((weight/100)*percent, 2)
    return x


for i in classInfo:
    code = i["Code"]
    currentGrade = 0
    completed = 0
    for j in i["Summative"]:
        currentGrade += getWeight(j["Weight"], getPercent(j["Max"], j["Grade"]))
        completed += j["Weight"]

    if currentGrade < i["Pass_Mark"]:
        need = round(i["Pass_Mark"] - currentGrade, 2)
        remaining = 100 - completed

        if need > remaining:
            print("\nSorry you can no longer pass this course from the remaining", remaining, "%.")
            print("Your Maximum Grade is", currentGrade + remaining, "%. The pass mark is", i["Pass_Mark"], "%.")

        else:
            print("\nYou still need", need, "% from the remaining", remaining, "% in order to pass", code, ".")

    elif completed < 100:
        print("\nCongrats, you have already passed", code, "with", currentGrade, "% out of", completed, "%")


