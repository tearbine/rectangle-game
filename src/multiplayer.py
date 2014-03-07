import socket, re
from thing import Thing
from player import Player

class Client:
    def __init__(self, server_ip, port):
        self.server_ip = server_ip
        self.port = port
        
    def sendpositions(self, player, coord1, coord2, width, height):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.server_ip, self.port))
        
        sock.send('sending_player_positions ')

        
        for msg_part in [player,coord1,coord2,width,height]:
            sock.send(str(msg_part) + ' ')
        
        sock.send('endmsg ')
            
        sock.close()
    def recvpositions(self):     
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.server_ip, self.port))
        final_positions = {}
        sock.send('receiving_player_positions endmsg')

        c_sent_msg_part = 'placeholder_string'
        sent_msg_part = []
        player_info = []
        
        while 'endmsg' not in c_sent_msg_part and c_sent_msg_part != []:
            c_sent_msg_part = sock.recv(16384).split()
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
        
        return final_positions      
        sock.close()
        
        
    def purgepositions(self):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.connect((self.server_ip, self.port))
        sock.send('purge_player_positions')
        sock.close()

'''client = Client()
player = Player('playertestclient',10,10)
player2 = Player('playertestclient2',20,20)
client.sendpositions(player, player.rect.x, player.rect.y, player.rect.height, player.rect.width)
client.sendpositions(player2, player2.rect.x, player2.rect.y, player2.rect.height, player2.rect.width)
print 'hello'
player_positions = client.recvpositions()
print 'bye', player_positions'''