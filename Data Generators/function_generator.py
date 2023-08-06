from math import sin, cos, tan, exp
import random
import matplotlib


#CONSTANTS
MIN_X = 0
MAX_X = 10
MAGNITUDE = 0.3
STEP_SIZE = 0.5
    

def function(x):
    return sin(x)

def noise(magnitude):
    return (2*random.randrange(0,2)-1) * exp(-random.random()*2) * magnitude

def write_to_file(name, X, Y):
    fob1 = open(name+".txt", "w+")
    fob2 = open(name+"_desmos.txt", "w+")
    for i in range(len(X)):
        fob1.writelines(str(X[i]) + " " + str(Y[i]) + "\n")
        fob2.writelines("\\left(" + str(X[i]) + "," + str(Y[i]) + "\\right)")
        if( i != len(X) - 1 ): fob2.writelines(",")
    fob1.close()
    fob2.close()

def main():
    X = []
    Y = []
    delta_range = ( MAX_X - MIN_X ) / 10
    i = MIN_X
    while i < MAX_X :
        x = i + STEP_SIZE * random.random()
        X.append(x)
        Y.append(function(x)+noise(MAGNITUDE))
        i += STEP_SIZE
    write_to_file("dataset", X, Y)
    
if __name__ == "__main__":
    main()
