#
#
# WARNING: THIS CODE STILL NEEDS SOME DEBUGGING
#
#
def dot_product( a , b ):
    if( len(a) != len(b) ):
        return "ERROR"
    ret = 0
    for i in range( 0 , len( a ) ):
        ret += a[i] * b[i]
    return ret

def main():
    class_count = int(input("Enter the number of classes: "))
    n = int(input("Enter the number of features"))
    m = int(input("Enter the number of datas"))
    print("Enter the datas like this:")
    print("X_1 X_2 X_3 .. X_n CLASS(zero indexed)")
    X = [[] for i in range(0,m)]
    Y = [0 for i in range(0,m)]
    for i in range(0,m):
        text_input = input("-> ").split()
        X[i].append(1)
        for j in range(0,n) :
            X[i].append(int(text_input[j]))
        Y[i] = int(text_input[-1])
    

    theta = [[0 for j in range(0,n+1)] for i in range(0,class_count)]


    iteration_count = 10000
    learning_rate = 0.01

    delta = [[0 for j in range(0,n+1)] for i in range(0,class_count)]

    etx = [[0 for j in range(0,m)] for i in range(0,class_count)]
    sum_etx = [0 for i in range(0,m)]

    for iteration in range( 0 , iteration_count ):

        for i in range(0,class_count):
            for j in range(0,m):
                etx[i][j] = dot_product( theta[i] , X[j] )

        for i in range(0,m):
            sum_etx[i] = 0
            for j in range(0,class_count):
                sum_etx[i] += etx[j][i]
            

        for x in range(0,class_count):
            for y in range(0,n+1):
                # updating delta[x][y]
                for i in range(0,m):
                    if( Y[i] != x ): continue
                    delta[x][y] = X[i][y] * ( 1 - etx[x][i] / ( 1 + sum_etx[i] ) )



    for i in range(0,class_count):
        print(theta[i])
    

if __name__ == "__main__":
    main()
