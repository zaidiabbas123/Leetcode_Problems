//98)validate bst

 list<int> mydata;
        inorderTraversal(root, mydata);

        int j = 0;
        int min = 0;
        for(int data: mydata)
        {
            if(data <= min && j > 0)
                return false;
            min = data;
            j++;
        }
        return true;

    }

    void inorderTraversal(TreeNode* root, list<int> &list)
    {
        if(!root)
            return;

        inorderTraversal(root->left, list);
        list.push_back(root->val);
        inorderTraversal(root->right, list);

    }