import psutil
import time
import pyodbc

#
server_name = 'DHRUBO'
database_name = 'System_info'

# Establish a connection to SQL Server
con = pyodbc.connect('Driver={SQL Server};'
                     'Server=' + server_name + ';'
                     'Database=' + database_name + ';'
                     'Trusted_Connection=yes;')

cursor = con.cursor()



# import psutil
# import time 
# import pyodbc
# import mysql.connector
# con = pyodbc.connect('Driver= {SQL SERVER};'
#                      'Server =  Dhrubo;'
#                      'Database= System_info;'
#                      'Trusted_Connection=yes;')
                     




# cursor = con.cursor()

while 1==1:
    Cpu_usage = psutil.cpu_percent(interval=1)
    Memory_usage = psutil.virtual_memory()[2]
    
    Cpu_interrupts = psutil.cpu_stats()[1]
    Cpu_calls = psutil.cpu_stats()[3]

    Memory_used = psutil.virtual_memory()[3]
    # Memory_used_percent = (Memory_used/Memory_usage)*100
    
    Memory_free = psutil.virtual_memory()[4]
    # Memory_free_percent = (Memory_free/Memory_used)*100

    bytes_sent = psutil.net_io_counters()[0]
    bytes_received = psutil.net_io_counters()[1]

    disk_usage = psutil.disk_usage('/')[3]
    
    cursor.execute('insert into Performance values (GETDate (),'
                   +str(Cpu_usage)+','
                   +str(Memory_usage)+','
                   +str(Cpu_interrupts)+','
                   +str(Cpu_calls)+','
                   +str(Memory_used)+','
                   +str(Memory_free)+','
                   +str(bytes_sent)+','
                   +str(bytes_received)+','
                   +str(disk_usage)+')')
    con.commit()
    print(Memory_usage)
    time.sleep(1)





# con = pyodbc.connect(driver='{SQL Server}', host='DESKTOP-5QJ8Q4M\SQLEXPRESS', database='System_info',
#                       trusted_connection='yes', user='Dhrubo', password='sql1234')

# Driver = 'SQL Server'
# Server_name = 'DHRUBO'
# database = 'System_info'
# # password = 'sql1234'

# connection_string = f"""
#     Driver={Driver};
#     Server = {Server_name};
#     Database={database};
#     Trusted_Connection=yes;
# """

# con = odbc.connect(connection_string)