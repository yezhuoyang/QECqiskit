import numpy as np


class TannerGraph:

    def __init__(self,qubitnum:int,stabilizernum:int,xchecknum:int,zchecknum:int):
        self._xchecknum=xchecknum
        self._zchecknum=zchecknum
        self._qubitnum=qubitnum
        self._stabilizernum=stabilizernum
        self._codedistance=0
        self._numlogical=0
        self._Hmatrix=np.zeros((stabilizernum,qubitnum))
        pass


    # Check whether the
    def check_commute(self):
        pass


    def logical_qubit_num(self):
        pass


    def code_distance(self):
        pass


    def add_xcheck(self,qubitindex:int,xcheckindex:int):
        pass

    def add_zcheck(self,qubitindex:int,xcheckindex:int):
        pass

    def print_Hmatrix(self):
        pass
