from flask import Flask

import database #importing database file

db = database.db  #accessing our database connection

fellows = db['fellows']     #accessing the fellows collection
                            #if you notice, db is a dictionary whose collection 'fellows' is a key of that dictionary


#BASIC CRUD COMMANDS

# iNSERTING INTO THE DATABASE (CREATE)
fellow = {          #fellow is a dictionary of one person's details
    '_id': 1,      # You can specify your own id. If this is not specified the database creates one by default
    'name': 'John',
    'surname': 'Dou',
    'tribe': 'Berom',
    'siblings': ['Jane', 'Pam', 'Garos'],  #fields can be arrays 
    'age': 20,                              #fields can be integers
    'gender': 'male',
    'graduated': True,                       #fields can be boolean
    'parents': {                        #fields can also be another dictionary(nested)
        'father': 'David Dou',
        'mother': 'Mary Dou'
        }
    }

fellows.insert_one(fellow)  #inserting only one person's record at a time

fellows.insert_many(fellow1, fellow2) #inserting many records at a time



#RETRIEVING FROM A DATABASE (READ)

fellows.find() # this fetches every document from the fellows collection

fellows.find_one({'name': 'John', 'surname': 'Dou'})  #fetches the record of person with name John and surname Dou

fellows.find_one_and_delete(criteria)  #finds one record and deletes it based on the criteria


#UPDATING DOCUMENTS IN THE DATABASE (UPDATE)

# updating
fellows.update_one(criteria, update)
fellows.find_one_and_update(criteria, update)   #finds one record and updates it with the update command

# replacing
fellows.replace_one(criteria, replacement)
fellows.find_one_and_replace(criteria, replacement) #finds one record and replaces it with the replacement record



# DELETING DOCUMENTS IN THE DATABASE (DELETE)
fellows.delete_one(criteria)  # deletes one record specified
fellows.delete_many(criteria) #deletes many records at once

 

#  There are many other commands that are not as basic as these ones.
#  You can always google to find more complex commands
