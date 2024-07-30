class Rational:

    def __init__(self,n=0,d=0):
        self.n=n
        self.d=d

    def __str__(self):
        mstr= " "
        mstr+=str(self.n)
        mstr+="/"
        mstr+=str(self.d)
        mstr+= " "
        return mstr

    def simplification(self):
        count=1
        if int(self.n) > int(self.d):
            i=int(self.n)
        if int(self.n) < int(self.d):
            i=int(self.d)
        ans=0
        while count<=i:
            if int(self.n)%count==0 and int(self.d)%count==0:
                ans=count
            count+=1
        self.n=int(self.n) // ans
        self.d=int(self.d) // ans
        return self

    def equal(r1,r2):
        if r1.n==r2.n and r1.d==r2.d:
            return True
        else:
            return False
    staticmethod(equal)

    def reciprocal(r1):
        r1.n,r1.d = r1.d,r1.n
        return r1
    staticmethod(reciprocal)

    def absolute(r1):
        x=-(int(r1.n)/int(r1.d))
        return x

    def to_convert(type,r1):
        if str(type) == 'integer':
            return int(r1.n) // int(r1.d)
        if str(type) == 'float':
            return int(r1.n) /  int(r1.d)
    staticmethod(to_convert)

    def from_convert(type,number):
        if str(type) == 'integer':
            return f"{number} / 1"
        if str(type) == 'float':
            number=str(number)
            n=number.split('.')
            lenght=n[1]
            m=n[0];m+=n[1]
            return f"{n}/{10**lenght}"
    staticmethod(from_convert)

    def power(r1,power):
        r1.n=int(r1.n)**power
        r1.d=int(r1.d)**power
        return r1
    staticmethod(power)

    def arithmetic_oper(operation,r1,number):
        if str(operation) == '+':
            r1.n=str(int(r1.n)+number)
            return r1
        elif str(operation) == '-':
            r1.n=int(r1.n)-number
            return r1
        elif str(operation) == '*':
            r1.n=int(r1.n)*number
            return r1
        elif str(operation) == '/':
            r1.d=int(r1.d)*number
            return r1
    staticmethod(arithmetic_oper)

    def rational_oper(operation,r1,r2):
        if str(operation) == '+':
            r1.n=int(r1.n)+int(r2.n)
            r1.d=int(r1.d)*int(r2.d)
            return r1
        elif str(operation) == '-':
            r1.n=int(r1.n)-int(r2.n)
            r1.d=int(r1.d)*int(r1.d)
            return r1
        elif str(operation) == '*':
            r1.n=int(r1.n)*int(r2.n)
            r1.d=int(r1.d)*int(r1.d)
            return r1
        elif str(operation) == '/':
            r1.n=int(r1.n)*int(r2.d)
            r1.d=int(r1.d)*int(r1.n)
            return r1
    staticmethod(rational_oper)
    def additive_inv(r1):
        return 0

    def multiplicative_inv(r1):
        return 1

    def compare(type1,type2,r1,r2):
        if str(type1)=='Rational' and str(type2)=='integer':
            if int(r1.n) // int(r1.d) > int(r2):
                return "Greater"
            elif int(r1.n) // int(r1.d) < int(r2):
                return "Lesser"
            else:
                return "Equal"
        if str(type1)=='Rational' and str(type2)=='float':
            if int(r1.n)/int(r1.d)>int(r2):
                return "Greater"
            elif int(r1.n)/int(r1.d)<int(r2):
                return "Lesser"
            else:
                return "Equal"
        if str(type1)=="Rational" and str(type2)=="string":
            if int(r1)==int(r2):
                return "Equal"
            else:
                return "Unequal"
    staticmethod(compare)

    def get_rat_numeriator(r1):
        return r1.n
    def get_rat_denominator(r1):
        return r1.d

    def set_rat_numeriator(r1,x):
        x=r1.n
        return r1
    def set_rat_denominator(r1,y):
        y=r1.d
        return r1
    staticmethod(set_rat_denominator)


def main():

    rat_1=Rational(-2,4)
    rat_2=Rational(4,8)

    h=rat_1.simplification()
    print(f"simplification of rat num is : {h}")

    a=Rational.equal(rat_1,rat_2)
    print(f"eqvilance : {a}")

    s=rat_2.reciprocal()
    print(f"reciprocal is : {s}")

    r=rat_1.absolute()
    print(f"absolute of rat num is : {r}")

    s=Rational.to_convert("integer",rat_2)
    print(f"to convrt int and float : {s}")

    a=Rational.from_convert("integer",5)
    print(f"from conversion is : {a}")

    n=Rational.power(rat_1,2)
    print(f"power of rat num is : {n}")

    a=Rational.arithmetic_oper('/' , rat_2 , 2)
    print(f"arithmetic_oper on rat num is : {a}")

    l=Rational.rational_oper('-',rat_1,rat_2)
    print(f"rational oper is : {l}")

    d=rat_1.additive_inv()
    print(f"additive_inv is : {d}")

    e=rat_2.multiplicative_inv()
    print(f"multiplicative_inv is : {e}")

    x=Rational.compare("Rational","integer",rat_1,"3")
    print(f"comparsion of rat num is : {x}")

    z=Rational.get_rat_numeriator(rat_1)
    print(f"get rat num numeriator is : {z}")

    j=Rational.get_rat_denominator(rat_1)
    print(f"get rat num denominator is : {j}")

    k=Rational.set_rat_numeriator(rat_2,2)
    print(f"set rat num numeriator is : {k}")

    g=Rational.set_rat_denominator(rat_1,4)
    print(f"set rat num denominator is : {g}")



main()
