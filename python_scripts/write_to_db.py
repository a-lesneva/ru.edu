import sqlite3
import json

connection = sqlite3.connect('schoolsdb.sqlite')
cur = connection.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Schools;
DROP TABLE IF EXISTS State;
DROP TABLE IF EXISTS Suburb;

CREATE TABLE Schools (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT NOT NULL,
    address_line TEXT NOT NULL,
    suburb_id INTEGER NOT NULL,
    state_id INTEGER NOT NULL,
    website TEXT,
    email TEXT,
    working_hours TEXT,
    person TEXT,
    details TEXT,
    social_media TEXT,
    active BOOLEAN NOT NULL
);

CREATE TABLE State (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT NOT NULL UNIQUE 
);

CREATE TABLE Suburb (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name TEXT NOT NULL UNIQUE,
    postcode TEXT NOT NULL,
    state_id INTEGER NOT NULL
);
''')

f = open('corrected_list.json').read()
data = json.loads(f)
for d in data:
    
    name = d['name']
    address_line = d['address']
    website = d['website']
    person = d['person']
    email = d['email']
    working_hours = d['hours']
    social_media = d['social media']
    details = d['details']
    state = d['state']
    postcode = d['postcode']
    suburb = d['suburb']
    active = True

    cur.execute('INSERT OR IGNORE INTO State (name) VALUES ( ? )', (state, ))
    cur.execute('SELECT id from State WHERE name = ?', (state, ))
    state_id = cur.fetchone()[0]

    cur.execute('INSERT OR IGNORE INTO Suburb (name, postcode, state_id) VALUES (?, ?, ?)', (suburb, postcode, state_id))
    cur.execute('SELECT id from Suburb WHERE name = ?', (suburb, ))
    suburb_id = cur.fetchone()[0]

    cur.execute('''INSERT INTO Schools (
        name, address_line, suburb_id, state_id, website, email, working_hours, person, details,
        social_media, active) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
        (name, address_line, suburb_id, state_id, website, email, working_hours, person, details,
        social_media, active))
    connection.commit()
connection.close()


