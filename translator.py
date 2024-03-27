def translater(phrase):
    result=""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            if letter.isupper():
                result = result + "G"
            else:
                result = result + "g"
        else:
            result = result + letter
    return result

#  comments are fun
print(translater(input("Enter a phrase: ")))