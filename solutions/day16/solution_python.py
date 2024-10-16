class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # Create a max heap to store counts and associated characters
        heap = []
        if a > 0:
            heap.append((-a, 'a'))  # Use negative to simulate max-heap
        if b > 0:
            heap.append((-b, 'b'))
        if c > 0:
            heap.append((-c, 'c'))
        
        # Convert list into a heap
        heapq.heapify(heap)
        
        result = []
        
        while heap:
            # Pop the most frequent character
            count1, char1 = heapq.heappop(heap)
            
            # If the last two characters in the result are the same as char1, try the next character
            if len(result) >= 2 and result[-1] == result[-2] == char1:
                if not heap:
                    break  # No other characters to choose from
                
                # Get the second most frequent character
                count2, char2 = heapq.heappop(heap)
                result.append(char2)
                
                # If there are still occurrences left, push it back to the heap
                if count2 + 1 < 0:
                    heapq.heappush(heap, (count2 + 1, char2))
                
                # Push the first character back to try it later
                heapq.heappush(heap, (count1, char1))
            else:
                # Otherwise, add the most frequent character to the result
                result.append(char1)
                
                # If there are still occurrences left, push it back to the heap
                if count1 + 1 < 0:
                    heapq.heappush(heap, (count1 + 1, char1))
        
        return ''.join(result)