from heapq import heappop, heappush


class Solution(object):
    def getSkyline(self, buildings):
        """
        Solves the Skyline problem in O(n log n) time complexity and O(n) space complexity.

        Algorithm:
        1. Convert buildings into events (start/end points)
        2. Process events in order, maintaining active heights in max heap
        3. Add points to result when max height changes

        Args:
            buildings: List of [left, right, height] building coordinates

        Returns:
            List of [x, height] skyline points
        """
        # Create events from buildings
        events = []
        for left, right, height in buildings:
            # Negative height for start event to handle same position correctly
            events.append((left, -height, right))
            events.append((right, 0, 0))  # End event

        # Sort events by position and height
        events.sort()

        # Initialize result list and max heap for heights
        skyline = []
        active_heights = [(0, float("inf"))]  # (height, ending_x)

        # Process all events
        for pos, neg_height, right in events:
            # Remove ended buildings from heap
            while active_heights[0][1] <= pos:
                heappop(active_heights)

            # Start event: add building to heap
            if neg_height != 0:
                heappush(active_heights, (neg_height, right))

            # If max height changed, add point to skyline
            curr_max_height = -active_heights[0][0]
            if not skyline or skyline[-1][1] != curr_max_height:
                skyline.append([pos, curr_max_height])

        return skyline
