import sqlite3

#Create table
conn = sqlite3.connect('factory.db')
c = conn.cursor()

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

def machine_data_entry():
    print()
    print("*** INPUT MACHINE DATA ***")
    machine_no = input("Machine No: ")
    lot_no = input("Lot No: ")
    downtime = input("Downtime: ")
    runtime = input("Runtime: ")
    machine_data = [(machine_no,lot_no,downtime,runtime)]
    c.executemany("INSERT INTO machine VALUES (?,?,?,?)",machine_data)
    conn.commit()
    print("\nYour entry has been recorded!")
    Menu()

def machine_data_display():
    header = " MACHINE DATA REPORT "
    footer = " END OF REPORT "
    print("\n"+header.center(60, '*')+"\n")
    c.execute("SELECT * FROM machine")

    items = c.fetchall()

    from tabulate import tabulate

    print(tabulate(items, headers=["MACHINE NO","LOT NO.","DOWNTIME", "RUNTIME"]))
    
    print("\n"+footer.center(60, '*'))
    Menu()

Menu()


#Loop inserting data into the table
while (response != '0'):

    if response == '1':
        machine_data_entry()
    elif response == 0: break
    
    if response == '2':
        machine_data_display()
    elif response == 0: break



conn.close()

