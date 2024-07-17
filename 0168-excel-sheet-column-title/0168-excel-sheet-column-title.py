class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
      s = ""
      while columnNumber > 0 :
        rem = columnNumber%26
        if rem == 0:
            rem = 26
            columnNumber-=1
        s = chr(rem+64)+s
        columnNumber//=26
      return s

      