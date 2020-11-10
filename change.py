import pandas as pd
from random import sample, randrange 
import copy
testcsv = pd.read_csv("mtsamples_copy.csv")

print(len(testcsv))
sur = list(testcsv[testcsv["medical_specialty"] == 'surgery'].index.values)
med = list(testcsv[testcsv["medical_specialty"] == 'medicines'].index.values)
other = list(testcsv[testcsv["medical_specialty"] == 'other'].index.values)
t = copy.copy(sur)

# print(len(sur))
# print(len(med))
# print(len(other))
# print(len(sample(sur,int(len(other)*88/100))))
t1 = [sur.pop(randrange(len(sur))) for _ in range(900)]
t2 = [med.pop(randrange(len(med))) for _ in range(900)]
t3 = [med.pop(randrange(len(med))) for _ in range(850)]

# for 