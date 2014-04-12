"""
 * Module : example_one
 * Author : Kawser
 * Website : http://kawser.org
 * Git : https://github.com/mkawserm
 *
 * Date : 12/04/2014
 * Time : 11:18 PM
 *
 *
 * Objective : We shall calculate resistance (R1 and R2) of a voltage divider using Rational class
 *
 * Input ::  V - Source Volt
 *           V2 - Desired Volt
 *           I2 - Desired current flow in ampere
 * Output :: R1 and R2 resistance in Ohm 
 *
 *
"""


from PyOp import Rational


def calculate_resistance():
    V = Rational( raw_input("Enter input/source voltage (V) : ") )
    
    V2 = Rational( raw_input("Enter output voltage (V2) : ") )
    I2 = Rational( raw_input("Enter output current (I2) : ") )
    R2 = V2/I2
    
    R1 =  ( (V-V2)*R2 )/ V2
    
    V1 = ( R1/(R1+R2) ) * V
    V2 = ( R2/(R1+R2) ) * V
    I1 = V1/R1
    
    
    print "======== Rational Format ==========="
    print "R1 = %s ohm" % R1
    print "I1 =%s amp" %I1
    print "V1 = %s volt" % V1
    
    
    print 
    
    print "R2 = %s ohm" % R2
    print "I2 = %s amp" % I2
    print "V2 = %s volt" % V2
    
    print
    print "======== Floating point format ======="
    print "R1 = %s ohm" % float(R1)
    print "I1 =%s amp" %float(I1)
    print "V1 = %s volt" % float(V1)
    
    
    print 
    
    print "R2 = %s ohm" % float(R2)
    print "I2 = %s amp" % float(I2)
    print "V2 = %s volt" % float(V2)
################################################################################




if __name__=="__main__":
    calculate_resistance()