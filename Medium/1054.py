import heapq
from typing import Counter, List


class Solution:
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        count = Counter(barcodes)
        max_heap = [(-freq, barcode) for barcode, freq in count.items()]
        heapq.heapify(max_heap)
        result = []
        prev_freq, prev_barcode = 0, None

        while max_heap:
            freq, barcode = heapq.heappop(max_heap)
            result.append(barcode)
            if prev_freq < 0:
                heapq.heappush(max_heap, (prev_freq, prev_barcode))

            prev_freq, prev_barcode = freq + 1, barcode

        return result
