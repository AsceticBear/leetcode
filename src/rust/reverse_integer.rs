#[allow(dead_code)]
struct Solution {}

impl Solution {
    #[allow(dead_code)]
    pub fn reverse(x: i32) -> i32 {
        x.signum()
            * x.abs()
                .to_string()
                .chars()
                .rev()
                .collect::<String>()
                .parse::<i32>()
                .unwrap_or(0)
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test() {
        let n1 = 123;
        assert_eq!(Solution::reverse(n1), 321);

        let n2 = -123;
        assert_eq!(Solution::reverse(n2), -321);

        let n3 = 120;
        assert_eq!(Solution::reverse(n3), 21);
    }
}
