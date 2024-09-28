import sqlite3       #Import the SQLite module:This imports the sqlite3 module, which allows you to work with SQLite databases in Python.

conn = sqlite3.connect('emaildb.sqlite')   #Connect to the database:This creates a connection to a SQLite database named emaildby.sqlite. If the file does not exist, it will be created.
cur = conn.cursor()  #Create a cursor object:This creates a cursor object (cur) which allows you to execute SQL commands and fetch results.

cur.execute('DROP TABLE IF EXISTS Counts')   #Drop the table if it exists:This SQL command removes the Counts table if it already exists, preparing a clean slate for new data.

cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')  #Create a new table:This creates a new table named Counts with two columns: org (to store the email domain) and count (to store the number of occurrences of that domain).

fname = input('Enter file name: ')  #Get the filename from user input:This prompts the user to enter a file name. The variable fname will hold the name of the file.
if len(fname) < 1:   #Set a default file name if none is provided:If the user does not provide a filename, it defaults to mbox.txt.
    fname = 'mbox.txt'
fh = open(fname)       #This opens the file specified by fname for reading.
for line in fh:      #Iterate through each line in the file:This loop goes through each line in the opened file.
    if not line.startswith('From: '):  #Check if the line starts with 'From: ':This condition checks if the line starts with "From: ". If it does not, the loop skips to the next iteration.
        continue
    pieces = line.split()      #Split the line into pieces:This splits the line into a list of words (pieces) based on whitespace.
    email = pieces[1]          #Extract the email address:This assumes the second piece of the line is the email address.
    org = email.split('@')[1]  #Extract the domain from the email address:This splits the email at the "@" symbol and takes the second part, which is the domain.
    cur.execute('SELECT count FROM Counts WHERE org = ?', (org, )) #Query the database for the domain:This executes a SQL command to select the current count for the extracted domain (org).
    try:   #Handle the query results:This block tries to fetch the count from the query:
        count = cur.fetchone()[0] #If it exists (cur.fetchone() returns a result), it updates the count by incrementing it by 1.
        cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (org, ))
    except:   ##If no result is found (the domain does not exist in the database), it catches the exception and inserts a new entry with a count of 1.
        cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (org, ))

conn.commit()   #Commit the changes to the database:This saves all changes made during the session to the database.

sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'   #Prepare and execute a query to get the top 10 domains:This creates a SQL command to select the top 10 domains ordered by their count in descending order. It then iterates through the results and prints each domain alongside its count.
for row in conn.execute(sqlstr):
    print(row[0], row[1])

conn.close()   #Close the connection: This closes the connection to the database, freeing up resources.