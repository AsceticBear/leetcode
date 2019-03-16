#[allow(dead_code)]
struct Solution {}

impl Solution {
    #[allow(dead_code)]
    pub fn num_jewels_in_stones(j: String, s: String) -> i32 {
        use std::collections::HashSet;
        let jewels: HashSet<char> = j.chars().collect();
        s.chars().into_iter().filter(|x| jewels.contains(x)).count() as i32
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test() {
        let j1 = String::from("aA");
        let s1 = String::from("aAAbbbb");
        assert_eq!(Solution::num_jewels_in_stones(j1, s1), 3);

        let j2 = String::from("z");
        let s2 = String::from("ZZ");
        assert_eq!(Solution::num_jewels_in_stones(j2, s2), 0);

        let j3 = String::from("ngm");
        let s3 = String::from("kxg");
        assert_eq!(Solution::num_jewels_in_stones(j3, s3), 1);
    }
}
