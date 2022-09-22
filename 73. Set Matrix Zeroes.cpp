class Solution {
public:
    void setZeroes(vector<vector<int>>& matrix) {
         //change all row and column to -1 for that particular 0 so            that we dont inc no of 0's and hamper existing 0's
        //optimize using 2 dummy array
        int col0=1,rows=matrix.size(),cols=matrix[0].size();
        for(int i=0;i<rows;i++){
            if(matrix[i][0]==0)col0=0;
            for(int j=1;j<cols;j++){
                if(matrix[i][j]==0){
                    matrix[i][0]=matrix[0][j]=0;
                }
            }
        }
        for(int i=rows-1;i>=0;i--){
            for(int j=cols-1;j>=1;j--){
                if(matrix[i][0]==0||matrix[0][j]==0){
                    matrix[i][j]=0;
                }
            }
            if(col0==0)matrix[i][0]=0;
        }
    }
};