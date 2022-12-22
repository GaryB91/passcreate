from passlib.hash import sha512_crypt
import getpass

 

x = getpass.getpass(prompt='Password for hashing: ')
y = getpass.getpass(prompt='Password for hashing again: ')

 

if x != y:
    print("passwords dont match...try again")
    exit()

 

hash = sha512_crypt.using(rounds=100000).hash(y)
print(hash)