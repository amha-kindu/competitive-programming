class MyCircularDeque {
    list<int> queueFront;
    list<int> queueLast;
    int capacity;
    int size;
public:
    MyCircularDeque(int k) {
        capacity=k;
        size=0;
    }
    
    bool insertFront(int value) {
        if(size<capacity){
            queueFront.push_back(value);
            size++;
            return true;
        }else{
            return false;
        }
    }
    
    bool insertLast(int value) {
        if(size<capacity){
            queueLast.push_back(value);
            size++;
            return true;
        }else{
            return false;
        }
    }
    
    bool deleteFront() {
        if(queueFront.size()>0){
            queueFront.pop_back();
            size--;
            return true;
        }else if(queueLast.size()>0){
            queueLast.pop_front();
            size--;
            return true;
        }
        return false;
    }
    
    bool deleteLast() {
        if(queueLast.size()>0){
            queueLast.pop_back();
            size--;
            return true;
        }else if(queueFront.size()>0){
            queueFront.pop_front();
            size--;
            return true;
        }
        return false;
    }
    
    int getFront() {
        if(queueFront.size()>0){
            return queueFront.back();    
        }else if(queueLast.size()>0){
            return queueLast.front();
        }
        return -1;   
    }
    
    int getRear() {
        if(queueLast.size()>0){
            return queueLast.back();    
        }else if(queueFront.size()>0){
            return queueFront.front();
        }
        return -1;
    }
    
    bool isEmpty() {
        return queueLast.empty() && queueFront.empty();
    }
    
    bool isFull() {
        return size==capacity;
    }
};

/**
 * Your MyCircularDeque object will be instantiated and called as such:
 * MyCircularDeque* obj = new MyCircularDeque(k);
 * bool param_1 = obj->insertFront(value);
 * bool param_2 = obj->insertLast(value);
 * bool param_3 = obj->deleteFront();
 * bool param_4 = obj->deleteLast();
 * int param_5 = obj->getFront();
 * int param_6 = obj->getRear();
 * bool param_7 = obj->isEmpty();
 * bool param_8 = obj->isFull();
 */