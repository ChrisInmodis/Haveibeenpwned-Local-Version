import sqlite3

#erstellt automatisch eine SQLite DB mit dem Titel: pwned_indexed
conn = sqlite3.connect("pwned_indexed")
c = conn.cursor()

#DB wird im selben Verzeichnis erstellt in dem das Skript liegt
c.execute("CREATE TABLE passwords (hash text, prevalence integer)")
#Index ermöglicht schnellere Abfragen
c.execute("CREATE UNIQUE INDEX idx_hash ON passwords (hash)")

hashvalue = ""
prevalence = 0
count = 0

print("Starting...")
path = "C:/Path/to/your/file/pwned_ordered.txt"
input_file = open(path,"r")
for line in input_file: 
    split = line.split(":")
    hashvalue = split[0]
    prevalence = split[1]

    c.execute("INSERT INTO passwords (hash, prevalence) VALUES(?, ?)", (hashvalue, prevalence))
    if(count % 1000000 == 0):
        print("1.000.000 done")
    count += 1

conn.commit()
conn.close()

