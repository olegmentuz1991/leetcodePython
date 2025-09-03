class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for i in range(len(image)):
            row = []
            for j in range(len(image[i])-1,-1,-1):
                row.append(1 - image[i][j])
            result.append(row)
        return result


s = Solution()
s.flipAndInvertImage(([[1,1,0],[1,0,1],[0,0,0]]))