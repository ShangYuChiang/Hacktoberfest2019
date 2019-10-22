Zero = ["  ***  ",
        " *   * ",
        "*     *",
        "*     *",
        "*     *",
        " *   * ",
        "  ***  "]
One = [" * ",
       "** ",
       " * ",
       " * ",
       " * ",
       " * ",
       "***"]

Two = [" *** ",
       "*   *",
       "*  * ",
       "  *  ",
       " *   ",
       "*    ",
       "*****"]

Three = [" *** ", "*   *", "    *", "  ** ", "    *", "*   *", " *** "]
Four = ["   *  ", "  **  ", " * *  ", "*  *  ", "******", "   *  ",
         "   *  "]
Five = ["*****", "*    ", "*    ", " *** ", "    *", "*   *", " *** "]
Six = [" *** ", "*    ", "*    ", "**** ", "*   *", "*   *", " *** "]
Seven = ["*****", "    *", "   * ", "  *  ", " *   ", "*    ", "*    "]
Eight = [" *** ", "*   *", "*   *", " *** ", "*   *", "*   *", " *** "]
Nine = [" ****", "*   *", "*   *", " ****", "    *", "    *", "    *"]
 

Digits = [Zero, One, Two, Three, Four, Five, Six, Seven, Eight, Nine]
while True:
    digits = input()
    if(int(digits)<10000000000 and int(digits)>=0):
        break
    print('Input error, please enter again!')
    
NeedStart = input("")
row = 0
while row < 7:
    line = ""
    column = 0
    while column < len(str(digits)):
        number = int(digits[column])
        digit =  Digits[number]
        if NeedStart == "Y":
            line += digit[row].replace('*' , str(number) ) + "  "
        elif NeedStart == "N":
            line += digit[row] + "  "
        else:
            line += digit[row] + "  "
        column += 1
    print(line)
    row += 1
