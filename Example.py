#[username,password,clientcode,ciddata,[messageType,eventQualifier,eventCode,partition,zoneUser],]

# Importing the ContactIDServer class from csvAlarmServer module
from csvAlarmServer import ContactIDServer

# List of client codes allowed to interact with this server
allowed_clients = ['1234']

# Define the callback function to process received alarm data
def processAlarm(data):
    # Check if the client code is in the allowed list and the event code is not '602' (suppress polling messages)
    if data[2] in allowed_clients and data[4][2] != '602':
        print("Data:  " + str(data))  # Print the entire data list received from the alarm
        print("Auth User:  " + data[0]) #Print the Username used for authentication
        print("Auth Pass:  " + data[1]) #Print the Password used for authentication
        print("Event Qualifier: " + server.find_event_quals(data[4][1]))  # Retrieve and print the event qualifier description
        print("Event Code: " + server.find_event_description(data[4][2]))  # Retrieve and print the event code description
        print("Partition: " + data[4][3])  # Print the partition where the event occurred
        print("Zone / User: " + data[4][4])  # Print the zone or user associated with the event
        print("Client Code: " + data[2])  # Print the client code associated with the data
        print("----------------------------")  # Print separators for clarity in output
        print("----------------------------")

# Initialize the ContactIDServer with the specified port and the callback function
server = ContactIDServer(BindPort=5553, callback=processAlarm)

# Start the server to listen for incoming alarm messages
server.run_server()
