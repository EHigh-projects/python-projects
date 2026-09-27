# import numpy for arrays and data reading functionalities

import numpy as np

# import data from downloads folder path, use skiprows parameter to avoid reading first 3 lines of text doccument (irrelevant)

data = np.loadtxt("C:/Users/ejhig/Downloads/data.txt", skiprows = 3) 

# the next three lines seperate the frequency, amplitude, and amplitude error data 

f = np.array(data[:,0])  
a = np.array(data[:,1])  
da = np.array(data[:,2]) 

# the next three lines then use formatted strings to print the data with labels.  

print( f"f = {f}")
print( f"a = {a}")
print( f"da = {da}")
