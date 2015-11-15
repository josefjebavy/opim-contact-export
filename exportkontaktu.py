#!/usr/bin/env python
# -*- coding: utf-8 -*- 

# export contact from OPIM DB
# tested on Open MokoNeo Freerunner with SHR system.

import csv 
import sqlite3
db = sqlite3.connect("/etc/freesmartphone/opim/pim.db")

cur = db.cursor() 

cur1 = db.cursor()

# Use all the SQL you like
cur.execute("SELECT * FROM contacts")

# print all the first cell of all the rows
for row in cur.fetchall() :
    id = row[0]
    row1=cur1.execute("SELECT * FROM  contacts_email  where contacts_id=?",[id])
    email=""
    try:
        email=row1.next()[3]
    except:
        pass
    name=""
    try:
        name=cur1.execute('select value from contacts_name where contacts_id=? and field_name="Name"',[id]).next()[0]
    except:
        pass
 
    surname=""
    try:
        surname=cur1.execute('select value from contacts_name where contacts_id=? and field_name="Surname"',[id]).next()[0]
    except:
        pass


    affi=""
    try:
        affi=cur1.execute('select value from contacts_generic where contacts_id=? and field_name="Affiliation"',[id]).next()[0]
    except:
        pass

    mp=""
    try:
        mp=cur1.execute('select value from contacts_phonenumber where contacts_id=? and field_name="Mobile phone"',[id]).next()[0]
    except:
        pass
    p=""
    try:
        p=cur1.execute('select value from contacts_phonenumber where contacts_id=? and field_name="Phone"',[id]).next()[0]
    except:
        pass
    cp=""
    try:
        cp=cur1.execute('select value from contacts_phonenumber where contacts_id=? and field_name="Cell phone"',[id]).next()[0]
    except:
        pass
    hp=""
    try:
        hp=cur1.execute('select value from contacts_phonenumber where contacts_id=? and field_name="Home phone"',[id]).next()[0]
    except:
        pass

#Mobile phone
#Phone
#Cell phone
#Home phone
    #print str(id)+":"+name+" "+surname+";"+email+";mp:"+mp+";p:"+p+";cp:"+cp+";hp:"+hp
    print "BEGIN:VCARD"              
    print "VERSION:3.0"            
    print "FN:"+name+" "+surname
    print "N:"+surname+";"+name+";;;"
    if mp!="":             
        print "TEL;TYPE=MOBILE,VOICE:"+mp
    if p!="":             
        print "TEL;TYPE=PHONE,VOICE:"+p
    if cp!="":             
        print "TEL;TYPE=CELL,VOICE:"+cp
    if hp!="":             
        print "TEL;TYPE=HOME,VOICE:"+hp
        
    if email!="":             
        print "EMAIL:"+email
    if affi!="":             
        print "ORG:"+affi
        
    print "END:VCARD" 


# self.curs.execute(""" insert into data  (datetime,cislo ) 
#             values(date('now'),?)  """, [cislo])

cur.close();
cur1.close();

db.close();
