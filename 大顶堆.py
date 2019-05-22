class MaxHeap:
    def __init__(self,cap):
        self.cap = cap
        self.heap = [None for _ in range(cap+1)]
        self.idx = 0
    
    def create(self,a:list):
        if not list:
            return
        self.heap = [None for _ in range(len(a)+1)]
        self.cap = len(a)
        self.idx = len(a)
        for i in range(len(a)):
            self.heap[i+1] = a[i]
        p = self.idx>>1
        while p > 0:
            l = 2*p
            r = 2*p+1
            kMax = l
            if r <= self.idx and self.heap[r] > self.heap[kMax]:
                kMax = r
            if self.heap[kMax] <= self.heap[p]:
                p -= 1
                continue 
            t = self.heap[kMax]
            self.heap[kMax] = self.heap[p]
            self.heap[p] = t

            p2 = kMax

            while p2<=self.idx:
                l2 = 2*p2
                r2 = 2*p2+1
                kMax2 = l2
                if l2 > self.idx:
                    break
                if r2<=self.idx and self.heap[r2] > self.heap[l2]:
                    kMax2 = r2
                if self.heap[p2] >= self.heap[kMax2]:
                    break
                t2 = self.heap[p2]
                self.heap[p2] = self.heap[kMax2]
                self.heap[kMax2] = t2
                p2 = kMax2

            p -= 1

    
    def push(self,val):
        if val == None:
            return
        if self.idx >= self.cap:
            return
        self.idx += 1
        self.heap[self.idx] = val
        
        p = self.idx>>1
        while p > 0:
            l = 2*p
            r = 2*p+1
            kMax = l
            if r <= self.idx and self.heap[r] > self.heap[kMax]:
                kMax = r
            if self.heap[kMax] <= self.heap[p]:
                break
            t = self.heap[kMax]
            self.heap[kMax] = self.heap[p]
            self.heap[p] = t
            p = p >> 1

    
    def pop(self):
        if self.idx == 0:
            return
        pop = self.heap[1]
        self.heap[1] = self.heap[self.idx]
        self.heap[self.idx] = None
        self.idx -= 1
        
        p = 1
        while p <= self.idx:
            l = 2*p
            r = 2*p+1
            if l > self.idx:
                break
            kMax = l
            if r <= self.idx and self.heap[r] > self.heap[kMax]:
                kMax = r
            if self.heap[kMax] <= self.heap[p]:
                break 
            t = self.heap[kMax]
            self.heap[kMax] = self.heap[p]
            self.heap[p] = t
            p = kMax

        return pop


    def count(self):
        return self.idx

    
    def heapSort(self):
        k = self.idx
        for _ in range(k):
            t = self.pop()
            self.heap[self.idx+1] = t

        print(self.heap)

heap = MaxHeap(10)

heap.create([1,2,3,4,5,6,7])

# for i in range(9):
#     heap.push(i)

print(heap.heap)

heap.heapSort()

# for i in range(9):
#     print(heap.pop())