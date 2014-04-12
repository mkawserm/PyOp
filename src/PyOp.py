"""
 * Library : PyOp
 * Author : Kawser
 * Website : http://kawser.org
 * Git : https://github.com/mkawserm
 *
 * Date : 11/04/2014
 * Time : 11:47 PM
 *
 * Objects : PyOp,Rational
 * Objective :Perform advanced mathematical operation using Python
 *
"""






import math
import random
from Queue import Queue







###########################################################

class PyOp(object):
    def __init__(self,*kwards,**kwargs):
        self.__prime__data__() #initilize our pre calculated prime data


    def findDivisors(self,n):
        if self.isPrime(n):
            return [1,n]
        else:
            factors = [1,n]
            for x in xrange(2 , int( math.sqrt(n) )+1 ):
                if (n%x) == 0:
                    factors.append(x)
                    factors.append(n/x)
            return factors
    
    def findPrimeFactors(self,n):
        return self.factor(n)

    
    def findXGCD(self,a,b):
        x = 0
        y = 1
        lastx =  1
        lasty = 0
        while b != 0:
            temp = b
            quotient = int(math.floor(a / b))
            b = a % b
            a = temp
            temp = x
            x = lastx -quotient*x
            lastx = temp
            temp = y
            y = lasty-quotient*y
            lasty = temp
        return [lastx,lasty]

    
    def findGCD(self,a,b):
        while b!=0:
            t = b
            b = a%b
            a = t
        return a
    
    def findLCM(self,a,b):
        return abs(a*b)/self.findGCD(a, b)
    
        
    def isPrime(self,n):
        if n <= 1 :
            return False
        elif n==2:
            return True
        
        #check if n in pre calculated prime data
        if n in self.__prime_list:
            return True
        
        #prime search algorithm
        for x in xrange(2 , int( math.sqrt(n) )+1 ):
            if (n%x) == 0:
                return False
        return True




    def rabin_miller(self,p):
        if(p<2):
            return False
        if(p!=2 and p%2==0):
            return False
        s=p-1
        while(s%2==0):
            s>>=1
        for i in xrange(10):
            a=random.randrange(p-1)+1
            temp=s
            mod=pow(a,temp,p)
            while(temp!=p-1 and mod!=1 and mod!=p-1):
                mod=(mod*mod)%p
                temp=temp*2
            if(mod!=p-1 and temp%2==0):
                return False
        return True    
    
    
    def brent(self,n):
        if(n%2==0):
            return 2;
        x,c,m=random.randrange(0,n),random.randrange(1,n),random.randrange(1,n)
        y,r,q=x,1,1
        g,ys=0,0
        while(True):
            x=y
            for i in range(r):
                y,k=(y*y+c)%n,0
            while(True):
                ys=y
                for i in range(min(m,r-k)):
                    y,q=(y*y+c)%n,q*abs(x-y)%n
                g,k=self.findGCD(q,n),k+m
                if(k>= r or g>1):break
                r=2*r
                if(g>1):break
        if(g==n):
            while(True):
                ys , g = (x*x+c)%n , self.findGCD( abs(x-ys) , n )
                if g>1:
                    break
        return g
    
    def pollard(self,n):
        if(n%2==0):
            return 2;
        x=random.randrange(2,1000000)
        c=random.randrange(2,1000000)
        y=x
        d=1
        while(d==1):
            x=(x*x+c)%n
            y=(y*y+c)%n
            y=(y*y+c)%n
            d=self.findGCD(x-y,n)
            if(d==n):
                break;
        return d
    
    def factor(self,n):
        Q_1=Queue()
        Q_2=[]
        Q_1.put(n)
        while(not Q_1.empty()):
            l=Q_1.get()
            if(self.rabin_miller(l)):
                Q_2.append(l)
                continue
            d=self.pollard(l)
            if(d==l):Q_1.put(l)
            else:
                Q_1.put(d)
                Q_1.put(l/d)
        return Q_2
    
    
    
    


    ###data initilizer method is here###
    def __prime__data__(self):
        """store all pre calculated prime data 2-3727"""
        self.__prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
                             47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
                             107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
                             167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
                             229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
                             283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353,
                             359, 367, 373, 379, 383, 389, 397, 401, 409, 419, 421,
                             431, 433, 439, 443, 449, 457, 461, 463, 467, 479, 487,
                             491, 499, 503, 509, 521, 523, 541, 547, 557, 563, 569,
                             571, 577, 587, 593, 599, 601, 607, 613, 617, 619, 631,
                             641, 643, 647, 653, 659, 661, 673, 677, 683, 691, 701,
                             709, 719, 727, 733, 739, 743, 751, 757, 761, 769, 773,
                             787, 797, 809, 811, 821, 823, 827, 829, 839, 853, 857,
                             859, 863, 877, 881, 883, 887, 907, 911, 919, 929, 937,
                             941, 947, 953, 967, 971, 977, 983, 991, 997, 1009, 1013,
                             1019, 1021, 1031, 1033, 1039, 1049, 1051, 1061, 1063, 1069,
                             1087, 1091, 1093, 1097, 1103, 1109, 1117, 1123, 1129, 1151,
                             1153, 1163, 1171, 1181, 1187, 1193, 1201, 1213, 1217, 1223,
                             1229, 1231, 1237, 1249, 1259, 1277, 1279, 1283, 1289, 1291,
                             1297, 1301, 1303, 1307, 1319, 1321, 1327, 1361, 1367, 1373,
                             1381, 1399, 1409, 1423, 1427, 1429, 1433, 1439, 1447, 1451,
                             1453, 1459, 1471, 1481, 1483, 1487, 1489, 1493, 1499, 1511,
                             1523, 1531, 1543, 1549, 1553, 1559, 1567, 1571, 1579, 1583,
                             1597, 1601, 1607, 1609, 1613, 1619, 1621, 1627, 1637, 1657,
                             1663, 1667, 1669, 1693, 1697, 1699, 1709, 1721, 1723, 1733,
                             1741, 1747, 1753, 1759, 1777, 1783, 1787, 1789, 1801, 1811,
                             1823, 1831, 1847, 1861, 1867, 1871, 1873, 1877, 1879, 1889,
                             1901, 1907, 1913, 1931, 1933, 1949, 1951, 1973, 1979, 1987,
                             1993, 1997, 1999, 2003, 2011, 2017, 2027, 2029, 2039, 2053,
                             2063, 2069, 2081, 2083, 2087, 2089, 2099, 2111, 2113, 2129,
                             2131, 2137, 2141, 2143, 2153, 2161, 2179, 2203, 2207, 2213,
                             2221, 2237, 2239, 2243, 2251, 2267, 2269, 2273, 2281, 2287,
                             2293, 2297, 2309, 2311, 2333, 2339, 2341, 2347, 2351, 2357,
                             2371, 2377, 2381, 2383, 2389, 2393, 2399, 2411, 2417, 2423,
                             2437, 2441, 2447, 2459, 2467, 2473, 2477, 2503, 2521, 2531,
                             2539, 2543, 2549, 2551, 2557, 2579, 2591, 2593, 2609, 2617,
                             2621, 2633, 2647, 2657, 2659, 2663, 2671, 2677, 2683, 2687,
                             2689, 2693, 2699, 2707, 2711, 2713, 2719, 2729, 2731, 2741,
                             2749, 2753, 2767, 2777, 2789, 2791, 2797, 2801, 2803, 2819,
                             2833, 2837, 2843, 2851, 2857, 2861, 2879, 2887, 2897, 2903,
                             2909, 2917, 2927, 2939, 2953, 2957, 2963, 2969, 2971, 2999,
                             3001, 3011, 3019, 3023, 3037, 3041, 3049, 3061, 3067, 3079,
                             3083, 3089, 3109, 3119, 3121, 3137, 3163, 3167, 3169, 3181,
                             3187, 3191, 3203, 3209, 3217, 3221, 3229, 3251, 3253, 3257,
                             3259, 3271, 3299, 3301, 3307, 3313, 3319, 3323, 3329, 3331,
                             3343, 3347, 3359, 3361, 3371, 3373, 3389, 3391, 3407, 3413,
                             3433, 3449, 3457, 3461, 3463, 3467, 3469, 3491, 3499, 3511,
                             3517, 3527, 3529, 3533, 3539, 3541, 3547, 3557, 3559, 3571,
                             3581, 3583, 3593, 3607, 3613, 3617, 3623, 3631, 3637, 3643,
                             3659, 3671, 3673, 3677, 3691, 3697, 3701, 3709, 3719, 3727]
        #################################################################################
