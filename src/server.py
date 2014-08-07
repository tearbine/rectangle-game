import socket, select

serversocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
serversocket.bind(('localhost', 7777))

toread = [serversocket]


clientthings = []
clientsockets = {}
player_positions = {}
while 1:
    print 'waiting for connection'
    rready,wready, err = select.select(toread, [],[])
    print 'connection %s is ready' % rready
    
    
    print 'connected!'
    final_msg = []
    end_loop = False
    while end_loop == False: 
        
        '''sent_msg_part = 'placeholder_string'
        while sent_msg_part != 'endmsg' or len(sent_msg_part) == 0:
            sent_msg_part = 'endmsg' # if sent_msg doesn't return anything
            
            data = sent_msg
            for sent_msg_part in sent_msg:
                print 'sent_msg: ',sent_msg_part
                if sent_msg_part != 'endmsg':

                    try:
                        final_msg.append(float(sent_msg_part))
                    except ValueError:
                        final_msg.append(sent_msg_part)'''
        data, addr = serversocket.recvfrom(4096)
        
        print 'final msg: ', final_msg
        
        if len(final_msg) == 0:
            end_loop = True
            
        elif final_msg[0] == 'sending_player_positions':
            print 'adding positions', [final_msg[2],final_msg[3],final_msg[4],final_msg[5]]
            player_positions[final_msg[1]] = [final_msg[2],final_msg[3],final_msg[4],final_msg[5]]
            print 'done adding positions'
            end_loop = True
            
            
            
            
        elif final_msg[0] == 'receiving_player_positions':
            print 'player_positions: ' + str(player_positions)
            for player in player_positions:
                clientsockets[clientsocket] = clientsocket.sendto(player + ' ')
                for player_info in range(len(player_positions[player])):
                    clientsockets[clientsocket] = clientsocket.sendto(str(player_positions[player][player_info]) + ' ')
                clientsockets[clientsocket] = clientsocket.sendto('endplayermsg' + ' ')
            clientsockets[clientsocket] = clientsocket.sendto('endmsg ')
            
            sent_msg = ''
            while sent_msg != 'received_all_positions':
                sent_msg = clientsocket.recvfrom(4096)
                print 'waiting for done check'
            end_loop = True
            
            
            
        elif final_msg[0] == 'purge_player_positions_list':
            player_positions = {}
            end_loop = True
        
        
        
        print 'end of loop'

        
#end_loop = True
    
