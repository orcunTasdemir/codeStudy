from typing import List


class Solution:
    def multiSplit(self, s:str, dels : List) -> List:
        splits = self.getEncounters(s, dels)
        oneChosen = splits[0]
        splits.pop(0)
        for split in splits:
            print(split)
            s = s.replace(split, oneChosen)
        listy = s.split(oneChosen)
        return listy

    def getEncounters(self, s : str, dels : List) -> List[List]:
        encounters = []
        # given 2 delimiters, I want to split starting from the biggest versions of their combined string into the smaller versions
        for idx in range(len(s)):
            for delidx in range(len(dels)):
                # if the first character of the delimiter
                # is encountered, save that 
                if s[idx] == dels[delidx][0]:
                    if s[idx: idx + len(dels[delidx])] == dels[delidx]:
                        # save the index it is encountered
                        encounters.append([idx, idx + len(dels[delidx])])
        print(encounters)
        splits = []
        for idx in range(len(encounters)):
            if idx < len(encounters)-1:
                if (encounters[idx][1] > encounters[idx+1][0]) and (encounters[idx][1] < encounters[idx+1][1]) :
                    # encounters[idx][1] = encounters[idx+1][1]
                    print(encounters[idx][0])
                    print(encounters[idx+1][1])
                    splits.append(s[encounters[idx][0]:encounters[idx+1][1]])
                else:
                    splits.append(s[encounters[idx][0]:encounters[idx][1]])
            else:
                splits.append(s[encounters[idx][0]:encounters[idx][1]])
        print(splits)
        return splits
        
s = Solution()
sentence = 'this is a test, this is only a test!'
delimiters = ['is', 'a']
print(s.multiSplit(sentence, delimiters))
                    
        
