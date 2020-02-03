import numpy as np

def projectOntoPlane(basis1, basis2, v):
	ortho = np.cross(basis1, basis2)
	orthoComp = np.dot(v, ortho)/np.dot(ortho, ortho) * ortho
	planev = v-orthoComp
	return planev

print(projectOntoPlane([1,1,1], [1,0,0], [3,3,3]))
print(projectOntoPlane([1,1,1], [1,0,0], [1,2,3]))
print(projectOntoPlane([1,1,1], [1,0,0], [0,0,3]))