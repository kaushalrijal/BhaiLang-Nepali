import sys

def interprete(filepath):
    output = "" 
    code = open(filepath)
    for i in code:
        if 'bhan bhai' in i:
            output+=(i.replace("bhan bhai", "print"))
        elif 'yo ho bhai' in i:
            output +=(i.replace("yo ho bhai ", ""))
        elif 'haal bhai' in i:
            output +=(i.replace("haal bhai", "input"))
        else:
            output += i
    code.close

    try:
        exec(output)
    except:
        print("ke garya bhai, ke garyaaa? error bhayo ta")

args = sys.argv

if len(args) == 1:
    print("Welcome to Bhailang Nepali version 1.0.0 by Kaushal Rijal")
    print("Enter the filename or filepath to run the code")

    filepath = input(">>>    ")
    interprete(filepath=filepath)

elif len(args)==2:
    interprete(filepath=args[1])

else:
    print("ERROR: The number of arguments passed were more than required")

input("\nPress enter to exit: ")
