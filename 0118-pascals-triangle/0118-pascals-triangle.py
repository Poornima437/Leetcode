class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        tr=[]
        for i in range(numRows):
            row = [1] * (i + 1)
            for j in range(1,i):
                row[j]=tr[i-1][j-1]+tr[i-1][j]
            tr.append(row)
        return tr


        