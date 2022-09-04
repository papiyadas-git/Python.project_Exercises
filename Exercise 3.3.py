gender = input("enter you gender: ")
Hemoglobin = float(input("please enter your hemoglobin value: "))
if gender == "female" or "Female" or "FEMALE":
    if 117 <= Hemoglobin <= 155:
        print("you have a normal hemoglobin level")
        print("a")
    if 117 > Hemoglobin:
        print("you have a low level of hemoglobin")
        Print("b")
    if 155 < Hemoglobin:
        print("you have a high level of hemoglobin")
        print("c")
elif gender == "male" or "Male" or "MALE":
    if 134<= Hemoglobin <=167:
        print("you have a normal hemoglobin level")
        print("d")
    if 134>Hemoglobin:
        print("you have a low level of hemoglobin")
        print("e")
    if 167<Hemoglobin:
        print("you have a high level of hemoglobin")
        print("f")
else:
    print("invalid input")
    print("g")