def is_unique(input):    
    suma=0
    for i in input.replace(" ",""):       
        for j in input.replace(" ",""):
            if(i==j):
                suma+=1
                if(suma>1):         
                   return "No"       
        suma=0   
    return  "Yes"

input = "This is a test string"
a=is_unique(input)
print(a)