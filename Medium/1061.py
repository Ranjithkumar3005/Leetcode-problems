class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        dum = []

        for i in range(len(s1)):
            found = False
            for group in dum:
                # Check if s1[i] or s2[i] is in an existing group
                if s1[i] in group or s2[i] in group:
                    group.add(s1[i])
                    group.add(s2[i])
                    found = True
                    break
            if not found:
                dum.append(set([s1[i], s2[i]]))  # New group for this pair

        merged_groups = []
        while dum:
            group = dum.pop()
            for other in dum[:]:
                if group & other:  # If there's an intersection
                    group |= other
                    dum.remove(other)
            merged_groups.append(sorted(group))  # Sort group lexicographically

        char_map = {}
        for group in merged_groups:
            min_char = group[0]  # Smallest character in sorted group
            for char in group:
                char_map[char] = min_char

        result = "".join(char_map.get(ch, ch) for ch in baseStr)

        return result
