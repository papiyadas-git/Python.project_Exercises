length = float(input("Enter the size of the caught Zander (cm): "))
if length<42:
    size_gap = str(42-length)
    print("Please release the zander back into the lake, it is " + size_gap + "cm below the size limit.")