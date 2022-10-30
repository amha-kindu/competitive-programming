
class Solution {
public:
    void printV(vector<int>& v){
        for(int i: v)   cout<<i<<" ";
        cout<<endl;
    }
    vector<string> topKFrequent(vector<string>& words, int k) {
        unordered_map<int, set<string>> counter;
        vector<int> counts;
        for(string s: set(words.begin(), words.end())){
            int c = count(words.begin(), words.end(), s);
            if(counter.find(c)==counter.end()){
                counts.push_back(c);
                push_heap(counts.begin(), counts.end());
            }
            counter[c].insert(s);
        }

        vector<string> answer;
        while(answer.size()<k){
            pop_heap(counts.begin(), counts.end());
            for(string s: counter[counts.back()]){
                answer.push_back(s);
                if(answer.size()==k)    break;
            }
            counts.pop_back();
            
        }
        return answer;
    }
};