import subprocess
import os
import mysql.connector    # Pre-Requsite mysql.connector and mysql-connector-python need to be install if not installed



def main():
    host = input("Enter Host: ")
    packet = int(input("\nEnter Packet: "))
    print("\n")
    pingResponse = os.popen(f"ping -c {packet} {host} | tail -n 1 | cut -d\" \" -f4 | cut -d '/' -f 2" ).read().split('\n')
    print("Average Ping is:", pingResponse[0])
    mySQL(host, pingResponse[0])



def mySQL(host, pingResponse):
    #establishing the connection
    conn = mysql.connector.connect(
    user='root', password='password', host='127.0.0.1', database='cyberjet')
    #Creating a cursor object using the cursor() method
    cursor = conn.cursor()

    insert_stmt = (
        "INSERT INTO node_info_log(nodeid, ping)"
        "VALUES (%s, %s)"
    )
    data = (host,pingResponse)
    print (data)
    try:
        # Executing the SQL command
        cursor.execute(insert_stmt, data)

        # Commit your changes in the database
        conn.commit()
    except:
        # Rolling back in case of error
        conn.rollback()
        
        # Closing the connection
        conn.close()

main()