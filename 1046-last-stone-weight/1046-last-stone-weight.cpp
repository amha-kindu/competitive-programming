class Solution {
public:
    int lastStoneWeight(vector<int>& stones) {
        make_heap(stones.begin(), stones.end());
        while(stones.size()>1){
            int x=0;
            for(int i=0;i<2;i++){
                pop_heap(stones.begin(), stones.end());
                x = abs(x-stones.back());
                stones.pop_back();
            }
            if(x!=0){
                stones.push_back(x);
                push_heap(stones.begin(), stones.end());
            }
        }
        if(stones.size()>0) return stones.front();
        else return 0;
    }
};