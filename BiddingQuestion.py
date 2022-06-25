from typing import List


class Solution:

    def parseBidsFile(self, text_file) -> List[List[int]]:
        with open(text_file, "r") as bids_txt:
            lines = bids_txt.readlines()
            numBids = int(lines[0])
            # numAttributes = int(lines[1])
            bids = [[int(x) for x in lines[line_num].strip(
                '\n').split(' ')] for line_num in range(2, numBids + 2)]
            totalShares = int(lines[numBids + 2])
        return bids, totalShares

    def getUnallottedUsers(self, bids: List[List[int]], totalShares: int) -> List[int]:
        # First group bidders into a list of lists where they are ordered by the amount they bid for the 2nd index
        # bids.sort(key=lambda x: x[2])
        unallottedUsers = [bid[0] for bid in bids if bid[1] > 0]
        # print(unallottedUsers)
        groups = {}
        for bid in bids:
            groups.setdefault(bid[2], []).append(bid)
            # print(groups)
        bids_grouped = list(groups.values())
        # print(bids_grouped)
        # now we process each of these groups until either the shares or the bidders run out
        for group in bids_grouped:
            # we check for if there is no shares left to sale at the beginnig of each group
            if(totalShares == 0):
                return unallottedUsers
            # if there are shares left and the group is larger than one bidder we want to do iterative selling
            if len(group) > 1:
                # sort the group by increasing-order timestamp
                group.sort(key=lambda x: x[3])
                # totalRequested = sum([bidder[1] for bidder in group])
                removeds = []
                while(totalShares > 0):
                    for removed in removeds:
                        group.remove(removed)
                        removeds = []
                    for bidder in group:
                        if(totalShares > 0):
                            if(bidder[1] > 0):
                                unallottedUsers.remove(bidder[0])
                                totalShares -= 1
                                bidder[1] -= 1
                            else:
                                removeds.append(bidder)
                                # print(removeds)
                # otherwise we want to just sell however many shares the highest bidder at this time is requesting
            else:
                unallottedUsers.remove(group[0][0])
                if(group[0][1] >= totalShares):
                    return unallottedUsers
                # otherwise we can  continue after subtracting the sold shares
                totalShares -= group[0][1]

        return unallottedUsers


s = Solution()
print(s.getUnallottedUsers(*s.parseBidsFile("BiddingQuestionInput.txt")))
# print(bids, totalShares)
