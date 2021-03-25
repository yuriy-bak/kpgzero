class Heapq:
    # Код взят из https://github.com/python/cpython/blob/2d1cbe4193499914ccc9d217ea63eb17ff927c91/Lib/heapq.py#L258
    # Поскольку heapq не портирован в Sculpt
    def heapify(self, x):
        """Transform list into a heap, in-place, in O(len(x)) time."""
        n = len(x)
        # Transform bottom-up.  The largest index there's any point to looking at
        # is the largest with a child index in-range, so must have 2*i + 1 < n,
        # or i < (n-1)/2.  If n is even = 2*j, this is (2*j-1)/2 = j-1/2 so
        # j-1 is the largest, which is n//2 - 1.  If n is odd = 2*j+1, this is
        # (2*j+1-1)/2 = j so j-1 is the largest, and that's again n//2-1.
        # Выглядит уродливо, но reversed на платформе не работает
        for i in range((n//2)-1, -1, -1):
            self._siftup(x, i)

    def heappop(self, heap):
        """Pop the smallest item off the heap, maintaining the heap invariant."""
        lastelt = heap.pop()    # raises appropriate IndexError if heap is empty
        if heap:
            returnitem = heap[0]
            heap[0] = lastelt
            self._siftup(heap, 0)
            return returnitem
        return lastelt

    def _siftup(self, heap, pos):
        endpos = len(heap)
        startpos = pos
        newitem = heap[pos]
        # Bubble up the smaller child until hitting a leaf.
        childpos = 2*pos + 1    # leftmost child position
        while childpos < endpos:
            # Set childpos to index of smaller child.
            rightpos = childpos + 1
            if rightpos < endpos and not heap[childpos] < heap[rightpos]:
                childpos = rightpos
            # Move the smaller child up.
            heap[pos] = heap[childpos]
            pos = childpos
            childpos = 2*pos + 1
        # The leaf at pos is empty now.  Put newitem there, and bubble it up
        # to its final resting place (by sifting its parents down).
        heap[pos] = newitem
        self._siftdown(heap, startpos, pos)

    def _siftdown(self, heap, startpos, pos):
        newitem = heap[pos]
        # Follow the path to the root, moving parents down until finding a place
        # newitem fits.
        while pos > startpos:
            parentpos = (pos - 1) >> 1
            parent = heap[parentpos]
            if newitem < parent:
                heap[pos] = parent
                pos = parentpos
                continue
            break
        heap[pos] = newitem

    def heappush(self, heap, item):
        """Push item onto heap, maintaining the heap invariant."""
        heap.append(item)
        self._siftdown(heap, 0, len(heap)-1)
