from random import randint


class ArraysCore:
    def __init__(self):
        self.rang=0
        self.col=0
        self.row=0
        pass
    def createAnArray(self,dimension,rang):
        matrix=[]
        if(dimension>1):
            self.rang=rang
            self.col=self.rang[1]
            self.row=self.rang[0]
            for x in range(self.row):
                matrixRow = []
                for i in range(self.col):
                    matrixRow.append(randint(0, 10))
                matrix.append(matrixRow)
        else:
            self.rang=rang
            for i in range(self.rang):
                matrix.append(randint(0,10))
        return matrix
    def getDimension(self,arr):
        r=0
        c=0
        for i in range(len(arr)):
            r=r+1
            c=0
            for j in range(len(arr[i])):
                c=c+1
        dimension=[r,c]
        return dimension
    def insertAnElement(self,location,arr,data):
        if(arr.ndim>1 and location.ndim>1):
            pass
        return 1