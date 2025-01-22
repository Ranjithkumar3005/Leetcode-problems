class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """
        h = {}
        for i in range(0, len(list1)):
            if list1[i] in list2:
                h[list1[i]] = i + list2.index(list1[i])
        mini = min(list(h.values()))
        dum = []
        for i in h:
            if h[i] == mini:
                dum.append(i)
        return dum
