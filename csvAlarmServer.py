import socket
import csv
from io import StringIO
import datetime

class ContactIDServer:
    def __init__(self, host='0.0.0.0', port=65431, callback=None):
        self.host = host
        self.port = port
        self.callback = callback
        self.server_socket = None
        self.event_codes = {
            '100': 'Medical Emergency',
            '101': 'Fire Alarm',
            '130': 'Burglary',
            '137': 'Tamper',
            '570': 'Bypass',
            '110': 'Power Outage',
            '120': 'Panic Alarm',
            '602': 'Service Test Report',
            '407': 'Remote Arming/Disarming'
        }
        self.event_quals = {
            '1': 'New Event or Opening/Disarm',
            '3': 'New Restore or Closing/Arming',
            '6': ' Previously reported condition still present (status report)',
            }
    def find_event_quals(self, event_id):
        description = self.event_quals.get(event_id)
        if description:
            return f"{description} ({event_id})"
        else:
            return f"{event_id}"
    
    def find_event_description(self, event_id):
        description = self.event_codes.get(event_id)
        if description:
            return f"{description} ({event_id})"
        else:
            return f"{event_id}"

    def parse_contact_id_message(self, contact_id_string):
        contact_id_string
        if len(contact_id_string) != 11:
            print(f"Invalid message length: {contact_id_string}")
            return ["Invalid message length"]

        mt = contact_id_string[0:2]
        q = contact_id_string[2]
        xyz = contact_id_string[3:6]
        gg = contact_id_string[6:8]
        ccc = contact_id_string[8:11]

        result = [
            contact_id_string[0:2], #mt
            contact_id_string[2],    #q
            contact_id_string[3:6],#xyz
            contact_id_string[6:8], #gg
            contact_id_string[8:11],#ccc
        
        ]
        return result
    
    def parse_csv_alarm_data(self, data):
        f = StringIO(data)
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            if row and len(row) >= 4:
                result = [
                    #data,  #raw
                    row[0],#username
                    row[1],#password
                    row[2],#client code
                    row[3],#cid
                    self.parse_contact_id_message(row[3]), #cid data disected
                    
                ]
                
        f.close()
        self.callback(result)
        return result

    def run_server(self):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen(5)
        print(f"Server listening on {self.host}:{self.port}")
        try:
            while True:
                conn, addr = self.server_socket.accept()
                #print(f"Connected by {addr}")
                #print(f"Received at: {datetime.datetime.now()}")
                try:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        decoded_message = data.decode().strip()
                        self.parse_csv_alarm_data(decoded_message)  # Or handle your decoded message
                        conn.sendall(decoded_message.encode())
                finally:
                    conn.close()
        except KeyboardInterrupt:
            print("Server is shutting down.")
        finally:
            self.shutdown_server()

    def shutdown_server(self):
        """Shut down the server cleanly by closing the server socket."""
        if self.server_socket:
            self.server_socket.close()
            print("Server socket has been closed.")
