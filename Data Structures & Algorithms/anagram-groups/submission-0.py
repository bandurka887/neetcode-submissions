class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        Output = []
        arr = []
        hashset = set()

        for i in strs:
            hash = {}
            if i not in hashset:
              hashset.add(i)
              for n in i:
                  hash[n] = hash.get(n,0) + 1
              arr.append(i)         
              for x in range(len(strs)):
                  if strs.index(i) != x:
                    dict2 = {}
                    for b in strs[x]:
                      dict2[b] = dict2.get(b,0) + 1
                    if dict2 == hash:
                      hashset.add(strs[x])
                      arr.append(strs[x])
            if arr:
              Output.append(arr)
            arr = [] 
        return Output

        