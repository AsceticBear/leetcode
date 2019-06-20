/// Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.

/// Example
/// Input:
///      nums1 = [1,2,3,0,0,0], m = 3
///      nums2 = [2,5,6],       n = 3
/// Output:
///      [1,2,2,3,5,6]

#[allow(dead_code)]
struct Solution {}

impl Solution {
    #[allow(dead_code)]
    pub fn merge(nums1: &mut Vec<i32>, m: i32, nums2: &mut Vec<i32>, _n: i32) -> Vec<i32> {
        nums1.truncate(m as usize);
        nums1.append(nums2);
        nums1.sort();
        nums1.to_vec()
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_merge_1() {
        let mut nums1 = vec![1, 2, 3, 0, 0, 0];
        let m = 3;
        let mut nums2 = vec![2, 5, 6];
        let n = 3;

        let output = vec![1, 2, 2, 3, 5, 6];
        assert_eq!(output, Solution::merge(&mut nums1, m, &mut nums2, n));
    }

    #[test]
    fn test_merge_2() {
        let mut nums1 = vec![-1, 0, 0, 3, 3, 3, 0, 0, 0];
        let m = 6;
        let mut nums2 = vec![1, 2, 2];
        let n = 3;

        let output = vec![-1, 0, 0, 1, 2, 2, 3, 3, 3];
        assert_eq!(output, Solution::merge(&mut nums1, m, &mut nums2, n));
    }
}
