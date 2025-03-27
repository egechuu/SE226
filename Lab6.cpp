//
// Created by ege on 27.03.2025.
//
#include <iostream>
using namespace std;

double recursiveSum(int n) {
  if(n==0) return 0;
  return 1.0 / n + recursiveSum(n-1);
}
// overloaded method
double recursiveSum() {
  int a;
  cout << "Please enter a number: ";
  cin >> a;
  double result = recursiveSum(a);
  cout << "The result is: " << result << endl;
}

int main() {
  recursiveSum();
}



