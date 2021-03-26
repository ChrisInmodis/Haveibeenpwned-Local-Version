import sqlite3
import hashlib,binascii

password = input("Enter your Password: ")
hash = hashlib.new('md4', password.encode('utf-16le')).digest()

#Hash in Großbuchstaben und zu String konvertieren
hash = binascii.hexlify(hash).upper().decode("utf-8")

#mit DB verbinden
conn = sqlite3.connect("pwned_indexed")
c = conn.cursor()
          
#Prüfen ob Hash in DB
c.execute("SELECT * FROM passwords WHERE hash=?", (hash,))
result = c.fetchone()
print("Checking: ", hash)
if(result != None ):
    print("Pwned: ", hash)
else:
    print("Not pwned!")

conn.commit()
conn.close()  
