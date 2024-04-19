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
        self._error_list=[]
        
        
    def add_error(self,row,col):
        self._error_list.append((row,col))
    
    
    def display_qubit_layout(self):
        colorama_init()
        qubitindex=0
        for row in range(0,self._distance):
            #print("row{}".format(row),end="\n")
            for col in range(0,self._distance):
                if (row,col) in self._error_list:
                    print(f'{Fore.RED}O({row},{col}){Style.RESET_ALL}',end='')
                else:
                    print('O({},{})'.format(row,col),end='')
                if col==self._distance-1:
                    continue
                if row%2==0:
                    if qubitindex>=10:
                        print(f'{Fore.GREEN}--Z{qubitindex}--{Style.RESET_ALL}',end='')
                    else:
                        print(f'{Fore.GREEN}--Z{qubitindex} --{Style.RESET_ALL}',end='')
                    qubitindex+=1
                else:
                    if qubitindex>=10:
                        print(f'{Fore.YELLOW}--X{qubitindex}--{Style.RESET_ALL}',end='')
                    else:
                        print(f'{Fore.YELLOW}--X{qubitindex} --{Style.RESET_ALL}',end='')
                    qubitindex+=1
            print('\n')
            
            if row==self._distance-1:
                continue
            for col in range(0,self._distance):
                if col%2==0:
                    print(f'{Fore.YELLOW}  |     {Style.RESET_ALL}'.format(row,col),end='')
                else:
                    print(f'{Fore.GREEN}  |     {Style.RESET_ALL}'.format(row,col),end='')
                print('     ',end='')               
            print('\n')
            
            for col in range(0,self._distance):
                if col%2==0:
                    if qubitindex>=10:
                        print(f'{Fore.YELLOW}  X{qubitindex}   {Style.RESET_ALL}'.format(row,col),end='')
                    else:
                        print(f'{Fore.YELLOW}  X{qubitindex}    {Style.RESET_ALL}'.format(row,col),end='')
                    qubitindex+=1
                else:
                    if qubitindex>=10:
                        print(f'{Fore.GREEN}  Z{qubitindex}   {Style.RESET_ALL}'.format(row,col),end='')
                    else:
                        print(f'{Fore.GREEN}  Z{qubitindex}    {Style.RESET_ALL}'.format(row,col),end='')
                    qubitindex+=1
                print('     ',end='')               
            print('\n')            
            
            for col in range(0,self._distance):
                if col%2==0:
                    print(f'{Fore.YELLOW}  |     {Style.RESET_ALL}'.format(row,col),end='')
                else:
                    print(f'{Fore.GREEN}  |     {Style.RESET_ALL}'.format(row,col),end='')
                print('     ',end='')               
            print('\n')
        
        
        
    def surface_stabilizer():
        
        
        pass
        
    