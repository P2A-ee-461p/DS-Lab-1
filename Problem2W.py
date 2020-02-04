import numpy as np

def projectOntoPlane(basis1, basis2, v):
	ortho = np.cross(basis1, basis2)
	orthoComp = np.dot(v, ortho)/np.dot(ortho, ortho) * ortho
	planev = v-orthoComp
	return planev

plane1 = [1,1,1]
plane2 = [1,0,0]

print("normal: ", np.cross(plane1, plane2))

print(projectOntoPlane(plane1, plane2, [3,3,3]))
print(projectOntoPlane(plane1, plane2, [1,2,3]))
print(projectOntoPlane(plane1, plane2, [0,0,1]))
