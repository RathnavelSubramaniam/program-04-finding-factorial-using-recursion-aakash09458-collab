def factorial (n) :
    if n==0 or n==1:
        return 1
    else:
          return n*factorial(n-1)
 number=int(input("entera number":))
 if number<0:
    print("\n Erro:Factorial is not defined for negative numbers.")
 else:
     result=factorial(number)
     print(f"\n the factorial of {number} is {result}")
