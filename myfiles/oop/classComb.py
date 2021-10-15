class calcComb:

    def __init__(self,stringa):
        
        self.__stringa = stringa
        self.stringalist = list(stringa)

    def getStringa(self):
        return self.__stringa

    def getStringalist(self):
        return self.stringalist

    def setStringa(self, str):
        self.__stringa = str
        self.stringalist = list(str)

    def permutazioni(self, k):
        return len(self.__stringa)**k

    #def posizioni(self,k):
    
    def permutazioni3(self, k, p):      #metodo che fa pare della calcomb
        return len(self.__stringa)**k 

        return len(self.__stringa)**p


primiDieciNumeri=calcComb("abcdefghil")
print(primiDieciNumeri.permutazioni3(3,4))


