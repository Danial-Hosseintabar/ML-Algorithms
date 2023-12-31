#include <bits/stdc++.h>
using namespace std ;
int main(){
	int n , m ;
	
	cout << "# n = number of features\n# Enter n : ";
	cin >> n ;
	cout << "\n# m = number of datas\n# Enter m : " ;
	cin >> m ;

	double Y[m] ;
	double X[m][n+1] ;
	double th[n+1] ;


	double learning_rate ;
	double iteration_count ;
	cout << "\n# Enter alpha : " ;
	cin >> learning_rate ;
	cout << "# Enter iteration count : " ;
	cin >> iteration_count ;


	cout << "\n# Enter you datas\n# The input form is like this :\n# " <<
		"\"x_1 x_2 ... x_n y\" in each line\n\n" ;

	for(int i = 0 ; i < m ; i++){
		X[i][0] = 1 ;
		for(int j = 1 ; j <= n ; j++)
			cin >> X[i][j] ;
		cin >> Y[i] ;
	}

	memset( th , 0 , ( n + 1 ) * sizeof( double ) ) ;

	
	

	{
		double sum[n+1] ;
		double poly[m] ;
		for(int k = 0 ; k < iteration_count ; k++){
			
			for(int j = 0 ; j < m ; j++){
				poly[j] = 0 ;
				for(int t = 0 ; t <= n ; t++)
					poly[j] += th[t] * X[j][t] ;
			}
			for(int i = 0 ; i <= n ; i++){
				sum[i] = 0 ;
				for(int j = 0 ; j < m ; j++){
					sum[i] += ( poly[j] - Y[j] ) * X[j][i] ;
				}
			}

			for(int i = 0 ; i <= n ; i++) th[i] -= learning_rate * sum[i] ;
		}
	}

	cout << "\n# Final Answer for Theta[i] ( 0 <= i <= " << n << " )" << endl ;
	for(int i = 0 ; i <= n ; i++) cout << "Theta[" << i << "] = " << th[i] << '\n' ;
	cout << "\n\n";

}
