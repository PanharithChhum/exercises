#include <vector>
#include <iostream>
#include <cmath>

using namespace std;

bool check(int row, int col, vector<int> queens)
{
    for(int i = 0; i < (int)queens.size(); i++){
        if(queens.at(i) == col or i == row or 
            abs(queens.at(i) - col) == abs(i - row))
            return false;
    }
    return true;

}

vector<vector<int> > solve(int board_size, vector<int> queens, int* max_queens)
{
    int row = 0;
    int col = 0;
    
    vector<vector<int> > solutions;

    while(true){
        if(row == 0 and col == board_size){ //base case, reached the end
            return solutions;
        }
        if(row == board_size){  //we have a solution
            solutions.push_back(queens);
            (*max_queens)++;
        }
        //optimized to quit when subsequent line is empty
        if(col == board_size or row == board_size){
            int c = queens.back();
            queens.pop_back();
            row--;
            col = c + 1;
        }
        else if(check(row, col, queens)){
            queens.push_back(col);
            row++;                          //check next line
            col = 0;
        }
        else
            col++;
    }

}

int main()
{
    int board_size = 8;
    int max_queens = 0;
    vector<int> queens;

    vector<vector<int> > solutions = solve(board_size, queens, &max_queens);

    for(size_t i = 0; i < solutions.size(); i++){
        for(size_t j = 0; j < solutions.at(i).size(); j++){
            cout << solutions.at(i).at(j) << " ";
        }
        cout << endl;
    }
    cout << "combinations are " << max_queens << endl;

    return 0;
}