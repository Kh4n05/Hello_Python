"""def fibonacci (n:int) -> int:
    if n < 2:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)
n = int(input("Enter n: "))
print (fibonacci(n))

def C(n:int, k: int) -> int:
    if k > n:
        print ("Error: k > n")
    elif k == 0 or k == n:
        return 1
    return C(n-1, k) + C(n-1, k-1)
n, k = [int(x) for x in input("Enter n,k in nCk: ").split(",")]
print (C(n, k))

def sum (n: int) -> int:
    return (( n + sum (n-1)) if n > 1 else 1)
print (sum(6))
    
def toBinary(x: int) -> str:
    if x > 1:
        return toBinary(x // 2) + str(x % 2)
    return str(x % 2)
x = int(input ("Enter number in base10: "))
print(toBinary(x))"""

"""def toHex(x: int) -> str:
    letter_list = {
        10: "A",
        11: "B",
        12: "C",
        13: "D",
        14: "E",
        15: "F"
    }
    
    if x < 15:
        if 0 <= x < 10:
            return  str(x%16)
        return str(letter_list.get(x%16))
    else:
        if 0 <= x%16 < 10:
            return toHex(x//16) + str(x%16)
        return toHex(x//16) + str(letter_list.get(x%16))


x = int(input("Enter base10 number: "))
print (toHex(x))"""
"""
from math import sqrt
def isPrime (x: int, i = 2 ) -> bool:
    if x == 0 or x == 1:
        return False
    if x%i == 0:
        return False
    if i**2 > x:
        return True
    return isPrime(x, i +1)

x = int(input("Enter number: "))
print(isPrime(x))"""

"""def five_steps_Pattern (n: int) -> str :

    if n <= 0: 
        return str(n) 
    return str(n) + "," + str(five_steps_Pattern(n-5)) + "," + str(n)
          
n = int(input("Enter number: "))
print(five_steps_Pattern(n))"""

'''def Recaman(n: int) -> int:
   arr = [0]*n
   print (arr)
   for i in range (1,n):
      recur_term = arr[i-1] - i
      for j in range (0, i):
         if arr[j] == recur_term or recur_term < 0:
            recur_term = arr[i-1] + i
            break
         arr[i] = recur_term
         return print(arr[i], end=", ")        

n = int(input("Enter number: "))
print (Recaman(n))'''

def Recaman (n: int, list = [0]) -> list:
    if n == 0:
        return list
    recur_term = Recaman(n-1)[-1] - n
    if recur_term > 0 and recur_term not in list:
        list.append(recur_term)
    else:
        list.append(recur_term + 2*n)
    return list
print (Recaman(100))

#Recaman(0) = 0
#Recaman(n) = Recaman (n-1) - n if Recaman (n-1) - n > 0 or Recaman(n-1) - n != Recamn_List[]
# Else: Recaman(n) = Recaman (n-1) + n