import hashlib
import random
import secrets
import string

encoded_password = input("Enter your SHA256 encrypted password:\t")

bruh = input("\nAbout how many characters is your users password? (The more characters you enter, the longer this may take, however you may never get a result if you enter too little):\t")
bruh = int(bruh)
bruh = (bruh + 1)

encoded_string = 0

while encoded_password != encoded_string:
    poo = random.randrange(1,bruh)

    randstring = (''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase) for i in range(poo)))

    result2 = hashlib.sha256(randstring.encode())

    encoded_string = (result2.hexdigest())

    if (encoded_password == encoded_string):
       print(input("\nThe retard's password is:\t" + randstring))
       break
    else:
      continue
