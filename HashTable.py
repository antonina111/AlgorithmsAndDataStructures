class HashTable(object):
    
    def __init__(self, size):
        
        self.size = size
        self.slots = [None] * self.size
        self.data = [None] * self.size
        
    def put(self,key,data):
        
        #create HashValue
        hashValue = self.hashFunction(key, len(self.slots))
        
        #if slot is ampty - use this slot
        if self.slots[hashValue]==None:
            self.slots[hashValue] = key
            self.data[hashValue] = data
            
        else:
            if self.slots[hashValue] == key:
                self.data[hashValue] = data
            #if slot is not empty - calculate new hash value
            else:
                nextslot = self.rehash(hashValue,len(self.slots))
                
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    nextslot = self.rehash(nextslot,len(self.slots))
                
                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data
            
        
        
    def hashFunction(self,key,size):
        return key%size
    
    def rehash(self,oldhashval, size):
        return (oldhashval)+1%size
    
    
    def get(self,key):
        
        startSlot = self.hashFunction(key, len(self.slots))
        data = None
        
        stop = False
        found = False
        position = startSlot
        
        while self.slots[position] != None and not found and not stop:
            
            if self.slots[position] == key:
                found = True
                data = self.data[position]
                
            else:
                position = self.rehash(position, len(self.slots))
                if position == startSlot:
                    stop = True
        return data
    
    
    
    def __getitem__(self,key):
        return self.get(key)
    
    def __setitem__(self,key,data):
        self.put(key,data)