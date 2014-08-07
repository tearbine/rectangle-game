import socket, select

class Client:
    def __init__(self, server_ip, port):
        self.server_ip = server_ip
        self.port = port
        self.addr = self.server_ip, self.port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.connect((self.server_ip, self.port))
        
        
    def sendpositions(self, player, coord1, coord2, width, height):
        
        self.sock.sendto('sending_player_positions ', self.addr)

        
        for msg_part in [player,coord1,coord2,width,height]:
            print type(self.server_ip), type(self.port)
            self.sock.sendto(str(msg_part) + ' ', self.addr)
        
        self.sock.sendto('endmsg ', self.addr)
        
            
    def recvpositions(self):     
        
        final_positions = {}
        self.sock.sendto('receiving_player_positions endmsg', self.addr)

        c_sent_msg_part = 'placeholder_string'
        sent_msg_part = []
        player_info = []
        
        while 'endmsg' not in c_sent_msg_part and c_sent_msg_part != []:
            c_sent_msg_part = self.sock.recvfrom(1024).split()
            for msg_part in c_sent_msg_part:
                try:
                    sent_msg_part.append(float(msg_part))
                except:
                    sent_msg_part.append(msg_part)
        for msg_part in sent_msg_part:
            if msg_part != 'endplayermsg' and msg_part != 'endmsg':
                player_info.append(msg_part)
            elif msg_part == 'endmsg':
                break
            else:                        
                final_positions[player_info[0]] = [player_info[1],player_info[2],player_info[3],player_info[4]]
                player_info = []
                
        self.sock.sendto('received_all_positions')
        
        return final_positions      
        self.sock.close()
        
        
    def purgepositions(self):
        self.sock.sendto('purge_player_positions')
        self.sock.close()
