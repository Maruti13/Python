def ChkChar(ch):
    
    if(ch == 'A' or ch == 'a' or ch == 'E' or ch == 'e' or ch == 'I' or ch == 'i' or ch == 'O' or ch == 'o' or ch == 'U' or ch == 'u'):
        return True
    
    else:
        return False

def main():

    Value = input("Enter the character : ")
    bRet = False

    bRet = ChkChar(Value)

    if(bRet == True):
        print(Value,"is a Vowel")
    
    else:
        print(Value,"is a Consonant")

if __name__ == "__main__":
    main()