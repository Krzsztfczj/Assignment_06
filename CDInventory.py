#------------------------------------------#
# Title: Assignment06_Starter.py
# Desc: Working with classes and functions.
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# Kris Czaja, 2021-Nov-20, Completed TODOs
# Kris Czaja, 2021-Nov-20, added docstrings.
#------------------------------------------#

# -- DATA -- #
strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object
strID = ''
strTitle = ''
strArtist = ''

# -- PROCESSING -- #

class DataProcessor:
    """Processing the data within the program"""
    # Completed: TODO add functions for processing here
        #Moved CD deletion option 
        #Moved adding CD


    # Completed: TODO move processing code into function
        # deleting CD from inventory was moved to DataProcessor section
        # and defined as function CDDel.
    @staticmethod
    def CDdel(table):
        """Function to delete CDs from the inventory

        Searches for ID input by user (input is not part of the function) and removes it from the table.

        Args:
            table - 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            Displays CD Inventory after the deletion.
        """
        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == intIDDel:
                del table[intRowNr]
                blnCDRemoved = True
                break
        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        IO.show_inventory(table)
    
    
    # Completed: TODO move processing code into function
            # addidng CD was moved to DataProcessor section
            # and defined as CDDadd.
    @staticmethod           
    def CDadd(CDEntry, table):
        """Function to add CDs to the inventory

        Records user's input, which is not part of the function, and stores it in the table, but not the text file.

        Args:
            CDEntry - effectively information on one CD in the form od a dictionary
            table - 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            None
        """
        IO.AddInput()
        intID = int(strID)
        CDEntry = {'ID': intID, 'Title': strTitle, 'Artist': strArtist}
        table.append(CDEntry)


class FileProcessor:
    """Processing the data to and from text file"""
        # Completed: TODO Add code here
            #Moved to function inventory saving
            
    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        #K.C. - initially I simply replaced 'r' with 'a+' in row 102, but then the program wouldn't load data from file - I don't know why.
        #so I went with second best option - opened with 'a' in case there was no file, closed and opened with 'r'. Ugly, but works.
        objFile = open(file_name, 'a')   
        objFile.close() 
        objFile = open(file_name, 'r')   
        for line in objFile:
            data = line.strip().split(',')
            dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
            table.append(dicRow)
        objFile.close()

        # Completed: TODO move processing code into function
            #moved file saving process to the write_file function

    @staticmethod
    def write_file(table,file):
        """Function to save inventory to file.
        
        Saves data existing in program memory to a text file in the same format of a 2d table.
        
        Args:
            table - 2D data structure (list of dicts) that holds the data during runtime
        Returns:
            None.
        
        """
            
        objFile = open(file, 'w')
        for row in table:
                lstValues = list(row.values())
                lstValues[0] = str(lstValues[0])
                objFile.write(','.join(lstValues) + '\n')
        objFile.close()


# -- PRESENTATION (Input/Output) -- #

class IO:
    """Handling Input / Output"""
   # Completed: TODO add I/O functions as needed
        #Moved input for adding CD
        
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """

        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

       
    
     # Completed: TODO move IO code into function
         # Input required for the purpose of adding CD was moved to IO.
         # To meet all SoC requirements, the variables were defined as global.
    
    def AddInput():
        """Collects user input for further saving.
        
        Args:
            None
        Returns
            None

        """
        global strID
        global strTitle
        global strArtist
        strID = input('Enter ID: ').strip()
        strTitle = input('What is the CD\'s title? ').strip()
        strArtist = input('What is the Artist\'s name? ').strip()
        
 
# 1. When program starts, read in the currently saved Inventory
FileProcessor.read_file(strFileName, lstTbl)

# 2. start main loop
while True:
    # 2.1 Display Menu to user and get choice
    IO.print_menu()
    strChoice = IO.menu_choice()

    # 3. Process menu selection
    # 3.1 process exit first
    if strChoice == 'x':
        break
    # 3.2 process load inventory
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    
    # 3.3 process add a CD
    elif strChoice == 'a':
        # 3.3.1 Ask user for new ID, CD Title and Artist
        # 3.3.2 Add item to the table
        DataProcessor.CDadd(dicRow,lstTbl)
        
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
   
  # 3.4 process display current inventory
    
    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.
    
    # 3.5 process delete a CD
    
    elif strChoice == 'd':
        # 3.5.1 get Userinput for which CD to delete
        # 3.5.1.1 display Inventory to user
        IO.show_inventory(lstTbl)
        # 3.5.1.2 ask user which ID to remove
        intIDDel = int(input('Which ID would you like to delete? ').strip())
        # 3.5.2 search thru table and delete CD
        DataProcessor.CDdel(lstTbl)
        continue  # start loop back at top.
        
    # 3.6 process save inventory to file
    
    elif strChoice == 's':
        # 3.6.1 Display current inventory and ask user for confirmation to save
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        # 3.6.2 Process choice
        if strYesNo == 'y':
            # 3.6.2.1 save data
            FileProcessor.write_file(lstTbl, strFileName)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    
    # 3.7 catch-all should not be possible, as user choice gets vetted in IO, but to be save:
    else:
        print('General Error')




