#include <vector>

class NaiveBayes {
	public:
		NaiveBayes(int n, int m, int k, std::vector<std::vector<bool>> x, std::vector<int> y){
			this->n = n; // number of features
			this->m = m; // number of datas
			this->k = k; // number of classes
			this->x = x; // x datas
			this->y = y; // y datas

		}
	
		float probabality_y_given_x(int _y, std::vector<bool> _x){
			return probability_y(_y) * probability_x_given_y(_x, _y) / probability_x(_x) ;
		}
	
	private:
		int n, m, k;
		std::vector<std::vector<bool>> x;
		std::vector<int> y;

		float probability_y(int _y){
			int cnt = 0;
			for(int i = 0 ; i < m ; i++)
				cnt += (_y == y[i]);
		}

		float probability_x_given_y(std::vector<bool> _x, int _y){
			int cnt;
			float ret = 1;
			for(int i = 0 ; i < n ; i++){
				cnt = 0 ;
				for(int j = 0 ; j < m ; j++)
					if(x[j][i] == _x[i]) cnt++;
				ret *= float(1) * cnt / m;
			}
			return ret;
		}

		float probability_x(std::vector<bool> _x){
			float p = 0;
			for(int _y = 0 ; _y < k ; _y++){
				p += probability_y(_y) * probability_x_given_y(_x, _y);
			}
			return p;
		}

	
};

int main(){
	// test
}

