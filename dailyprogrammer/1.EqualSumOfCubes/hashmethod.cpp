//compile with "clang++ -std=c++11 -Wall -Wextra -o hashmethod hashmethod.cpp"
//run with "./hashmethod"
#include <unordered_map>
#include <iostream>
#include <list>
#include <math.h>

using namespace std;

int main() 
{
	//map result to pair of integers
    unordered_map <int, list< pair<int, int> > > resultToListofPairs;

    int MAX = 1000;

    //store each pair of numbers in a pair container
    pair<int, int> couple;

    //map each sum produced by a^3 + b^3 to a list of ab pairs that produce the same sum
    for(int a = 0; a <= MAX; a++){
    	for(int b = 0; b <= MAX; b++){
    		int sum = pow(a, 3) + pow( b, 3);
    		couple.first = a;
    		couple.second = b;
    		//append unique ab pair to list of pairs that produce the same sum
    		resultToListofPairs[sum].push_front(couple);
    	}
    }

    //iterate though the hash table
    for( auto it = resultToListofPairs.begin(); it != resultToListofPairs.end(); it++){

    	//store each list as a local variable
    	list<pair<int,int>> pairlist = it->second;

    	//print all unique pairs of ab and cd
    	for(auto it1 = pairlist.begin(); it1 != pairlist.end(); it1++){
    		for(auto it2 = pairlist.begin(); it2 != pairlist.end(); it2++){
    			if(it1->first != it2->first && it1->first != it2->second){
    				//print right justified
    				printf("%4d %4d %4d %4d \n", it1->first, it1->second, it2->first, it2->second);
    			}
    		}
    	}
    }

    return 0;

}

		// Formal iterator
    	// //print all unique pairs of ab and cd
    	// for(list<pair<int,int>>::iterator it1 = mylist.begin(); it1 != mylist.end(); it1++){
    	// 	for(list<pair<int,int>>::iterator it2 = mylist.begin(); it2 != mylist.end(); it2++){
    	// 		if(it1->first != it2->first && it1->first != it2->second){
    	// 			printf("%4d %4d %4d %4d \n", it1->first, it1->second, it2->first, it2->second);
    	// 		}
    	// 	}
    	// }