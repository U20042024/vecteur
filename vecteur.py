import math
#la_classe_mere
class vecteur2D() :
    _nbV = 0
    def __init__(self, X, Y) :
        self.__X = X
        self.__Y = Y
        vecteur2D._nbV = vecteur2D._nbV + 1

#getters_and_setters
    def getX(self) :
        return self.__X        
    
    def getY(self) :
        return self.__Y

    def setX(self, X) :
        self.__X = X

    def setY(self, Y) :
        self.__Y = Y
    
    def getnbV(self) :
        return vecteur2D._nbV
    
#methodes
    def ToString(self) :
        return ("X = ", self.getX(), "Y = ", self.getY()) 
    
    def Equals(self, V2) :
        X1, Y1 = self.getX(), self.getY()
        X2, Y2 = V2.getX(), V2.getY()
        if X1 == X2 and Y1 == Y2 :
            return True
        else :
            return False
        
    def norme(self) :
        return math.sqrt(self.getX() ** 2 + self.getY() ** 2)

#subclass
class vecteur3D(vecteur2D) :
    def __init__(self, X, Y, Z):
        vecteur2D.__init__(self, X, Y)
        self._Z = Z

#getters and setters
    def getZ(self) :
        return self._Z
    
    def setZ(self, Z) :
        self.__Z = Z

#methodes
    def ToString(self):
        return vecteur2D.ToString(), "Z = ", self.getZ()
    
    def Equals(self, V3) :
        vecteur2D().Equals()
        Z1 = self.getZ()
        Z2 = V3.getZ()
        if Z1 == Z2 :
            return True
        else :
            return False
        
    def norme(self) :
        returnvecteur2D().norme() + math.sqrt(self.getZ() ** 2)