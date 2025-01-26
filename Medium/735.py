class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        st = []
        for i in asteroids:
            while st and i < 0 and st[-1] > 0:
                if st[-1] < -i:
                    st.pop()
                    continue
                elif st[-1] == -i:
                    st.pop()
                break
            else:
                st.append(i)
        return st
