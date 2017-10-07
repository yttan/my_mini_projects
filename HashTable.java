
public class HashTable extends Object{//
	private int size;  //table size

	private Object[] keys;
	private Object[] values;
	private int items; // the number of all the objects put in
	public HashTable(int r){
		keys=new Object[r];
		values =new Object[r];
		items=0;
		size=r;
	}
	public HashTable(){
		size=2;
		keys=new Object[size];
		values =new Object[size];
		items=0;
		
	}
	
	public int size(){
		return items;
	}
	private void resize(int r){
		HashTable newhashtable;
		newhashtable = new HashTable(r);
		for (int i=0;i<size;i++)
			if (keys[i]!=null) {
				newhashtable.put(keys[i],values[i]);
			}
		keys = newhashtable.keys;
		values = newhashtable.values;
		size = newhashtable.size;
	}

	private int hash(Object key){
		return (key.hashCode() & 0x7fffffff) % size;
	}

	public void put(Object key, Object val){
		synchronized(this){
		if (items>=(size/2)) {
			resize(2*size);
		}
		int i;
		for (i=hash(key); keys[i]!=null;i =(i+1) % size){  //use linear probing to avoid collision
			if (keys[i].equals(key)){   //already have the key
				values[i]=val;
				return;
			}
		}
		keys[i]=key;
		values[i]=val;
		items++;
	}
	}
	public Object get(Object key){
		synchronized(this){
		int i;
		for (i=hash(key); keys[i]!=null;i=(i+1) % size){
			if(keys[i].equals(key))
				return values[i];
		}
		return null;
	}
	}
	
}
