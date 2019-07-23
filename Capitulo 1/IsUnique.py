def is_unique(input):    
    characters=[False for i in range(128)]
    input=input.replace(" ","")
    for i in input:
        if(characters[ord(i)]==True):
            print(i)
            return "No"
        characters[ord(i)]=True
    return "Si"

input = "I am wonderful"
response=is_unique(input)
print(response)