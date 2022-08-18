//79)Word search

class Solution {
public:
    bool exist(vector<vector<char>>& board, string word) {
        if(word.empty() or board.empty()){
            return false;
            
        }
        bool foundMatch=false;
        for(int i=0;i<board.size();i++){
            for(int j=0;j<board[0].size();j++){
                if(board[i][j]==word[0]){
                    searchWord(word,{},board,0,i,j,foundMatch);
                }
                if(foundMatch){
                    return foundMatch;
                }
            }
        }
        return foundMatch;
    }
    void searchWord(const std::string&word,
                   std::string currentWord,
                   std::vector<std::vector<char>>& board,
                   int index,
                   int i,
                   int j,
                   bool& foundMatch)
    {
        if(currentWord.size()==word.size()){
            foundMatch=true;
            return;
        }
        if(i<0 or j<0 or i>=board.size() or j>=board[0].size() or board[i][j]!=word[index] or foundMatch)
            return;
        currentWord+=word[index];
        char temp=board[i][j];
        board[i][j]=' ';
        searchWord(word,currentWord,board,index+1,i+1,j,foundMatch);
        searchWord(word,currentWord,board,index+1,i-1,j,foundMatch);
        searchWord(word,currentWord,board,index+1,i,j+1,foundMatch);
        searchWord(word,currentWord,board,index+1,i,j-1,foundMatch);
        board[i][j]=temp;
        
    }
};