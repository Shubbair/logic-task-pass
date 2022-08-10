'''
  Hussain Salih Mahdi
'''

#------------------------------------------------------

# Solution of Q1
def remove_given_char(string,char):
    return string.replace(char,'')

print(remove_given_char('Helxlo World!','x'))

#------------------------------------------------------

# Solution of Q2
def find_prime(num):
    primes = []
    if num > 1:
        for i in range(2,num):
            if num % i == 0:
                primes.append(i)
    return primes
    
print(find_prime(15))

#-------------------------------------------------------

# Solution of Q3
def char_count(string,char):
    return string.count(char)

print(char_count('Hello World!','l'))

#------------------------------------------------------

# Thanks for watching!