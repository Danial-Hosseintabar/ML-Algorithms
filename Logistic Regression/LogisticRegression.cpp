#include <bits/stdc++.h>
using namespace std ;

double calculate_polynomial( double* X , double* th , int n ){
	// returns the value of theta[i] * X[i] from i = 0 to i = n
	double ret = 0 ;
	for(int i = 0 ; i <= n ; i++) ret += th[i] * X[i] ;
	return ret ;
}

double sigmoid( double x ){
	return 1 / ( exp(-x) + 1 ) ;
}

int main(){
	int m ;
	cout << "# Enter number of datas: " ;
	cin >> m ;
	int n ;
	cout << "# Enter number of features: " ;
	cin >> n ;
	cout << "\n# Enter datas, enter each one in a single line like this :\n" ;
	cout << "# \"x_1 x_2 ... x_n y\" ( y is the binary output )\n\n" ;
	
	double Y[m] ;
	double X[m][n+1] ;
	double th[n+1] ;

	memset( th , 0 , ( n + 1 ) * sizeof( double ) ) ;

	for(int i = 0 ; i < m ; i++){
		cout << " -> " ;
		X[i][0] = 1 ;
		for(int j = 1 ; j <= n ; j++){
			cin >> X[i][j] ;
		}
		cin >> Y[i] ;
	}

	int iteration_count ;
	double learning_rate ;

	cout << "\n# Enter iteration count: " ;
	cin >> iteration_count ;
	cout << "# Enter learning rate: " ;
	cin >> learning_rate ;
	
	double sum[n+1] ;
	
	for(int z = 0 ; z < iteration_count ; z++){
		for(int i = 0 ; i <= n ; i++){
			sum[i] = 0 ;
			for(int j = 0 ; j < m ; j++) sum[i] += X[j][i] * (sigmoid(calculate_polynomial(X[j],th,n)) - Y[j]) ;
		}
		for(int i = 0 ; i <= n ; i++)
			th[i] -= sum[i] * learning_rate ;
	}

	cout << "\n# Theta:\n" ;
	for(int i = 0 ; i <= n ; i++)
		cout << setprecision(3) << fixed << " Theta[" << i <<"]: " << th[i] << '\n' ;
	cout << "\n# Output of function for each data:\n" ;
	for(int i = 0 ; i < m ; i++)
		cout << setprecision(3) << fixed << " " << sigmoid(calculate_polynomial(X[i],th,n)) << endl ;
}
