def isVowel(str):
    if(str.isalpha()):
        if(str in "aeiou"):
            print("Vowel")
        else:
            print("consonent")
    else:
        print("not an alphabet")
a=input("Enter string:")
isVowel(a)