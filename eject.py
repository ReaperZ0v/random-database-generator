#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 15:42:13 2020

@author: ReaperZ0v
"""

from faker import Faker
import pandas as pd
import numpy as np
import sqlite3
import time
import sys
import os
import re


class SQLEject:
    def __init__(self, startup_check):
        self.startup_check = bool(startup_check)
        if self.startup_check == True:
            print("[!] Installing Required Dependencies for SQLejector...")
            packages = ["Faker", "pandas", "numpy"]
            for package in packages:
                os.system(f"pip3 install {package}".format())
            
        print("[!] Booting up the SQLejector...")
        time.sleep(3.5)
        
        print("[+] Successfully Booted up the SQLejector! \n")
        for spacing in range(1):
            print("\n")
    
    def database_assembler(self, db_name, n_rows, export_to):
        self.db_name = db_name
        self.n_rows = n_rows
        self.export_to = export_to
        
        print(f"[!] Assembling Database {db_name}...".format())
        
        time.sleep(1.7)
        if os.path.exists(db_name):
            err_dialogue = input(f"[!] Database {db_name} already exists! Remove and create new (y/n)? : ".format())
            if err_dialogue == "y":
                os.remove(db_name)
                connection = sqlite3.connect(db_name)
                
            else:
                sys.exit()
            
        else:
            connection = sqlite3.connect(db_name)
            
        messages = [f"[+] Database {db_name} Assembled!", "[*] Writing that db's table...", 
                    f"[+] Table all setup within {db_name} database!"]
        
        for msg in messages:
            print(msg)
            time.sleep(2.2)
        
        print("\n")
        self.infiltrate(self.export_to)
        
    def infiltrate(self, export_var):
        VAR_SQLITE = "sqlite"
        VAR_DATA_FRAME = "dataframe"
        
        if export_var == VAR_SQLITE:
            faker_object = Faker()
            if os.path.exists(self.db_name):
                connection = sqlite3.connect(self.db_name)
                cursor_initializer = connection.cursor()
                sql_statement = """CREATE TABLE Customers(id INTEGER PRIMARY KEY AUTOINCREMENT, 
                                                          name VARCHAR(100), job VARCHAR(50), 
                                                          email VARCHAR(50), country VARCHAR(50), city VARCHAR(50))"""
                cursor_initializer.execute(sql_statement)        
                for iteration in range(self.n_rows):
                    sql_query = "INSERT INTO Customers(name, job, email, country, city) VALUES (?, ?, ?, ?, ?, ?)"                      
                    cursor_initializer.execute(sql_query, (faker_object.first_name(),
                                                           faker_object.job().replace(' ', '_'),
                                                           faker_object.ascii_free_email(),
                                                           faker_object.country(),
                                                           faker_object.city()
                                              ))
                    connection.commit()
                print(f"[+] {self.n_rows} rows of random data written to database {self.db_name}".format())
                
        else:
            print(f"[!] Export parameter {export_var} does not exist.")
            
        

sqej = SQLEject(startup_check=False)
sqej.database_assembler("test.db", 25, "sqlite")
        
        


