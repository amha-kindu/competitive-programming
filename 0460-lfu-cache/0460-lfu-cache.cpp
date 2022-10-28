
class LinkedNode{
    public:
    LinkedNode* next;
    LinkedNode* prev;
    int value;
    int key;
    int count;
    LinkedNode(int val,int key, LinkedNode* next, LinkedNode* prev):value(val), key(key), next(next), prev(prev),count(1){}
    
};

class DoubleLL{
    public:
    LinkedNode* head;
    LinkedNode* tail;
    
    DoubleLL():head(nullptr), tail(nullptr){}
    DoubleLL(LinkedNode* head): head(head), tail(head){}
    DoubleLL(LinkedNode* head, LinkedNode* tail):head(head), tail(tail){}
    
    void insertFront(int key, int val){
        LinkedNode* newNode = new LinkedNode(val, key, head, nullptr);
        
        if(head==nullptr)   tail=newNode;
        else    head->prev=newNode;
        head = newNode;
    }
    void insertFront(LinkedNode* new_head){
        new_head->next = head;
        new_head->prev = nullptr;
        if(head==nullptr)   tail=new_head;
        else    head->prev=new_head;
        head = new_head;
    }

    void remove(LinkedNode* node){
        if(head==nullptr||node==nullptr)
            return;
        if(head==node)  head = node->next;
        if(node==tail)  tail = tail->prev;
        if(node->next!=nullptr) node->next->prev = node->prev;
        if(node->prev!=nullptr) node->prev->next=node->next;
        node->next=nullptr; node->prev=nullptr;
    }
    
};


class LFUCache {
public:
    int capacity;
    unordered_map<int, LinkedNode*> frames;
    unordered_map<int, DoubleLL> counter;
    
    LFUCache(int capacity): capacity(capacity){}
    
    int get(int key) {
        if(capacity>0 && frames.find(key)!=frames.end()){
            LinkedNode* node = frames[key];
            counter[node->count].remove(node);

            if(counter[node->count].head == nullptr) 
                counter.erase(node->count);

            node->count++;
            if(counter.find(node->count)==counter.end()){
                counter[node->count]= DoubleLL(node);
            }
            else   counter[node->count].insertFront(node);
            return node->value;
        }
        return -1;
    }
    void put(int key, int value) {
        if(frames.find(key)!=frames.end()){
            //Cache hit
            LinkedNode* node = frames[key];
            counter[node->count].remove(node);

            if(counter[node->count].head == nullptr) 
                counter.erase(node->count);

            node->count++;
            
            if(counter.find(node->count)==counter.end()){
                counter[node->count] = DoubleLL(node);
            }
            else   counter[node->count].insertFront(node);
            node->value = value;
        }
        else{
            LinkedNode* lfuNode=nullptr;
            
            //Cache miss   
            if(frames.size()==capacity)
            {
                int minCount = INT32_MAX;
                for(auto it: counter)   minCount=min(minCount, it.first);
                lfuNode = counter[minCount].tail;
                counter[minCount].remove(lfuNode);
                if(counter[minCount].head == nullptr) 
                    counter.erase(minCount);
                if(lfuNode!=nullptr)
                    frames.erase(lfuNode->key);
            }
            if(counter.find(1)==counter.end())  
                counter[1]= DoubleLL();
            if(lfuNode!=nullptr){
                lfuNode->key=key;
                lfuNode->value=value;
                lfuNode->count=1;
                counter[1].insertFront(lfuNode);
            }
            else    counter[1].insertFront(key, value);
            
            frames[key]=counter[1].head;
        }
        
    }
    
};


/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache* obj = new LFUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */