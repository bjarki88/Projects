class Grid:
    POS_X = 'x' #Fasti x fyrir staðsetningu a hnit 
    GRID_O = 'o' #Fasti o býr til hnitakerfið
    START_POS = [0,0] 
    def __init__(self, height=0, width=0):
        self.width = width
        self.height = height
        self.curr_pos = Grid.START_POS
    
    def build_grid(self):
        ''' Býr til hnitakerfið og setur inn staðsetningu á hnitakerfi '''
        if self.width == 0 and self.height == 0:
            self.grid = Grid.POS_X
            return self.grid
        else:
            self.grid = [[Grid.GRID_O for y in range(self.width)] for x in range(self.height)]
            cx, cy = self.curr_pos
            self.grid[cy][cx] = Grid.POS_X
            return self.grid
    
    def current_pos(self): 
        #bætum við +1 á y og x þar sem upphafsstaðsetning 
        #er (0,0) í python en við viljum (1,1)
        x, y = self.curr_pos
        x = x+1
        y = y+1
        return (y, x)
    
    def move_right(self):
        # (self.curr_pos[0] == self.witdh -1) þýðir að við erum lengst til hægri 
        # þá færum við okkur hringin ef við viljum fara til hægri
        if self.curr_pos[0] == self.width -1:
            self.curr_pos[0] = 0
        else:
            self.curr_pos[0] += 1


    def move_left(self):
        # (self.curr_pos[0] == 0) þýðir að við erum lengst til vinstri
        # þá færum við okkur hringin ef við viljum fara til vinstri
        if self.curr_pos[0] == 0:
            self.curr_pos[0] = self.width -1
        else:
            self.curr_pos[0] -= 1

    def move_up(self):
        # (self.curr_pos[1] == 0) þýðir að við erum efst upp
        # þá færum við okkur hringin ef við viljum fara upp
        if self.curr_pos[1] == 0:
            self.curr_pos[1] = self.height -1
        else:
            self.curr_pos[1] -= 1
    
    def move_down(self):
        # (self.curr_pos[1] == self.height -1) þýðir að við erum neðst niðri
        # þá færum við okkur hringin ef við viljum fara niður
        if self.curr_pos[1] == self.height -1:
            self.curr_pos[1] = 0
        else:
            self.curr_pos[1] += 1
    
    def __str__(self):
        return '{}\n'.format('\n'.join(''.join(row) for row in self.build_grid()))


