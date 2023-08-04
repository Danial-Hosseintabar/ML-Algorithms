# 2D data generator
# assigning a number of (x, y) coordinates a binary output.
# author: Dainal Hosseintabar

import random
import math


print("The seperating line is a * x + b * y + c = 0")
print("Data's are generated in this area: ( 0 < x < 10 ) & ( 0 < y < 10)")
print("Two outputs will be generated, one for using in desmos graphing app, one for using in command line programs")
print("")

print("Enter a:")
a = float(input())
print("Enter b:")
b = float(input())
print("Enter c:")
c = float(input())

data_count = int(input("Number of datas: "))
file_name = input("Name of output file: ")

fob = open(file_name + ".txt" , 'w')
fob_desmos = open( file_name + "_desmos.txt" , 'w' )

one = []
zero = []

for i in range( 0 , data_count ) :
    x = math.trunc( random.random() * 1000 ) / 100
    y = math.floor( random.random() * 1000 ) / 100
    if( a * x + b * y + c >= 0 ):
        value = 1
        one.append((x,y))
    else:
        value = 0
        zero.append((x,y))
    fob.write( str(x) + " " + str(y) + " " + str(value) + '\n' )

fob.close()

for i in range(0,len(one)):
    if( i > 0 ): fob_desmos.write( "," )
    fob_desmos.write("\\left(" + str(one[i][0]) + "," + str(one[i][1]) + "\\right)")

fob_desmos.write("\n")

for i in range(0,len(zero)):
    if( i > 0 ): fob_desmos.write( "," )
    fob_desmos.write("\\left(" + str(zero[i][0]) + "," + str(zero[i][1]) + "\\right)")


fob_desmos.close()
