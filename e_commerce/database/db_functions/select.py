import sqlite3
import sys
# sys.path.append('/home/gabriel/Programs/SWE/groupProject/e_commerce/')
# import create_account.create as edit


## attempts to connect to the database
def selector(command):
    try:
        connection = sqlite3.connect("sqlite.db")

    except:
        print("Failed connection.")

        ## exits the program if unsuccessful
        sys.exit()

    ## cursor to send queries through
    cursor = connection.cursor()


    #execute the command passed as argument
    cursor.execute(command)
    result = cursor.fetchall()

    #close connection
    cursor.close()
    connection.close()
    
    #return result
    return result
