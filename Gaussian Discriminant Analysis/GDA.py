import numpy as np
# GDA for 2-D data
# reading datas from file
raw_data = np.genfromtxt('data.txt', delimiter=' ')
#print(raw_data)

class_num = int(input("Enter the number of classes"))

data_count = 0
data = [np.array([]) for i in range(class_num)]

for each_data in raw_data:
    new_point = np.array([each_data[0], each_data[1]]);
    data_count += 1
    data[int(each_data[2])] = np.append(data[int(each_data[2])], new_point)

for i in range(len(data)):
    data[i] = data[i].reshape(int(data[i].size/2),1,2)



print(data[0][0].transpose())


# note: data[data_class][index of data in that class][index of feature]

center = np.array([]) # Mean of each normal distribution

for i in range(class_num):
    new_center = np.array([[0, 0]], dtype='float64')
    for j in range(int(data[i].size/2)):
        new_center += data[i][j]
    new_center /= data[i].size / 2
    center = np.append(center, new_center)

print("Center")
print(center)

covariance_matrix = np.full((2,2),0, dtype='float64')

for i in range(2):
    for j in range(data[i].shape[0]):
        deviation = data[i][j] - center[i]
        covariance_matrix += (np.matmul(deviation.transpose(),deviation))

covariance_matrix /= data_count

print(covariance_matrix)

print(np.linalg.det(covariance_matrix))
