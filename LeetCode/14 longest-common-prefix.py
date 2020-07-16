class Solution:
    def longestCommonPrefix(self, strs) -> str:
        if not strs or len(strs) == 0: return ""
        if len(strs) == 1: return strs[0]
        return self.longestCommonPrefixWithStr(strs[0], strs[1:len(strs)])

    def longestCommonPrefixWithStr(self, str1, strs:list):
        if str1 == "": return ""
        if len(strs) == 1:
            str2 = strs[0]
            i = 0
            preStr = ""
            while i < len(str1) and i < len(str2):
                if str1[i] == str2[i]:
                    preStr += str2[i]
                    i += 1
                else:
                    break
            return preStr
        else:
            return self.longestCommonPrefixWithStr(str1, [self.longestCommonPrefixWithStr(strs[0], strs[1:len(strs)])])

if __name__ == '__main__':
    print(Solution().longestCommonPrefix(["bc", "aba", "aaa"]))
