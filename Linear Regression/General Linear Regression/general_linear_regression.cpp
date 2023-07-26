#include <bits/stdc++.h>
using namespace std ;
int main(){
	int n , m ;
	
	cout << "n = number of features\nEnter n :";
	cin >> n ;
	cout << "m = number of datas\nEnter m :" ;
	cin >> m ;

	double Y[m] ;
	double X[m][n+1] ;
	double th[n+1] ;


	double alpha ;
	double iteration_count ;
	cout << "Select alpha" ;
	cin >> alpha ;
	cout << "Select iteration count" ;
	cin >> iteration_count ;


	cout << "Enter you datas\nThe input form is like this :\n" <<
		"\"x_1 x_2 ... x_n y\" in each line\n" ;

	for(int i = 0 ; i < m ; i++){
		X[i][0] = 1 ;
		for(int j = 1 ; j <= n ; j++)
			cin >> X[i][j] ;
		cin >> Y[i] ;
	}

	memset( th , 0 , ( n + 1 ) * sizeof( double ) ) ;

	
	

	{
		double sum[n+1] ;
		double poly ;
		for(int k = 0 ; k < iteration_count ; k++){
			
			for(int i = 0 ; i <= n ; i++){
				sum[i] = 0 ;
				for(int j = 0 ; j < m ; j++){
					poly = 0 ;
					for(int k = 0 ; k <= n ; k++) poly += th[k] * X[j][k] ;
					sum[i] += ( poly - Y[j] ) * X[j][i] ;
				}
			}

			for(int i = 0 ; i <= n ; i++) th[i] -= alpha * sum[i] ;
		}
	}

	cout << "Final Answer for Theta[i], 0 <= i <= " << n << endl ;
	for(int i = 0 ; i <= n ; i++) cout << th[i] << ' ' ;
	cout << '\n' ;

}