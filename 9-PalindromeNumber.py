# 9. Palindrome Number

class Solution:
  def isPalindrome(self, x: int) -> bool:    
    string: str = str(x)
    reversed_string: str = string[::-1]

    return string == reversed_string