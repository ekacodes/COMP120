import sqlite3

#Create table
conn = sqlite3.connect('factory.db')
c = conn.cursor()

c.execute('''DROP TABLE machine''')

c.execute('''CREATE TABLE machine
             (machine_no text, 
             lot_no text, 
             down_factor text,
             downtime integer, 
             runtime integer)
''')

def inputFakeData():
    fake_data = [
            ('F01','22ABCD001','Quality Check',30,50),
            ('F02','22ABCD002','Evaluation',40,50),
            ('F03','22ABCD003','PM',20,50),
            ('F02','22ABCD004','BM',10,50)
        ]
    c.executemany("INSERT INTO machine VALUES (?,?,?,?,?)",fake_data)

inputFakeData()

def Menu():
    #Display main menu
    print("---------------------------")
    print("Main Menu")
    print("---------------------------")
    print("1) Input machine data")
    print("2) Machine data report")
    print("3) Machine efficiency report")
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
            
        if response == '3':
            machine_efficiency()

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
    
def machine_efficiency():
    header = " MACHINE EFFICIENCY REPORT "
    footer = " END OF REPORT "
    print("\n"+header.center(70, '*')+"\n")
    c.execute("SELECT sum(downtime) FROM machine WHERE machine_no = 'F01'")
    sum_down1 = c.fetchone()[0]
    c.execute("SELECT sum(runtime) FROM machine WHERE machine_no = 'F01'")
    sum_run1 = c.fetchone()[0]
    
    c.execute("SELECT sum(downtime) FROM machine WHERE machine_no = 'F02'")
    sum_down2 = c.fetchone()[0]
    c.execute("SELECT sum(runtime) FROM machine WHERE machine_no = 'F02'")
    sum_run2 = c.fetchone()[0]
    
    c.execute("SELECT sum(downtime) FROM machine WHERE machine_no = 'F03'")
    sum_down3 = c.fetchone()[0]
    c.execute("SELECT sum(runtime) FROM machine WHERE machine_no = 'F03'")
    sum_run3 = c.fetchone()[0]

    
    print("Machine","\tEfficiency")
    
    print(f"F01\t\t{'{0:.0f}%'.format(((sum_run1-sum_down1)/sum_run1)*100)}")
    print(f"F02\t\t{'{0:.0f}%'.format(((sum_run2-sum_down2)/sum_run2)*100)}")
    print(f"F03\t\t{'{0:.0f}%'.format(((sum_run3-sum_down3)/sum_run3)*100)}")
    
    print("\n"+footer.center(70, '*'))
    Menu()
    
Menu()


conn.close()

