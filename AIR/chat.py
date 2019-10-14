import re
import sqlite3

connection = sqlite3.connect('chatdb.sqlite')
cursor = connection.cursor()

cursor.execute('CREATE TABLE chatTable (query TEXT, reply TEXT)')

B = 'Hello!'
print('B: ' + B)

while True:

    H = raw_input('H: ')
    if H == '':
        break;

    cursor.execute('SELECT reply FROM chatTable WHERE query = ?', (H,))
    row = cursor.fetchone()
    if row:
        print('B: ' + row[0])
    else:
        B = H
        print('B: ' + B + ' "seems to be new entry, train me please!"')
        H = raw_input('H: ')
        if H == '':
            break
        cursor.execute('INSERT INTO chatTable VALUES (?, ?)', (B, H))
        connection.commit()

