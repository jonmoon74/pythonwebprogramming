import sqlite3

# set the connection to the database (or create database if not existent
conn = sqlite3.connect('tutorial.db')
# setup a cursor for selecting and navigatig the database
c = conn.cursor()


# create a table within the database
def create_table():
    c.execute("CREATE TABLE example (Language VARCHAR, Version REAL, Skill TEXT)")

# comment out next line as only needed for initial run to create the table
# create_table()


# add data to the table
# with commit to save changes to database table
def enter_data():
    c.execute("INSERT INTO example VALUES('Python', 3.6, 'Intermediate')")
    c.execute("INSERT INTO example VALUES('Python', 2.7, 'Expert')")
    c.execute("INSERT INTO example VALUES('Python', 3.3, 'Beginner')")
    conn.commit()


def enter_dynamic_data():
    lang = input("What language? ")
    version = float(input("What skill level? "))
    skill = input("What skill level? ")

    c.execute("INSERT INTO example (Language, Version, Skill) VALUES (?, ?, ?)" (lang, version, skill))
    conn.commit()


def enter_data_via_variables(lang, version, skill):
    c.execute("INSERT INTO example VALUES(lang, version, skill)")
    conn.commit()
# close the connection to the database at the end of the script
# conn.close()
