#include <iostream>
using namespace std;

int main(void){
	ios::sync_with_stdio(false);
	double n1 = 2.555;
	double n2 = 2.565;

	cout<<fixed;
  	cout.precision(2);
  	cout<<n1<<'\n';
	cout<<n2<<'\n';

	return 0;
}