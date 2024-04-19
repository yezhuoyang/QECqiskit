#The class function of surface code


from QECCode import QECCode
from colorama import init as colorama_init
from colorama import Fore
from colorama import Style



class surfacecode(QECCode):
    
    def __init__(self, physical_qubits: int):
        
        distance=int(physical_qubits**0.5)
        super().__init__(physical_qubits,0,distance)
        
        stabilizerlist=[]

        #TODO: Add stabilizer for surface code


        self.set_stabilizers(stabilizerlist)
        self._onlybitflip=True
        self._onlyphaseflip=False
        
        
    
    def display_qubit_layout(self):
        colorama_init()
        for row in range(0,self._distance):
            #print("row{}".format(row),end="\n")
            for col in range(0,self._distance):
                print('O({},{})'.format(row,col),end='')
                if col==self._distance-1:
                    continue
                if row%2==0:
                    print(f'{Fore.GREEN}--Z--{Style.RESET_ALL}',end='')
                else:
                    print(f'{Fore.YELLOW}--X--{Style.RESET_ALL}',end='')
            print('\n')
            
            if row==self._distance-1:
                continue
            for col in range(0,self._distance):
                if col%2==0:
                    print(f'{Fore.YELLOW}  |   {Style.RESET_ALL}'.format(row,col),end='')
                else:
                    print(f'{Fore.GREEN}  |   {Style.RESET_ALL}'.format(row,col),end='')
                print('     ',end='')               
            print('\n')
            
            for col in range(0,self._distance):
                if col%2==0:
                    print(f'{Fore.YELLOW}  X   {Style.RESET_ALL}'.format(row,col),end='')
                else:
                    print(f'{Fore.GREEN}  Z   {Style.RESET_ALL}'.format(row,col),end='')
                print('     ',end='')               
            print('\n')            
            
            for col in range(0,self._distance):
                if col%2==0:
                    print(f'{Fore.YELLOW}  |   {Style.RESET_ALL}'.format(row,col),end='')
                else:
                    print(f'{Fore.GREEN}  |   {Style.RESET_ALL}'.format(row,col),end='')
                print('     ',end='')               
            print('\n')
        
        
            
    
    
        
        
        
    def surface_stabilizer():
        pass
        
    