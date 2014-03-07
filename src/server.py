import socket
import re

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.setsockopt(socket.IPPROTO_TCP, socket.TCP_NODELAY, 1)
serversocket.bind(('192.168.1.114', 7777))

serversocket.listen(5)

clientthings = []
player_positions = {}
while 1:
    (clientsocket, address) = serversocket.accept()
    print 'accepted connection'
    
    
    final_msg = []
    end_loop = False
    while end_loop == False: 
        
        sent_msg_part = 'placeholder_string'
        while sent_msg_part != 'endmsg':
            sent_msg = clientsocket.recv(16384).split()
            for sent_msg_part in sent_msg:
                if sent_msg_part != 'endmsg':
                    try:
                        final_msg.append(float(sent_msg_part))
                    except ValueError:
                        final_msg.append(sent_msg_part)
        
        if final_msg[0] == 'sending_player_positions':
            print 'adding positions'
            player_positions[final_msg[1]] = [final_msg[2],final_msg[3],final_msg[4],final_msg[5]]
            
            
            
            
        elif final_msg[0] == 'receiving_player_positions':
            print 'player_positions: ' + str(player_positions)
            for player in player_positions:
                clientsocket.send(player + ' ')
                for player_info in range(len(player_positions[player])):
                    clientsocket.send(str(player_positions[player][player_info]) + ' ')
                clientsocket.send('endplayermsg' + ' ')
            clientsocket.send('endmsg ')
            
            
            
        elif final_msg[0] == 'purge_player_positions_list':
            player_positions = {}
        
        else:
            clientsocket.send ('query not found')
            
            

                
        end_loop = True
    print 'end of query'