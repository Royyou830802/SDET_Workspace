class Solution:
    def check_input_format(self, s: str):
        if type(s) != str:
            raise TypeError("Input should be a string.")
        elif any([x for x in s if x not in "()[]{}"]):
            raise ValueError("Input should only contain parentheses.")
        elif len(s) > 10**4:
            raise ValueError("Input length should be no more than 10^4.")
        elif len(s) < 1:
            raise ValueError("Input length should be larger than 0.")
        
    def isValid(self, s: str) -> bool:
        '''
        This function is used for validating if the parenthese is balance.
        Input: a string that only include the "()[]{}"
        Output: True -> is, False -> is not. 
        '''
        self.check_input_format(s)
        # hashmap to store the relationship between
        hashmap = {")": "(", "]": "[", "}": "{"}
        # stack to store the "(,[,{"
        stack = []
        for c in s:
            if c not in ")]}":
                # if character is the begin of the quote, store it in the stack.
                stack.append(c)
            else:
                # if the c is the end of a quote, check if it can pair with the last c in the stack
                if not stack or stack.pop() != hashmap[c]:
                    # if cannot pair, return False immediately. 
                    return False
        if stack == []:
            # After checking all c in s, if the stack is empty,
            # means that all quote are pairable, return ture.
            return True
        else:
            # If stack is not empty, means some c can not pair, return False.
            return False
                
