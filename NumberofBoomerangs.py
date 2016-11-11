class Solution(object):
    def numberOfBoomerangs(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        c = 0
        for x1,y1 in points:
            dict = {}
            for x2,y2 in points:
                d = (x2-x1)**2+(y2-y1)**2
                if dict.has_key(str(d)):
                    dict[str(d)] = dict[str(d)] + 1
                else:
                    dict[str(d)] = 1
            for v in dict.itervalues():
                c = c +v*(v-1)

        print c


t = Solution()
points = [[0,0],[1,0],[-1,0],[0,1],[0,-1]]

t.numberOfBoomerangs(points)