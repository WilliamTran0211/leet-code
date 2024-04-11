"""
950. Reveal Cards In Increasing Order
Medium
Topics
Companies
You are given an integer array deck. There is a deck of cards where every card has a unique integer. 
The integer on the ith card is deck[i].

You can order the deck in any order you want. Initially, all the cards start face down (unrevealed) in one deck.

You will do the following steps repeatedly until all cards are revealed:

Take the top card of the deck, reveal it, and take it out of the deck.
If there are still cards in the deck then put the next top card of the deck at the bottom of the deck.
If there are still unrevealed cards, go back to step 1. Otherwise, stop.
Return an ordering of the deck that would reveal the cards in increasing order.

Note that the first entry in the answer is considered to be the top of the deck.

Example 1:

Input: deck = [17,13,11,2,3,5,7]
Output: [2,13,3,11,5,17,7]
Explanation: 
    We get the deck in the order [17,13,11,2,3,5,7] (this order does not matter), and reorder it.
    After reordering, the deck starts as [2,13,3,11,5,17,7], where 2 is the top of the deck.
    We reveal 2, and move 13 to the bottom.  The deck is now [3,11,5,17,7,13].
    We reveal 3, and move 11 to the bottom.  The deck is now [5,17,7,13,11].
    We reveal 5, and move 17 to the bottom.  The deck is now [7,13,11,17].
    We reveal 7, and move 13 to the bottom.  The deck is now [11,17,13].
    We reveal 11, and move 17 to the bottom.  The deck is now [13,17].
    We reveal 13, and move 17 to the bottom.  The deck is now [17].
    We reveal 17.
    Since all the cards revealed are in increasing order, the answer is correct.


"""

from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:

        increasing = sorted(deck)

        length = len(deck)

        results = [0] * length
        for i in range(len(increasing)):
            cal = i * 2

            if cal < length:
                results[cal] = increasing[i]
            else:
                new_cal = cal

                while new_cal >= length:
                    new_cal = (new_cal % length) * 2 + 1

                results[new_cal] = increasing[i]

        return results

    def deckRevealedDecreasing2(self, deck: List[int]) -> List[int]:
        n = len(deck)
        if n == 1:
            return deck
        res, sorted_deck, next_idx = [None] * n, sorted(deck), 0
        while None in res:
            index_none_dict = [
                index for index, value in enumerate(res) if value is None
            ]
            print(sorted_deck, index_none_dict, next_idx)
            for i in range(next_idx, len(index_none_dict), 2):
                res[index_none_dict[i]] = sorted_deck.pop(0)
            next_idx = 1 if res[index_none_dict[-1]] != None else 0
            print("RES: ", res)
        return res

    def deckRevealedDecreasing3(self, deck: List[int]) -> List[int]:
        import collections

        dq = collections.deque()
        for card in reversed(sorted(deck)):
            dq.rotate()
            dq.appendleft(card)
        return list(dq)


sol = Solution()

# deck = [17, 13, 11, 2, 3, 5, 7]  # ans [2,13,3,11,5,17,7]
# print("ans: ", sol.deckRevealedIncreasing(deck))


# deck = [10, 12, 9, 15, 1, 2, 3, 4]  # ans [1,9,2,12,3,10,4,15]
# print("ans: ", sol.deckRevealedIncreasing(deck))


deck = [17, 13, 11, 2, 3, 5, 7, 1, 6, 15, 12, 8]  # ans [1,8,2,13,3,11,5,17,6,12,7,15]
print("ans: ", sol.deckRevealedDecreasing3(deck))
