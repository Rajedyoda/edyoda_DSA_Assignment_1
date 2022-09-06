
def FirstNonRepeat(string1):
 
    for index in string1:
 
        if (string1.find(index,(string1.find(index)+1))) == -1:
            print("First nonrepeating character is :",index)
            break
    else:
        print("Either all characters are repeating or string is empty")
    return
 
#__main__
 
string1 = input("Type String to check First NonRepeating Character is: ")
 
FirstNonRepeat(string1)


 