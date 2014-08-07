import socket
import json

class Client:
    def __init__(self, address):
        self.address = address        
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    def upload_position(self, player_position):
        data = ['uploading_position', player_position]
        self.socket.sendto(json.dumps(data), self.address)
        
    def download_positions(self):
        data = ['downloading_positions']
        self.socket.sendto(json.dumps(data), self.address)
        recv_data, addr = self.socket.recvfrom(1024)
        recv_data = json.loads(recv_data)
        return recv_data
      
if __name__ == '__main__':    

    
    player_position = ['my butt',422,16,32,34]
    
    client = Client(('localhost', 7777))
    
    client.upload_position(player_position)
    player_positions = client.download_positions()
    print player_positions
    
    '''clientsocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    address = 'localhost', 7777
    
    data = ['uploading_position', player_position]
    clientsocket.sendto(json.dumps(data), address)
    print 'sent: %s' %data
    
    recv_data, addr = clientsocket.recvfrom(1024)
    
    print 'server says: ' + recv_data
    
    print 'downloding now loser'
    
    data = ['downloading_positions']
    clientsocket.sendto(json.dumps(data), address)
    recv_data, addr = clientsocket.recvfrom(1024)
    recv_data = json.dumps(recv_data)
    print 'received: ' + recv_data'''    