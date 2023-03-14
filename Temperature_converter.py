t= float(input("Enter temperature:"))
scl1, scl2=[str(x) for x in input("Enter original scale and converted scale(A->B):").split("->")]
Scale_dictionary = {
        "K":"Kelvin", 
        "C":"Celsius", 
        "F":"Fahrenheit",
        "R":"Rankine", 
        "D":"Delisle", 
        "N":"Newton", 
        "Re":"Rèaumur", 
        "Ro":"Rømer"
        }
def temperature_converter(t:float, scl1:str, scl2:str) -> str:
    if scl1 == 'F':
        t= (t-32)*5/9
    elif scl1 == 'K':
        t= t-273.15
    elif scl1 == 'R':
        t= (t-419.67)*5/9
    elif scl1 == 'D':
        t= 100 - t*2/3
    elif scl1 == 'N':
        t= t*100/33
    elif scl1 == 'Re':
        t= t*5/4
    elif scl1 == 'Ro':
        t= (t-7.5)*40/21
    elif scl1 == 'C':
        t= t
    else:
        return(print("Invalid Scale1 Input")) 
    if scl2 == 'F':
        t= t*9/5 + 32
    elif scl2 == 'K':
        t= t + 273.15
    elif scl2 == 'R':
         t= t*9/5 + 419.67
    elif scl2 == 'D':
        t= 3/2*(- t + 100)
    elif scl2 == 'N':
        t= t*33/100
    elif scl2 == 'Re':
        t= t*4/5
    elif scl2 == 'Ro':
        t= t*21/40 + 7.5
    elif scl2 == 'C': 
        t= t
    else:
        return(print("Invalid Scale2 Input")) 
    return print(str(t)+" "+Scale_dictionary[scl2])                   #return statement breaks the function out 

temperature_converter(t,scl1,scl2)

Scale_list = ["K", "C","F","R","D","N","Re","Ro"]
for index in range(len(Scale_list)):
    if Scale_list[index] != scl2:
        temperature_converter(t,scl1,Scale_list[index])
         


""""
if __name__  == '__main__':
    print ('I am the main program')
else:
    print ('I am being imported')"""