'''2225. Find Players With Zero or One Losses
'''
class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        winners = []
        losses = []

        tmp_list = {}

        for match in matches:
            tmp_list[match[0]] = tmp_list.get(match[0], 0)
            tmp_list[match[1]] = tmp_list.get(match[1], 0) + 1

        for tmp_k in tmp_list.keys():
            if tmp_list[tmp_k] == 0:
                winners.append(tmp_k)
            elif tmp_list[tmp_k] == 1:
                losses.append(tmp_k)

        winners.sort()
        losses.sort()

        return [winners, losses]
        