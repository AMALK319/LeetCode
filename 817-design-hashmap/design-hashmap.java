
class MyHashMap {

    ArrayList<LinkedList<Pair>> list ;
    int size;
    float loadFactor = 0.5f;

    public MyHashMap() {
        list = new ArrayList<>(10);
        for(int i=0; i<10; i++){
            list.add(new LinkedList<>());
        }

    }
    
    public void put(int key, int value) {
        int hash = Math.abs(Integer.valueOf(key).hashCode() % list.size());
        LinkedList<Pair> linkedList = list.get(hash);
        for(Pair pair: linkedList){
            if(pair.key == key) {
                pair.value = value;
                return;
            }
        }

       /*  if( ((float)size / list.size()) > loadFactor) {
            this.resize();
            hash = Integer.valueOf(key).hashCode() % list.size(); // Recalculate hash after resizing
            linkedList = list.get(hash); // Get the new bucket after resizing
        } */

        linkedList.add(new Pair(key, value));
        size++;
        
    }
    
    public int get(int key) {
        int hash = Math.abs(Integer.valueOf(key).hashCode()%list.size());
        LinkedList<Pair> linkedList = list.get(hash);
        for(Pair pair: linkedList){
            if(pair.key == key) {
               return pair.value;
            }
        }
        return -1;
    }
    
    public void remove(int key) {
        int hash = Math.abs(Integer.valueOf(key).hashCode()%list.size());
        LinkedList<Pair> linkedList = list.get(hash);
        Pair target = null;
        for(Pair pair: linkedList){
            if(pair.key == key) {
                target = pair;
            }
        }
        linkedList.remove(target);
        size--;
       
    }

    private void resize(){

        ArrayList<LinkedList<Pair>> old = list;
        list = new ArrayList<>();

        size = 0;

        for(int i=0; i<old.size()*2; i++){
            list.add(new LinkedList<>());
        }

        for(int i=0; i<old.size(); i++){
            for(Pair pair : old.get(i)){
                put(pair.key, pair.value);
            }
        }

    }

    class Pair {
        private int key;
        private int value;

        Pair(int key, int value){
            this.key = key;
            this.value = value;
        }
    }
}

/**
 * Your MyHashMap object will be instantiated and called as such:
 * MyHashMap obj = new MyHashMap();
 * obj.put(key,value);
 * int param_2 = obj.get(key);
 * obj.remove(key);
 */