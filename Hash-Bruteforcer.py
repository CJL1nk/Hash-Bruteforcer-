import hashlib
import random
import secrets
import string
from time import sleep
import base64

### Modules
MenuInput = 0

def ModuleMenu():
   print("_______________________________________")
   print("Select Bruteforce Module")
   print("_______________________________________")
   sleep(0.10)
   print("\n [1] SHA1")
   sleep(0.10)
   print("\n [2] SHA224")
   sleep(0.10)
   print("\n [3] SHA256")
   sleep(0.10)
   print("\n [4] SHA384")
   sleep(0.10)
   print("\n [5] SHA512")
   sleep(0.10)
   print("\n [6] MD5")
   sleep(0.10)
   print("\n [7] Blake2b")
   sleep(0.10)
   print("\n [8] Blake2s")
   sleep(0.10)
   print("\n [9] Base16")
   sleep(0.10)
   print("\n [10] Base32")
   sleep(0.10)
   print("\n [11] Base64")
   sleep(0.10)
   print("\n [12] Base85")
   sleep(0.10)
   print("\n [0] Exit")
ModuleMenu()

MenuInput = input("\n Pick your module [>]:\t")
MenuInput = int(MenuInput)

def SHA1():                                                              #SHA1 Bruteforce Module

   encoded_password = input("Enter your SHA1 encrypted password:\t")

   charcount = input("\nAbout how many characters is your users password?:\t")
   charcount = int(charcount)
   charcount = (charcount + 1)

   encoded_string = 0

   while encoded_password != encoded_string:
      charrange = random.randrange(1,charcount)

      randstring = (''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(charrange)))

      result2 = hashlib.sha1(randstring.encode())

      encoded_string = (result2.hexdigest())

      if (encoded_password == encoded_string):
         print(input("\nThe retard's password is:\t" + randstring))
         break
      else:
         continue

def SHA224():                                                              #SHA224 Bruteforce Module                         

   encoded_password = input("Enter your SHA224 encrypted password:\t")

   charcount = input("\nAbout how many characters is your users password?\t")
   charcount = int(charcount)
   charcount = (charcount + 1)

   encoded_string = 0

   while encoded_password != encoded_string:
      charrange = random.randrange(1,charcount)

      randstring = (''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(charrange)))

      result2 = hashlib.sha224(randstring.encode())

      encoded_string = (result2.hexdigest())

      if (encoded_password == encoded_string):
         print(input("\nThe retard's password is:\t" + randstring))
         break
      else:
         continue

def SHA256():                                                              #SHA256 Bruteforce Module                         

   encoded_password = input("Enter your SHA256 encrypted password:\t")

   charcount = input("\nAbout how many characters is your users password?\t")
   charcount = int(charcount)
   charcount = (charcount + 1)

   encoded_string = 0

   while encoded_password != encoded_string:
      charrange = random.randrange(1,charcount)

      randstring = (''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(charrange)))

      result2 = hashlib.sha256(randstring.encode())

      encoded_string = (result2.hexdigest())

      if (encoded_password == encoded_string):
         print(input("\nThe retard's password is:\t" + randstring))
         break
      else:
         continue

def SHA384():                                                              #SHA384 Bruteforce Module                         

   encoded_password = input("Enter your SHA384 encrypted password:\t")

   charcount = input("\nAbout how many characters is your users password?\t")
   charcount = int(charcount)
   charcount = (charcount + 1)

   encoded_string = 0

   while encoded_password != encoded_string:
      charrange = random.randrange(1,charcount)

      randstring = (''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(charrange)))

      result2 = hashlib.sha384(randstring.encode())

      encoded_string = (result2.hexdigest())

      if (encoded_password == encoded_string):
         print(input("\nThe retard's password is:\t" + randstring))
         break
      else:
         continue

