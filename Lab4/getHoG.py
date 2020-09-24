import numpy as np
import pdb

class HOG:
    def __init__(self,magnitude,angles, cells,cell_size, blocks, bins):
        self.magnitude = magnitude
        self.angles = angles
        self.cells = cells
        self.blocks = blocks
        self.bins = bins
        self.cell_size=cell_size
        #self.Hist=np.zeros((cells,cells,bins),dtype=int)
        
    def compute(self):
        Hist = []
        '''
        Compute HOG here
        
        '''
        if len(Hist)==0:
            print("HOG implementation missing or Input not correct")
            
        
        return Hist

    

            
            
        

