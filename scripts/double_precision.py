'''
References:

https://www.wikihow.com/Convert-a-Number-from-Decimal-to-IEEE-754-Floating-Point-Representation
https://babbage.cs.qc.cuny.edu/IEEE-754.old/Decimal.html
https://class.ece.iastate.edu/arun/Cpre305/ieee754/ie4.html
https://class.ece.iastate.edu/arun/CprE281_F05/ieee754/ie5.html
'''

from mpmath import mp
import argparse
import math
import re
import os
os.system('clear')

# =============================================================================
# ================================ Begin Class ================================
# =============================================================================

class DoublePrecision():
    # ------------------------------------------- Variables
    __myargs = argparse.Namespace
    __inputNum = float
    __spSign = str
    __dpSign = str
    __binaryPrecision = int
    __wholeNum = int
    __decNum = float
    __wholeNumBin = str
    __decNumBin = str
    
    # ------------------------------------------- Functions
    # constructor
    def __init__(self):
        self.__myargs = argparse.Namespace
        self.__binaryPrecision = 64
        self.__inputNum = 0.0
        self.__spSign = ''
        self.__dpSign = ''
        self.__wholeNum = 0
        self.__decNum = 0.0
        self.__wholeNumBin = '0b'
        self.__decNumBin = '0b'
    
    
    # setup arguments for class
    def setArguments(self):
        # ---------- set arguments for class IEEE754DFPU
        parser = argparse.ArgumentParser(prog='IEEE-754 Double Floating Point Unit',
                                        usage='%(prog)s [options] path',
                                        description='IEEE-754 double precision hexadecimal floating point unit generator',
                                        epilog='Happy trigonometry :)')
        # ---------- list of all possible args for Double Precision
        parser.add_argument('-num','--inputvalue',
                        type=float,default=0,metavar='',required=False,nargs='?',help='Input user defined decimal value')
        parser.add_argument('-sign','--signbit',
                            type=int,default=0,metavar='',required=False,help='Include sign bit in hex num')
        parser.add_argument('-v','--verbose',
                            type=int,default=0,metavar='',required=False,nargs='?',help='print verbose')
        parser.add_argument('-d','--debug',
                            type=int,default=0,metavar='',required=False,nargs='?',help='print debugging')
        self.__myargs = parser.parse_args()
    
    
    # determine sign of the number and display in binary format
    def getSign(self):
        if self.__inputNum >= 0:    
            self.__spSign = '0'
            self.__dpSign = '0'
            # print verbosity
            if self.__myargs.verbose:
                print('{:^5s}---- {:<21s}{:<5s}'.format(' ','Sign bit = ',"1'b0"))
        else:
            self.__spSign = '1'
            self.__dpSign = '1'
            # print verbosity
            if self.__myargs.verbose:
                print('{:^5s}---- {:<21s}{:<5s}'.format(' ','Sign bit = ',"1'b1"))
    
    
    # split input number into whole and dec
    def splitInputNum(self,number):
        # ---------- set decimal places and precision
        mp.prec = self.__binaryPrecision
        # ---------- get num as arg or input
        if self.__myargs.inputvalue:
            self.__inputNum = mp.mpf(self.__myargs.inputvalue)
        else:
            self.__inputNum = mp.mpf(number)
        print('Input Number:   {0} (10)'.format(self.__inputNum))
        # ---------- split input num
        if self.__inputNum >= 1.0:
            self.__decNum, self.__wholeNum = math.modf(self.__inputNum)
            self.__wholeNum = int(self.__wholeNum)
            self.__decNum = mp.mpf(self.__decNum)
        else:
            self.__wholeNum = 0
            self.__decNum = mp.mpf(self.__inputNum)
        # ---------- print debugging
        if self.__myargs.verbose:
            print('{:<5s}---- Whole num = [{:d}] Decimal num = [{:}]'
                .format(' ',self.__wholeNum,self.__decNum))
            print('{:<5s}---- Binary Precision = {:<2d} Decimal Places = {:<2d}'
                .format(' ',mp.prec,mp.dps))
    
    
    # convert bin num to base 2 scientific notation
    def base2Scientific(self):
        pass
    
    
    # convert the input num to binary
    def wholeNum2Bin(self):
        if self.__wholeNum > 0:
            self.__wholeNumBin = bin(self.__wholeNum)
        else:
            self.__wholeNumBin = '0b0'
        # ---------- print verbosity
        if self.__myargs.verbose:
            print('{:^5s}---- {:<10d} (10) ---> {:<10s} (2)'.format(' ',self.__wholeNum,self.__wholeNumBin))
    
    
    # convert dec num to bin
    def decNum2Bin(self):
        tempFloat = self.__decNum
        decNumLen = len(str(tempFloat)) - len(str(self.__wholeNum)) - 1
        for i in range(-1,-abs(decNumLen),-1):
            #tempFloat = tempFloat * pow(2,-1 * i)
            print(i)




# =============================================================================
# ================================= End Class =================================
# =============================================================================

def main():
    
    
    obj1 = DoublePrecision()
    obj1.setArguments()
    #obj1.splitInputNum(number=math.pi)
    obj1.splitInputNum(number=math.sin(math.radians(1)))
    obj1.getSign()
    obj1.wholeNum2Bin()
    obj1.decNum2Bin()
    #for i in range(0,91,1):
    #    # val = Decimal(math.sin(math.radians(i)))
    #    print('Input({:^2d}) ----> {:<60f} {:>3d}'.format(i,val,len(str(val))))

if __name__ == '__main__':
    main()
