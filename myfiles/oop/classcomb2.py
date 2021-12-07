from itertools import permutations

# classe calcolo combinatorio

def anagrammi(lettere):
#generiamo tutte le possibili permutazioni e le inseriamo in una lista
    permutazioni = list(permutations(lettere))

#inizializiamo una variabile stringa di appoggio e una lista dove salvarle
    temp = ''
    anagrammi = []

    for i in permutazioni:
        for carattere in i:
        # in temp concateno tutti gli elementi della tupla così da
        # ottenere i singoli anagrammi della stringa iniziale
            temp += carattere 

    # aggiungo la parola ricostruita dalla tupla alla lista finale degli anagrammi
        anagrammi.append(temp)
    # "svuoto" la variabile temp così da ricostruire un secondo anagramma
        temp = ''

    print(anagrammi) 

def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact *= num
    return fact

class calcComb():

    def __init__(self, stringa):

        self.__N = len(stringa)
        self.__stringa = stringa
        self.__listStringa = list(stringa)

    def get_stringa(self):
        return self.__stringa

    def get_listStringa(self):
        return self.__listStringa

    def setStringa(self):
        self.__stringa = str.upper()
        self.__listStringa = list(str.upper())    

    def confUtil(self):
        f=open("word.italian.txt")
        if self.__stringa in f:
            return 


    # PERMUTAZIONI

    def nPermutSenzaRip(self):
        n=len(self.__stringa)
        return factorial(n)

    def nPermutConRip(self):
        a=
        n=len(self.__stringa)
        if k+r<=n:
            return (factorial(n))/(factorial(k))


    def permutSenzaRip(self):
        return anagrammi(list(self.__stringa))

    def permutConRip(self):
        '''
        generare e restituire la lista di permutazioni CON ripetizione
        '''
        return 0

    # DISPOSIZIONI

    def nDispSemplSenzaRip(self,k):
        n=len(self.__stringa)
        if k<=n:
            x=factorial(n)
            y=factorial(n-k)
            return (x/y)    

    def nDispSemplConRip(self,k):
        return len(self.__stringa)**k        

    def dispSemplSenzaRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici SENZA ripetizione
        '''
        return 0


    def dispSemplConRip(self):
        '''
        generare e restituire la lista delle disposizioni semplici CON ripetizione
        '''
        return 0

    # COMBINAZIONI

    def nCombSemplSenzaRip(self,k):
        n=len(self.__stringa)
        c= (factorial(n))/(factorial(n-k))
        return c/factorial(k)

    def nCombSemplConRip(self,k):
        n=len(self.__stringa)
        return (factorial(n+k-1))/factorial(k)

    def combSenzaRip(self):
        '''
        generare e restituire la lista delle combinazioni SENZA ripetizione
        '''
        return 0


    def combConRip(self):
        '''
        generare e restituire la lista delle combinazioni CON ripetizione
        '''
        return 0