def SHA512():                                                              #SHA512 Bruteforce Module                         

   encoded_password = input("\nEnter your SHA512 encrypted password:\t")

   charcount = input("\nAbout how many characters is your users password?\t")
   charcount = int(charcount)
   charcount = (charcount + 1)

   encoded_string = 0

   while encoded_password != encoded_string:
      charrange = random.randrange(1,charcount)

      randstring = (''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(charrange)))

      result2 = hashlib.sha512(randstring.encode())

      encoded_string = (result2.hexdigest())

      if (encoded_password == encoded_string):
         print(input("\nThe retard's password is:\t" + randstring))
         break
      else:
         continue

def MD5():                                                              #MD5 Bruteforce Module                         

   encoded_password = input("\nEnter your MD5 encrypted password:\t")

   charcount = input("\nAbout how many characters is your users password?\t")
   charcount = int(charcount)
   charcount = (charcount + 1)

   encoded_string = 0

   while encoded_password != encoded_string:
      charrange = random.randrange(1,charcount)

      randstring = (''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(charrange)))

      result2 = hashlib.md5(randstring.encode())

      encoded_string = (result2.hexdigest())

      if (encoded_password == encoded_string):
         print(input("\nThe retard's password is:\t" + randstring))
         break
      else:
         continue

def Blake2b():                                                              #MD5 Bruteforce Module                         

   encoded_password = input("\nEnter your Blake2b encrypted password:\t")

   charcount = input("\nAbout how many characters is your users password?\t")
   charcount = int(charcount)
   charcount = (charcount + 1)

   encoded_string = 0

   while encoded_password != encoded_string:
      charrange = random.randrange(1,charcount)

      randstring = (''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(charrange)))

      result2 = hashlib.blake2b(randstring.encode())

      encoded_string = (result2.hexdigest())

      if (encoded_password == encoded_string):
         print(input("\nThe retard's password is:\t" + randstring))
         break
      else:
         continue

def Blake2s():                                                              #MD5 Bruteforce Module                         

   encoded_password = input("\nEnter your Blake2s encrypted password:\t")

   charcount = input("\nAbout how many characters is your users password?\t")
   charcount = int(charcount)
   charcount = (charcount + 1)

   encoded_string = 0

   while encoded_password != encoded_string:
      charrange = random.randrange(1,charcount)

      randstring = (''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(charrange)))

      result2 = hashlib.blake2s(randstring.encode())

      encoded_string = (result2.hexdigest())

      if (encoded_password == encoded_string):
         print(input("\nThe retard's password is:\t" + randstring))
         break
      else:
         continue
      
def Base16():                                                              #Base16 Decode Module 
   
   encoded_password = input("\nEnter your Base16 encoded password:\t")
   
   password = base64.b16decode(encoded_password)
   
   password = password.decode('ascii')
   
   print(input("\nThe retard's password is:\t" + str(password)))
      
def Base32():                                                              #Base32 Decode Module
   
   encoded_password = input("\nEnter your Base32 encoded password:\t")
   
   password = base64.b32decode(encoded_password)
   
   password = password.decode('ascii')
   
   print(input("\nThe retard's password is:\t" + str(password)))
   
      
def Base64():                                                              #Base64 Decode Module
   
   encoded_password = input("\nEnter your Base64 encoded password:\t")
   
   password = base64.b64decode(encoded_password)
   
   password = password.decode('ascii')
   
   print(input("\nThe retard's password is:\t" + str(password)))
   
def Base85():                                                              #Base85 Decode Module
   
   encoded_password = input("\nEnter your Base85 encoded password:\t")
   
   password = base64.a85decode(encoded_password)
   
   password = password.decode('ascii')
   
   print(input("\nThe retard's password is:\t" + str(password)))

def MenuControl():
   if MenuInput == 1:
      SHA1()
   elif MenuInput == 2:
      SHA224()
   elif MenuInput == 3:
      SHA256()
   elif MenuInput == 4:
      SHA384()
   elif MenuInput == 5:
      SHA512()
   elif MenuInput == 6:
      MD5()
   elif MenuInput == 7:
      Blake2b()
   elif MenuInput == 8:
      Blake2s()
   elif MenuInput == 9:
      Base16()
   elif MenuInput == 10:
      Base32()
   elif MenuInput == 11:
      Base64()
   elif MenuInput == 12:
      Base85()
   elif MenuInput == 0:
      exit
MenuControl()