############################################################################################







class Rational(object):
    """Representation of rational number"""
    def __init__( self, top = 1, bottom = 1 ):
        """Initializes Rational instance""" 
        # do not allow 0 denominator 21
        self.numerator = 1
        self.denominator = 1
        self.sign = 1
        
        if type(top) == str:
            top = float(top)
        if type(bottom) == str:
            bottom = float(bottom)
        
        if float(int(top)) == top:
            top = int(top)
        if float( int(bottom) ) == bottom:
            bottom = int(bottom)
        

        #print bottom
        if bottom == 0:
            raise ZeroDivisionError, "Cannot have 0 denominator"
        # assign attribute values
        
        if type(top) == type(0.0) and type(bottom) == type(0.0):
            if top>1:p,q = self.pbyq( top % int(top) )
            else:p,q = self.pbyq( top )
            
            rtop = Rational( int(top) ) + Rational(p,q)
            
            if bottom>1:p,q = self.pbyq( bottom % int(bottom) )
            else:p,q = self.pbyq( bottom )
            
            rbottom = Rational( int(bottom) ) + Rational(p,q)
            r = rtop / rbottom
            
            self.numerator = r.getNumerator()
            self.denominator = r.getDenominator()
            self.sign = r.sign
            
        elif type(top) == type(0.0) and type(bottom) == type(0):
            
            if top>1:p,q = self.pbyq( top % int(top) )
            else:p,q = self.pbyq( top )
                
            rtop = Rational( int(top) ) + Rational(p,q)
            rbottom = Rational( bottom, 1 )
            r = rtop / rbottom
            
            self.numerator = r.getNumerator()
            self.denominator = r.getDenominator()
            self.sign = r.sign
            
        elif type(top) == type(0) and type(bottom) == type(0.0):
            rtop = Rational( top )
            
            if bottom>1:p,q = self.pbyq( bottom % int(bottom) )
            else:p,q = self.pbyq( bottom )
                
            rbottom = Rational( int(bottom) ) + Rational(p,q)
            
            r = rtop / rbottom
            
            self.numerator = r.getNumerator()
            self.denominator = r.getDenominator()
            self.sign = r.sign
            
        elif type(top) == type(0) and type(bottom) == type(0):
            self.numerator = abs( top )
            self.denominator = abs( bottom )
            
            if self.numerator*self.denominator!=0:
                self.sign = ( top * bottom ) / ( self.numerator * self.denominator )
            else:
                self.sign = 1
        
            
            
        

        self.simplify()  # Rational represented in reduced form 
    
    
    def gcd(self, x, y ):
        """Computes greatest common divisor of two values"""
        while y:
            z = x
            x = y
            y = z % y
        return x
    
    def pbyq(self,n):
        if int(n) == 0:
            n = float(str(n))
            multiplier = 10
            while True:
                temp = n*multiplier
                if temp == float( (int(temp)) ) :
                    return (int(temp),multiplier)
                multiplier = multiplier*10
        else:
            return None
            
    def getNumerator(self):
        return self.numerator
    def getDenominator(self):
        return self.denominator
    
    # class interface method
    def simplify( self ):
        """Simplifies a Rational number""" 
        common = self.gcd( self.numerator, self.denominator )
        self.numerator /= common
        self.denominator /= common
    
    #overloaded unary operator
    def __neg__( self ):
        """Overloaded negation operator"""
        return Rational( -self.sign * self.numerator,self.denominator )
    
    # overloaded binary arithmetic operators
    def __add__( self, other ):
        """Overloaded addition operator"""
        return Rational(
                        self.sign * self.numerator * other.denominator+
                        other.sign * other.numerator * self.denominator,
                        self.denominator * other.denominator )
    
    def __sub__( self, other ):
        """Overloaded subtraction operator"""
        return self + ( -other )
    
    def __mul__( self, other ):
        """Overloaded multiplication operator""" 
        return Rational(
                        self.numerator * other.numerator,
                        self.sign * self.denominator * other.sign * other.denominator )
        
    def __div__( self, other ):
        """Overloaded / division operator."""
        return Rational(
                        self.numerator * other.denominator,
                        self.sign * self.denominator * other.sign * other.numerator )
    
    def __truediv__( self, other ):
        """Overloaded / division operator. (For use with Python 77      versions (>= 2.2) that contain the // operator)""" 
        return self.__div__( other )
    
    # overloaded binary comparison operators 82
    def __eq__( self, other ):
        """Overloaded equality operator"""
        #print "EQ Called"
        #print "self.-other :",self - other
        return ( self - other ).numerator == 0
    
    def __lt__( self, other ):
        """Overloaded less-than operator"""
        return ( self - other ).sign < 0
    
    def __gt__( self, other ):
        """Overloaded greater-than operator"""
        return ( self - other ).sign > 0
    
    def __le__( self, other ):
        """Overloaded less-than or equal-to operator"""
        return ( self < other ) or ( self == other )
    
    def __ge__( self, other ):
        """Overloaded greater-than or equal-to operator"""
        return ( self > other ) or ( self == other )
    
    def __ne__( self, other ):
        """Overloaded inequality operator"""
        return not ( self == other )
    
    # overloaded built-in functions
    def __abs__( self ):
        """Overloaded built-in function abs"""
        return Rational( self.numerator, self.denominator )
    
    def __str__( self ):
        """String representation"""
        # determine sign display
        if self.sign == -1:
            signString = "-"
        else:
            signString = ""
        if self.numerator == 0:
            return "0"
        elif self.denominator == 1:
            return "%s%d" % ( signString, self.numerator )
        else:
            return "%s%d/%d" %( signString, self.numerator, self.denominator )
    # overloaded coercion capability
    def __int__( self ):
        """Overloaded integer representation"""
        return self.sign * divmod( self.numerator,self.denominator )[ 0 ]
    
    def __float__( self ):
        """Overloaded floating-point representation"""
        return self.sign * float( self.numerator ) / self.denominator
    
    def __coerce__( self, other ):
        """Overloaded coercion. Can only coerce int to Rational"""
        if type( other ) == type( 1 ):
            return ( self, Rational( other ) )
        else:
            return None





if __name__ == '__main__':
    
    print "Testing Rational object"
    r1 = Rational(10,12)
    r2 = Rational(99,5)
    print "r1=",r1," r2=",r2
    print "r1+r2 : ",r1+r2
    print "r1-r2 : ",r1-r2
    print "r1/r2 : ",r1/r2
    print "r1*r2 : ",r1*r2
    
    
    print 
    print "Testing PyOp object"
    
    p = PyOp()
    print "p.isPrime(10) : ",p.isPrime(10)
    print "p.isPrime(2147483647) : ",p.isPrime(2147483647)
    print "p.findPrimeFactors(135) : ",p.findPrimeFactors(135)
    print "p.findDivisors(135) : ",p.findDivisors(135)
    print "p.findGCD(5,20) : ", p.findGCD(5,20)
    print "p.findLCM(10,20) : ", p.findLCM(10,20) 