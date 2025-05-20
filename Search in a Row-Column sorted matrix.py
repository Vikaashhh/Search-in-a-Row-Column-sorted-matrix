class Solution:
    def matSearch(self, mat, x):
        n = len(mat)        # rows
        m = len(mat[0])     # columns
        
        i, j = 0, m - 1     # top-right se search start karo
        
        while i < n and j >= 0:
            if mat[i][j] == x:
                return 1    # element mil gaya
            elif mat[i][j] > x:
                j -= 1      # left move karo
            else:
                i += 1      # neeche move karo

        return 0            # element nahi mila
