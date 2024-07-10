#prime number checker

def prime_checker(num):
      is_prime = True
      for i in range(2,num):
           if num % i == 0:
                is_prime = False
      if is_prime :
           print("It is a prime numnber")
      else :
           print("It is not a prime number ")

prime_checker(7)