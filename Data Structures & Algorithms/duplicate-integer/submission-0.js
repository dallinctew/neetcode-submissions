class Solution {
    /**
     * @param {number[]} nums
     * @return {boolean}
     */
    hasDuplicate(nums) {
        const seen = [];
        while (nums.length > 0) {
            const x = nums.pop(); 
            if (seen.indexOf(x) !== -1) return true;
            seen.push(x);
        }
        return false;
    }
}
