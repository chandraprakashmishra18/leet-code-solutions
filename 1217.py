class Solution:
    def Min_pos_to_move_chips(self,posittion):

        even = 0
        odd = 0

        for i in posittion:
            if i%2 == 0:
                even +=1

            else:
                odd +=1

        return min(odd,even) 