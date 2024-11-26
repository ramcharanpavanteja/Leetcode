class Solution {
    public int mySqrt(int x) {
        if (x < 2) {
            return x; // The square root of 0 is 0 and 1 is 1
        }

        int left = 0;
        int right = x;
        int ans = 0;

        while (left <= right) {
            int mid = left + (right - left) / 2;
            long midSquared = (long) mid * mid; // Use long to prevent overflow

            if (midSquared == x) {
                return mid; // Exact square root found
            } else if (midSquared < x) {
                ans = mid; // Potential answer
                left = mid + 1; // Move to the right half
            } else {
                right = mid - 1; // Move to the left half
            }
        }

        return ans;
    }
}