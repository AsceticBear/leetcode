/**
 * Given an array of non-negative integers, you are initially positioned at the first index of the array.
 *
 * Each element in the array represents your maximum jump length at that position.
 *
 * Determine if you are able to reach the last index.
 *
 */

#[allow(dead_code)]
struct Solution {}

impl Solution {
    #[allow(dead_code)]
    pub fn can_jump(nums: Vec<i32>) -> bool {
        let nums_len = nums.len() as u32;
        if nums_len == 0 {
            return false;
        }

        let mut current_max_reach = 0;
        for i in 0..nums_len {
            if current_max_reach >= nums_len - 1 {
                return true;
            }

            if i > current_max_reach {
                return false;
            }

            let step = nums[i as usize];
            let reached = i + step as u32;
            if reached >= current_max_reach {
                current_max_reach = reached;
            }
        }
        false
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_can_jump() {
        let v1 = vec![2, 3, 1, 1, 4];
        assert_eq!(Solution::can_jump(v1), true);

        println!("=================");

        let v2 = vec![3, 2, 1, 0, 4];
        assert_eq!(Solution::can_jump(v2), false);

        println!("=================");

        let v3 = vec![0];
        assert_eq!(Solution::can_jump(v3), true);

        println!("=================");

        let v4 = vec![0, 2, 3];
        assert_eq!(Solution::can_jump(v4), false);

        println!("=================");

        let v5 = vec![1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
        assert_eq!(Solution::can_jump(v5), true);
    }
}
