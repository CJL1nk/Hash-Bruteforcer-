import hashlib
from time import sleep
import base64

MenuInput = 0

def ModuleMenu():
   print("_______________________________________")
   print("Select Encryption Module")
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

def SHA1():
    
    encrypt_text = input("\nEnter the text you would like to encrypt:\t")
    
    encrypted_text = hashlib.sha1(encrypt_text.encode())
    
    encoded_text = (encrypted_text.hexdigest())
    
    print(input("\nYour hashed text is\t" + encoded_text))
    
def SHA224():
    
    encrypt_text = input("\nEnter the text you would like to encrypt:\t")
    
    encrypted_text = hashlib.sha224(encrypt_text.encode())
    
    encoded_text = (encrypted_text.hexdigest())
    
    print(input("\nYour hashed text is\t" + encoded_text))

def SHA256():
    
    encrypt_text = input("\nEnter the text you would like to encrypt:\t")
    
    encrypted_text = hashlib.sha256(encrypt_text.encode())
    
    encoded_text = (encrypted_text.hexdigest())
    
    print(input("\nYour hashed text is\t" + encoded_text))
    
def SHA384():
    
    encrypt_text = input("\nEnter the text you would like to encrypt:\t")
    
    encrypted_text = hashlib.sha384(encrypt_text.encode())
    
    encoded_text = (encrypted_text.hexdigest())
    
    print(input("\nYour hashed text is\t" + encoded_text))
    
def SHA512():
    
    encrypt_text = input("\nEnter the text you would like to encrypt:\t")
    
    encrypted_text = hashlib.sha512(encrypt_text.encode())
    
    encoded_text = (encrypted_text.hexdigest())
    
    print(input("\nYour hashed text is\t" + encoded_text))
    
def MD5():
    
    encrypt_text = input("\nEnter the text you would like to encrypt:\t")
    
    encrypted_text = hashlib.md5(encrypt_text.encode())
    
    encoded_text = (encrypted_text.hexdigest())
    
    print(input("\nYour hashed text is\t" + encoded_text))
    
def Blake2b():
    
    encrypt_text = input("\nEnter the text you would like to encrypt:\t")
    
    encrypted_text = hashlib.blake2b(encrypt_text.encode())
    
    encoded_text = (encrypted_text.hexdigest())
    
    print(input("\nYour hashed text is\t" + encoded_text))
    
def Blake2s():
    
    encrypt_text = input("\nEnter the text you would like to encrypt:\t")
    
    encrypted_text = hashlib.blake2s(encrypt_text.encode())
    
    encoded_text = (encrypted_text.hexdigest())
    
    print(input("\nYour hashed text is\t" + encoded_text))
    
def Base16():                                                              #Base16 Decode Module 
   
    text = input("\nEnter the text you would like to encode:\t")
    
    text_bytes = text.encode('ascii')
    
    encoded_text = base64.b16encode(text_bytes)
    
    base64_encode = encoded_text.decode('ascii')
    
    print(input("\nYour encoded text is:\t" + base64_encode))
    
def Base32():                                                              #Base16 Decode Module 
   
    text = input("\nEnter the text you would like to encode:\t")
    
    text_bytes = text.encode('ascii')
    
    encoded_text = base64.b32encode(text_bytes)
    
    base64_encode = encoded_text.decode('ascii')
    
    print(input("\nYour encoded text is:\t" + base64_encode))
    
def Base64():                                                              #Base16 Decode Module 
   
    text = input("\nEnter the text you would like to encode:\t")
    
    text_bytes = text.encode('ascii')
    
    encoded_text = base64.b64encode(text_bytes)
    
    base64_encode = encoded_text.decode('ascii')
    
    print(input("\nYour encoded text is:\t" + base64_encode))
    
def Base85():                                                              #Base16 Decode Module 
   
    text = input("\nEnter the text you would like to encode:\t")
    
    text_bytes = text.encode('ascii')
    
    encoded_text = base64.a85encode(text_bytes)
    
    base64_encode = encoded_text.decode('ascii')
    
    print(input("\nYour encoded text is:\t" + base64_encode))
    
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
