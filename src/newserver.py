import socket
import json

server_address = '192.168.1.114', 7777
message = 'hi'

serversocket = socket.socket(socket.AF_INET,
                             socket.SOCK_DGRAM)
serversocket.bind(server_address)

player_position_list = {}

while True:
    print 'listening. player positions is: ', player_position_list
    recv_data, addr = serversocket.recvfrom(1024)
    recv_data = json.loads(recv_data)
    print 'message received: ', recv_data
    
    query = recv_data[0]
    print 'query: ' + query
    
    if query == 'uploading_position':
        data = recv_data[1]
        print 'recieved:', data
        for position in data:
            player_position_list[data[0]] = int(data[1]),int(data[2]),int(data[3]),int(data[4])
        print 'adding: {0}'.format(player_position_list[data[0]])
        
    elif query == 'downloading_positions':
        print 'sending: '+ json.dumps(player_position_list)
        serversocket.sendto(json.dumps(player_position_list), addr)
        
    else:
        print 'elsed: ', recv_data
        serversocket.sendto('what are you saying to me', addr)