/**
 * Given an array nums of n integers, are there elements a, b, c in nums
 * such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.
 *
 * Note: The solution set must not contain duplicate triplets.
 */
#[allow(dead_code)]
struct Solution {}

impl Solution {
    #[allow(dead_code)]
    pub fn three_sum(nums: Vec<i32>) -> Vec<Vec<i32>> {
        let mut nums = nums;
        nums.sort();
        println!("sorted arrays: {:?}", nums);
        let mut result = Vec::new();

        for i in 0..nums.len() {
            if i > 0 && nums[i] == nums[i - 1] {
                continue;
            }

            let mut left = i + 1;
            let mut right = nums.len() - 1;

            // println!("For loop ---- left= {:?}, right= {:?}", left, right);
            while left < right {
                let sum = nums[i] + nums[left] + nums[right];
                println!(
                    "i = {:?}, left = {:?}, right = {:?}, sum = {:?}",
                    i, left, right, sum
                );
                if sum > 0 {
                    right = right - 1;
                    continue;
                } else if sum < 0 {
                    left = left + 1;
                    continue;
                } else {
                    let mut temp = Vec::new();
                    temp.push(nums[i]);
                    temp.push(nums[left]);
                    temp.push(nums[right]);
                    result.push(temp);

                    while right > 1 && nums[right - 1] == nums[right] {
                        right = right - 1;
                    }
                    left = left + 1;
                    right = right - 1;
                }
            }
        }
        result
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_three_sum() {
        let given_arrays1 = vec![-1, 0, 1, 2, -1, -4];
        let mut solution = Vec::new();
        solution.push(vec![-1, -1, 2]);
        solution.push(vec![-1, 0, 1]);
        assert_eq!(Solution::three_sum(given_arrays1), solution);

        let given_arrays2 = vec![0, 0, 0, 0];
        assert_eq!(Solution::three_sum(given_arrays2), vec![vec!(0, 0, 0)]);

        // let given_arrays3 = vec![];
        // assert_eq!(Solution::three_sum(given_arrays3), vec![]);

        let given_arrays4 = vec![-2, 0, 0, 2, 2];
        assert_eq!(Solution::three_sum(given_arrays4), vec![vec!(-2, 0, 2)]);
    }
}
