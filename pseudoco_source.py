import sqlite3

#Create table
conn = sqlite3.connect('factory.db')
c = conn.cursor()

#c.execute('''DROP TABLE machine''')

c.execute('''CREATE TABLE IF NOT EXISTS machine
             (machine_no text, 
             lot_no text, 
             down_factor text,
             downtime integer, 
             runtime integer)
''')

def checkTable():
    c.execute("""SELECT name FROM sqlite_master WHERE type='table' AND name='machine'""")
    result = c.fetchone()
    if result == None:
        inputFakeData()

checkTable()

def inputFakeData():
    fake_data = [
            ('F01','22ABCD001','QCCheck',30,50),
            ('F02','22ABCD002','Eval',40,50),
            ('F03','22ABCD003','PM',20,50),
            ('F02','22ABCD004','BM',10,50)
        ]
    c.executemany("INSERT INTO machine VALUES (?,?,?,?)",fake_data)

def Menu():
    #Display main menu
    print("---------------------------")
    print("Main Menu")
    print("---------------------------")
    print("1) Input machine data")
    print("2) Machine data report")
    print("3) Menu 3")
    print("4) Menu 4")
    print("0) Exit")
    print("---------------------------")
    #User response
    global response 
    response = input("Enter 1-5 to continue or 0 to exit: ")

    #Loop inserting data into the table
    while response!='0':
        if response == '1':
            machine_data_entry()
    
        if response == '2':
            machine_data_display()

def machine_data_entry():
    print()
    print("*** INPUT MACHINE DATA ***")
    machine_no = input("Machine No: ")
    lot_no = input("Lot No: ")
    down_factor = input("Factor: ")
    downtime = input("Downtime: ")
    runtime = input("Runtime: ")
    machine_data = [(machine_no,lot_no,down_factor,downtime,runtime)]
    c.executemany("INSERT INTO machine VALUES (?,?,?,?,?)",machine_data)
    conn.commit()
    print("\nYour entry has been recorded!")
    Menu()

def machine_data_display():
    header = " MACHINE DATA REPORT "
    footer = " END OF REPORT "
    print("\n"+header.center(70, '*')+"\n")
    c.execute("SELECT rowid, * FROM machine")

    items = c.fetchall()

    from tabulate import tabulate
    print(tabulate(items, headers=["MACHINE NO","LOT NO.","DOWNTIME FACTOR","DOWNTIME", "RUNTIME"]))
    
    print("\n"+footer.center(70, '*'))
    Menu()

Menu()


conn.close()

