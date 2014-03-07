from tiles import Tiles
class Levels:
    def load_level1(self, environment, player):
        tiles_list = {}
        environment_add_list = {}
        players = []
         
        tiles_list[300,30] = [(900,400), (1300,400)]
        tiles_list[60,30]  = [(-20,40)]
        tiles_list[30,400] = [(0,100), (400,100)]
        tiles_list[200,200] = [(600,500)]
        players.append(player)
        
        for tiles in tiles_list:
            for tile in tiles_list[tiles]:
                environment_add_list[Tiles(tiles[0],tiles[1])] = [tile[0],tile[1]]
        print environment_add_list
        
        for tile in environment_add_list:
            environment.add(tile, (environment_add_list[tile]))
        
        environment.add(player, (0,0))
    def load_level2(self, environment, player):
        tiles_list = {}
        environment_add_list = {}
        players = []
         
        tiles_list[200,30]  = [(-100,30),(100,-120),(300,-270),(500,-420),(700,-570)]
        tiles_list[30,30]   = [(100,30),(300,-120),(500,-270),(700,-420),(900,-570)]
        tiles_list[30,3000] = [(-100,-2970)]
        tiles_list[30,150]  = [(100,-120),(300,-270),(500,-420),(700,-570)]
        tiles_list[30,300]  = [(900,-870)]

        players.append(player)
        
        for tiles in tiles_list:
            for tile in tiles_list[tiles]:
                environment_add_list[Tiles(tiles[0],tiles[1])] = [tile[0],tile[1]]
        print environment_add_list
        
        for tile in environment_add_list:
            environment.add(tile, (environment_add_list[tile]))
        
        environment.add(player, (0,0))    
        
        