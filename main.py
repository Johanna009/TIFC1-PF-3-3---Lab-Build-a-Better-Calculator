def main():
  print("Hello learners!")

if __name__=="__main__":
  main()

  def addmultiplenumbers(numbers): 
     return sum(numbers)
  
resultado = (addmultiplenumbers([10, 20, 5]))
print(resultado)  

def multiplymultiplenumbers(numbers):
    resultado = 1
    for n in numbers:
        resultado *= n
    return resultado
print(multiplymultiplenumbers([10,9,8]))

def isItEven(num):
    return num % 5 == 0
print(isItEven(10))  # True
print(isItEven(22))  # False
print(isItEven(40))  # True

def isItAnInteger(num):
    try:
        int(num)
        return True
    except ValueError:
        return False

print(isItAnInteger("5"))     # True
print(isItAnInteger("5.5"))   # False
print(isItAnInteger(8))       # True


