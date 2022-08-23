import random
def prime_finder(n):
  # Write your code here
  prime_list = []
  # Exclude 0 and 1 for our list
  for x in range(1, n):
    if x == 1 or x == 0:
      continue
  # Check if the number is prime
    else:
      for y in range(2, int(x/2)+1):
        if x % y == 0:
          break
      else:
  #Add the number if it is prime     
        prime_list.append(x)
  #Return the list      
  return prime_list
  #Generate a random number
n = random.randint(0, 1000)
  #Print the list with the prime numbers
print(prime_finder(n+1))
