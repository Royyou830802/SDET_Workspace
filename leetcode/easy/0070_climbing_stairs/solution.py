class Solution:

    def CheckInput(self, n:int):
        if not isinstance(n, int):
            raise TypeError("The input is not a integer!")
        elif n < 1:
            raise ValueError("The input value is smaller than 1!")
        elif n > 45:
            raise ValueError("The input value is larger than 45!")
    
    def climbStairs(self, n: int) -> int:
        # Check that n is an int and 1 <= n <= 45
        self.CheckInput(n)

        # Deal with the basic cases when n = 1 or n = 2
        if n <= 2:
            return n
        
        ## Using DP to solve the normal cases
        # Two states to revording the method number of previous 1 and previous 2 steps
        state_prev2_method_num = 1 
        state_prev1_method_num = 2

        # Update the 2 states by the state translate function:
        # New State = Previous 1 step State + Previous 2 step State
        for idx in range(3, n+1):
            new_state = state_prev2_method_num + state_prev1_method_num
            state_prev2_method_num = state_prev1_method_num
            state_prev1_method_num = new_state
        
        # Return the latest state that record the method number of n
        return new_state