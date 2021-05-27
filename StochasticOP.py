import random

# [0011010011100000] p = 6/16 0.375

# 01011001 4/8
# 01001101 4/8            1/4    0.25
# AND
# 01001001                 3/8    .375

# 8  %error = (.375 - .25) / .25 * 100 = 50%
# 16 %error = (.3125 - .25) / .25 * 100 = 25%
# 32 %error = (.25 - .25) / .25 * 100 = 0%








#class for creating semi-random stochastic numbers(stochastic numbers of fixed length with a fixed p value, and a randomized location for the binary 1s within the number)
class StocNum:
    BinaryRepresentation = []
    pFrac = 0
    pDec = 0
    nOnes = 0
    nBits = 0
    def __init__(self, numOnes, numBits):
        BinaryRepresentation = [0] * numBits
        oneIndexes = []
        if (numOnes > numBits):
            print("ERROR: Cannot have more ones than the number of bits in this stochastic number!")
        else:
            i = 0
            while i < numOnes:
                newIndex = random.randint(0, numBits - 1)
                if newIndex not in oneIndexes:
                    oneIndexes.append(newIndex)
                    i = i + 1
            for i in oneIndexes:
                BinaryRepresentation[i] = 1
        self.BinaryRepresentation = BinaryRepresentation
        self.pFrac = str(numOnes) + "/" + str(numBits)
        self.pDec = numOnes / numBits
        self.nOnes = numOnes
        self.nBits = numBits
    
    def changeStocNum(self, newArr, newNumOnes, newNumBits):
        self.BinaryRepresentation = newArr
        self.pFrac = str(newNumOnes) + "/" + str(newNumBits)
        self.pDec = newNumOnes / newNumBits
        self.nOnes = newNumOnes
        self.nBits = newNumBits

def ANDer(stocNum1, stocNum2):
    if stocNum1.nBits != stocNum2.nBits:
        print("ERROR: The two stochastic numbers must be of the same length to be ANDed!")
    else:
        newArr = []
        newNumOnes = 0
        for i in range(stocNum1.nBits):
            if (stocNum1.BinaryRepresentation[i] == stocNum2.BinaryRepresentation[i]) and (stocNum1.BinaryRepresentation[i] == 1):
                newArr.append(1)
                newNumOnes += 1
            else:
                newArr.append(0)
        newStocNum = StocNum(2, 4)
        print("newNumOnes is ", newNumOnes)
        newStocNum.changeStocNum(newArr, newNumOnes, stocNum1.nBits)
        return newStocNum

def printFunc(numOnes1, numBits1, numOnes2, numBits2, result, expectedVal, trialNum):
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print(' TRIAL #',trialNum,' (',numBits1,' bit stochastic numbers)')   
    print('-----------------------------------------------------------------------------------------------------------------------------------------------------------------------')
    print("This is trial 1, where we will be multiplying stochastic numbers 3/8 (", numOnes1/numBits1, ") and 5/8 (", numOnes2/numBits2, ") with 8 bits.\n", numOnes1/numBits1, " * ", numOnes2/numBits2, " is ", numOnes1*numOnes2,"/", numBits1*numBits2," (", (numOnes1*numOnes2) / (numBits1*numBits2),")\nCalculating...\nThe resulting number is: ", result)
    print('The percent error for this trial is: ', (abs(result-expectedVal)/expectedVal)*100)

#trial1 code
stocNum1 = StocNum(3, 8)
stocNum2 = StocNum(5, 8)
resultStocNum = ANDer(stocNum1, stocNum2)
printFunc(3, 8, 5, 8, resultStocNum.pDec, 0.2344, 1)

#trial2 code
stocNum1 = StocNum(6, 16)
stocNum2 = StocNum(10, 16)
resultStocNum = ANDer(stocNum1, stocNum2)
printFunc(6, 16, 10, 16, resultStocNum.pDec, 0.2344, 1)

#trial3 code
stocNum1 = StocNum(12, 32)
stocNum2 = StocNum(20, 32)
resultStocNum = ANDer(stocNum1, stocNum2)
printFunc(12, 32, 20, 32, resultStocNum.pDec, 0.2344, 1)

#trial4 code
stocNum1 = StocNum(24, 64)
stocNum2 = StocNum(40, 64)
resultStocNum = ANDer(stocNum1, stocNum2)
printFunc(24, 64, 40, 64, resultStocNum.pDec, 0.2344, 1)

#trial5 code
stocNum1 = StocNum(48, 128)
stocNum2 = StocNum(80, 128)
resultStocNum = ANDer(stocNum1, stocNum2)
printFunc(48, 128, 80, 128, resultStocNum.pDec, 0.2344, 1)

#trial5 code
stocNum1 = StocNum(96, 256)
stocNum2 = StocNum(96, 256)
resultStocNum = ANDer(stocNum1, stocNum2)
printFunc(96, 256, 96, 256, resultStocNum.pDec, 0.2344, 1)

# #trial1 code
# sumOfResults = 0
# for i in range(20):
#     stocNum1 = StocNum(3, 8)
#     stocNum2 = StocNum(5, 8)
#     resultStocNum = ANDer(stocNum1, stocNum2)
#     sumOfResults += resultStocNum.pDec
# result = sumOfResults / 20
# printFunc(3, 8, 5, 8, result, 0.2344, 1)

# #trial2 code
# sumOfResults = 0
# for i in range(20):
#     stocNum1 = StocNum(6, 16)
#     stocNum2 = StocNum(10, 16)
#     resultStocNum = ANDer(stocNum1, stocNum2)
#     sumOfResults += resultStocNum.pDec
# result = sumOfResults / 20
# printFunc(6, 16, 10, 16, resultStocNum.pDec, 0.2344, 1)

# #trial3 code
# sumOfResults = 0
# for i in range(20):
#     stocNum1 = StocNum(12, 32)
#     stocNum2 = StocNum(20, 32)
#     resultStocNum = ANDer(stocNum1, stocNum2)
#     sumOfResults += resultStocNum.pDec
# result = sumOfResults / 20
# printFunc(12, 32, 20, 32, resultStocNum.pDec, 0.2344, 1)

# print("stocNum1 binary representation is", stocNum1.BinaryRepresentation)
# print("stocNum1 pFrac is", stocNum1.pFrac)
# print("stocNum1 pDec is", stocNum1.pDec)
# print("stocNum2 binary representation is", stocNum2.BinaryRepresentation)
# print("stocNum2 pFrac is", stocNum2.pFrac)
# print("stocNum2 pDec is", stocNum2.pDec)
# print("multiplying...")
# print("resulting pFrac is ", resultStocNum.pFrac)
# print("resulting pDec is ", resultStocNum.pDec)
# print("resulting binary representation is", resultStocNum.BinaryRepresentation)



        