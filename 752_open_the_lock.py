"""
752. Open the Lock
You have a lock in front of you with 4 circular wheels. 
Each wheel has 10 slots: '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. 
The wheels can rotate freely and wrap around: for example we can turn '9' to be '0', or '0' to be '9'. 
Each move consists of turning one wheel one slot.

The lock initially starts at '0000', a string representing the state of the 4 wheels.

You are given a list of deadends dead ends, meaning if the lock displays any of these codes, 
the wheels of the lock will stop turning and you will be unable to open it.

Given a target representing the value of the wheels that will unlock the lock, 
return the minimum total number of turns required to open the lock, or -1 if it is impossible.


Example 1:
Input: deadends = ["0201","0101","0102","1212","2002"], target = "0202"
Output: 6
Explanation: 
A sequence of valid moves would be "0000" -> "1000" -> "1100" -> "1200" -> "1201" -> "1202" -> "0202".
Note that a sequence like "0000" -> "0001" -> "0002" -> "0102" -> "0202" would be invalid,
because the wheels of the lock become stuck after the display becomes the dead end "0102".


Example 2:
Input: deadends = ["8888"], target = "0009"
Output: 1
Explanation: We can turn the last wheel in reverse to move from "0000" -> "0009".


Example 3:
Input: deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888"
Output: -1
Explanation: We cannot reach the target without getting stuck.

BFS can sove this problem 


        # bfs from target search
        # deadend elimite approach
        # use a visited to avoid duplicate
        # 0000 - [1000, 0100, 0010, 0001, 9000, 0900, 0090, 0009]


"""

from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        from collections import deque

        if "0000" in deadends:
            return -1

        def children(lock):
            """
            function này có mục đích tìm ra các giá trị khả kiến của số lock hiện tại
            ví dụ với trường hợp khởi tạo  0 0 0 0

            + Khi tăng 1 giá trị tại 1 nơi ta có:
                1 0 0 0
                0 1 0 0
                0 0 1 0
                0 0 0 1

            + Khi giảm 1 giá trị tại 1 nơi ta có:
                9 0 0 0
                0 9 0 0
                0 0 9 0
                0 0 0 9

            """
            res = []
            for i in range(4):
                digit = str((int(lock[i]) + 1) % 10)
                res.append(lock[:i] + digit + lock[i + 1 :])

                digit = str((int(lock[i]) + 9) % 10)
                res.append(lock[:i] + digit + lock[i + 1 :])

                """
                khi quay số trên ổ khóa sẽ có các trường hợp đặt biệt là 0, 9 cho trường hợp giảm và tăng 1 số:

                + Khi tăng lên 1 số với trường hợp "9" sẽ thành 10 và nó nằm ngoài các lựa cho cho phép. 
                Theo đúng nguyên lý từ 9 sẽ về lại 0:
                Vậy nên chỉ cần chia lấy dư cho 10 sẽ dc kết quả nằm trong khoảng từ 0-9.
                Ví dụ:  9 tăng 1 thành 10 và 10 % 10 = 0
                        7 tăng 1 thành 8 và 8 % 10 = 8   => (int(lock[i]) + 1) % 10
                
                        
                + Khi giảm 1 số với trường hợp "0" sẽ thành -1 và nó cũng sẽ nằm ngoài các lựa chọn cho phép
                Theo đúng nguyên lý từ 0 sẽ về ngược lại 9:
                Vậy nên chỉ cần cộng thêm 10 số để bỏ đi phần âm và chia lấy dư cho 10.
                Ví dụ:  0 giảm 1 thành -1, lấy -1 + 10 = 9 % 10 = 9
                        7 giảm 1 thành 6, lấy 6 + 10 = 16 % 10 = 6

                        Rút gọn phần -1 + 10 thành +9 => (int(lock[i]) + 9) % 10
                
                """
            return res

        queue = deque()
        queue.append(["0000", 0])
        visit = set(deadends)
        while queue:
            lock, turns = queue.popleft()
            if lock == target:
                return turns
            for child in children(lock):
                if child not in visit:
                    visit.add(child)
                    queue.append([child, turns + 1])
            """
            Ta sử dụng 1 queue để thực hiện kiểm tra các giá trị:
            pop 1 phần từ trong queue và kiểm tra nó có khớp với lock hay không? Nếu khớp trả về số lần mà nó đã đi qua.
            Nếu không khớp thì tìm các giá trị khả kiến tiếp theo của nó rồi thêm vào queue với số lần nó đã đi qua trước đó.
            Visit để tránh các trường hợp lặp lại, do đó thêm deadend vào visit để biến nó thành điều kiện dừng. 
            """

        return -1


sol = Solution()
deadends = ["0201", "0101", "0102", "1212", "2002"]
target = "0202"
print("ans: ", sol.openLock(deadends, target))
