import sys
import numpy as np
#print('argument',sys.argv)
#print("length:",len(sys.argv))
#sys.argv[0]=filename
#sys.argv[1]=table coloumn name
#convert into numPy array and slice argument from 2 to last element
#bcoz 1st element is filename,2nd is column name of table
nameArr = np.array(sys.argv)
for arg in nameArr[2:]:
  print(arg)


