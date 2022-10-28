class MyNode{
    public:
    int value;
    MyNode* next;
    MyNode* prev;
    MyNode():value(0), next(nullptr), prev(nullptr){}
    MyNode(int val): value(val), next(nullptr), prev(nullptr){}
    MyNode(int val, MyNode* nxt, MyNode* prv): value(val), next(nxt), prev(prv){}
    MyNode(int val, MyNode* nxt): value(val), next(nxt), prev(nullptr){}

};


class MyLinkedList {
public:
    MyNode* head;
    MyNode* tail;
    int nodeCount;
    
    MyLinkedList():head(nullptr),tail(nullptr),nodeCount(0){}
    
    int get(int index) {
        int i = 0;
        MyNode* node = head;
        while(node!=nullptr){
            if(i==index)    return node->value;
            node=node->next;
            i++;
        }
        return -1;
    }
    
    void addAtHead(int val) {
        if(head!=nullptr){
            MyNode* newHead = new MyNode(val, head);
            head->prev=newHead;
            head = newHead;
        }else{
            head = new MyNode(val);
            tail = head;
        }
        nodeCount++;
    }
    
    void addAtTail(int val) {
        if(tail!=nullptr){
            MyNode* newTail = new MyNode(val, nullptr, tail);
            tail->next=newTail;
            tail = newTail;
        }else{
            tail=new MyNode(val);
            head=tail;
        }
        nodeCount++;
    }
    
    void addAtIndex(int index, int val) {
        if(index>nodeCount) return;
        if(index==nodeCount){
            addAtTail(val);
            return;
        }
        else if(index==0){
            addAtHead(val);
            return;
        }
        int i = 0;
        MyNode* node = head;
        while(node!=nullptr){
            if(i==index){
                MyNode* newNode = new MyNode(val, node, node->prev);
                node->prev->next = newNode;
                node->prev = newNode;
                nodeCount++;
                return;
            }
            node=node->next;
            i++;
        }
    }
    
    void deleteAtIndex(int index) {
        if(index<0 || index>=nodeCount) return;
        if(index==0){
            MyNode* temp = head;
            head = head->next;
            if(head!=nullptr)   head->prev=nullptr;
            delete temp;
            nodeCount--;
            return;
        }else if(index==nodeCount-1){
            MyNode* temp = tail;
            tail = tail->prev; 
            if(tail!=nullptr)   tail->next=nullptr;
            delete temp;
            nodeCount--;
            return;
        }
        int i = 0;
        MyNode* node = head;
        while(node!=nullptr){
            if(i==index){
                MyNode* prev = node->prev;
                MyNode* next = node->next;
                node->prev=nullptr;
                node->next=nullptr;
            
                next->prev = prev;
                prev->next=next;
                
                delete node;
                
                nodeCount--;
                return;
            }
            node=node->next;
            i++;
        }
    }
};

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList* obj = new MyLinkedList();
 * int param_1 = obj->get(index);
 * obj->addAtHead(val);
 * obj->addAtTail(val);
 * obj->addAtIndex(index,val);
 * obj->deleteAtIndex(index);
 */