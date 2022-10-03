class Solution {
    public int smallestEvenMultiple(int n) {
    
       int lcm = (n> 2) ? n : 2;

    while(true) {
      if( lcm % n == 0 && lcm % 2 == 0 )
      break;
      ++lcm;
    }
        return lcm;
    }
}
