#creating the following shape using numpy 
#[1. 1. 1. 1. 1.]
#[1. 0. 0. 0. 1.]
#[1. 0. 9. 0. 1.]
#[1. 0. 0. 0. 1.]
#[1. 1. 1. 1. 1.]

#importing numpy
import numpy as np

#creating an output
output = np.ones((5,5))

#creating and inserting the middle 
middle = np.zeros((3,3))
middle[1,1] = 9
print(middle)

#inserting the middle into the output
output[1:4,1:4] = middle
print(output)

