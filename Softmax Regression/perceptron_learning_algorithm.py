# Perceptron learning algorithm
# author: Danial Hosseintabar

def get_positive_integer_input():
    while True :
        try:
            n = int(input("->"))
            if n > 0 :
                return n
            else:
                print("Please enter a positive number")
        except:
            print("Error: please enter a number")

def threshold(x):
    if(x >= 0): return 1
    else: return 0

n = 0
m = 0

print("Enter the number of features for each data")
n = get_positive_integer_input()
print("Enter the number of datas")
m = get_positive_integer_input()

X = []
Y = []

print("Enter all datas like this:")
print("x1 x2 x2 ... xn y ( where y is either 0 or 1 )")

for i in range(0,m):
    x_i = [1]
    inputs = input().split(' ')
    for i in range(0,n):
        x_i.append(float(inputs[i]))
    X.append(x_i)
    Y.append(float(inputs[n]))

theta = []

for i in range(0,n+1):
    theta.append(0)

learning_rate = 0.01
iteration_count = 10000

def calculate_hypothesis( X , theta ):
    ret = 0
    for i in range(0,n+1):
        ret += X[i] * theta[i]
    return threshold(ret)

def calculate_sum( index , X , Y , theta ):
    ret = 0
    for i in range( 0 , m ):
        ret += ( calculate_hypothesis( X[i] , theta ) - Y[i] ) * X[i][index]
    return ret

for i in range(0,iteration_count):
    sum = []
    for i in range(0,n+1):
        sum.append( calculate_sum(i , X , Y , theta) )
    for i in range(0,n+1):
        theta[i] -= learning_rate * calculate_sum(i,X,Y,theta)

for i in range(0,n+1):
    print("theta[" , i , "] :" , theta[i])


input("Press Enter to Exit")
