def prime_factorization(n):
 pflist = []
 i = 2
 while i <= n:
   if n % i == 0:
     pflist.append(i)
     n /= i
   else:
     i+=1
 
 print(pflist)

num = int(input("Enter a number"))
prime_factorization(num)