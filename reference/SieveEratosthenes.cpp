#include <math.h>
#include <iostream>

using namespace std;

void runEratosthenesSieve(int upperBound) {
      long sum = 0;
      int upperBoundSquareRoot = (int)sqrt((double)upperBound);
      bool *isComposite = new bool[upperBound + 1];
      for(int i = 0; i < (upperBound + 1); i++){
            isComposite[i] = false;
      }
      for (int m = 2; m <= upperBoundSquareRoot; m++) {
            if (!isComposite[m]) {
                  for (int k = m * m ; k <= upperBound; k += m){
                        cout << "k is " << k << endl;
                        isComposite[k] = true;
                  }
            }
      }
      for (int m = 2; m <= upperBound; m++)
            if (!isComposite[m])
                  sum += m;
      delete [] isComposite;
      cout << sum << endl;

}

int main()
{
      int max = 100;
      runEratosthenesSieve(max);
}