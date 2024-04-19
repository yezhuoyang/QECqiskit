# This is the python file for testing
from qiskit.circuit.library.standard_gates import HGate
from QECCode import QECCode
from noise import construct_bitflip_noise_model, construct_phaseflip_noise_model
from Surface.surface import surfacecode



if __name__ == '__main__':
    suface_code=surfacecode(25)
    
    suface_code.add_error(0,0)
    
    suface_code.add_error(3,3)
    
    suface_code.display_qubit_layout()