# A very simple dataGenerating app for classification problems on 2-D plain
import numpy as np

class_num = int(input("Enter the number of classes: "))
data_per_class = int(input("Enter the number of data per each class:"))

means = np.array([])
covs = np.array([])

for i in range(class_num):
    inp = input("Enter mean coordinate: ").split(' ')
    means = np.append(means, [float(inp[0]), float(inp[1])])
    covs = np.append( covs , float(input("Enter Covariance( This will be treated as an estimate covariance ): ")))


means = means.reshape(class_num , 2)

data = np.array([])

for i in range(class_num):
    for j in range(data_per_class):
        angle = np.random.random() * 2 * np.pi
        distance = abs(np.random.normal(0, covs[i]))
        x = means[i][0] + distance*np.cos(angle)
        y = means[i][1] + distance*np.sin(angle)
        data = np.append(data, [x, y])

data = data.reshape(class_num,data_per_class,2)

file = open('data.txt', 'w+')
file_desmos = open('data_desmos.txt', 'w+')

for i in range(class_num):
    for j in range(data_per_class):
        file.writelines(str(data[i][j][0]) + ' ' + str(data[i][j][1]) + ' ' + str(i) + '\n')
    

for i in range(class_num):
    for j in range(data_per_class):
        file_desmos.writelines('\\left(' + str(data[i][j][0]) + ',' + str(data[i][j][1]) + '\\right)')
        if( j != data_per_class - 1 ): file_desmos.writelines(',')
    file_desmos.writelines('\n\n\n')
    
file.close()
file_desmos.close()
