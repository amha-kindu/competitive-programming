class LinkedNode{
    public:
    LinkedNode* next;
    LinkedNode* prev;
    int value;
    int key;
    LinkedNode(int val,int key, LinkedNode* next, LinkedNode* prev):value(val), key(key), next(next), prev(prev){}
    
};

class DoubleLL{
    public:
    LinkedNode* head;
    LinkedNode* tail;
    
    DoubleLL():head(nullptr), tail(nullptr){}
    DoubleLL(LinkedNode* head, LinkedNode* tail):head(head), tail(tail){}
    
    LinkedNode* popBack(){
        LinkedNode* temp = tail;
        tail = tail->prev; 
        if(tail!=nullptr){
            tail->next=nullptr;
        }
        else head=nullptr;
        
        return temp;
    }
    
    void insertFront(int key, int val){
        LinkedNode* newNode = new LinkedNode(val, key, head, nullptr);
        
        if(head==nullptr)   tail=newNode;
        else    head->prev=newNode;
        head = newNode;
    }
    
    void moveToFront(LinkedNode* node){
        if(node==head)  return;
        if(node==tail)  tail=tail->prev;

        LinkedNode* prev = node->prev;
        LinkedNode* next = node->next;
        if(prev!=nullptr)
            prev->next = next;
        if(next!=nullptr)
            next->prev = prev;
        
        node->prev=nullptr;
        node->next = head;
        head->prev=node;
        head = node;
    }
    
};


class LRUCache {
public:
    int capacity;
    unordered_map<int, LinkedNode*> frames;
    DoubleLL addresses;
    
    LRUCache(int capacity) {
        this->capacity = capacity;
        addresses = DoubleLL();    
    }
    
    int get(int key) {
        if(frames.find(key)!=frames.end()){
            LinkedNode* node = frames[key];
            addresses.moveToFront(node);
            return node->value;
        }
        return -1;
    }
    
    void put(int key, int value) {
        if(frames.find(key)!=frames.end()){
            //Cache hit
            LinkedNode* node = frames[key];
            addresses.moveToFront(node);
            node->value = value;
        }
        else{
            //Cache miss   
            if(frames.size()==capacity)
            {
                LinkedNode* leastUsed = addresses.tail;
                addresses.tail = addresses.tail->prev; 
                if(addresses.tail!=nullptr){
                    addresses.tail->next=nullptr;
                }
                else addresses.head=nullptr;
                
                frames.erase(leastUsed->key);
                delete leastUsed;
            }
            // addresses.insertFront(key, value);
            LinkedNode* newNode = new LinkedNode(value, key, addresses.head, nullptr);
        
            if(addresses.head==nullptr)   addresses.tail=newNode;
            else    addresses.head->prev=newNode;
            addresses.head = newNode;
            frames[key]=addresses.head;
        }
        
    }
};
/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */