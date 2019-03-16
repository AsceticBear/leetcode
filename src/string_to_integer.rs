#[allow(dead_code)]
struct Solution {}

impl Solution {
    #[allow(dead_code)]
    pub fn my_atoi(str: String) -> i32 {
        let a = &mut str.trim_start().split_whitespace();
        let b = a.next().unwrap_or("");

        if b.len() == 0 {
            return 0;
        }

        let mut sign: i64 = 1;
        let mut sum: i64 = 0;
        let mut start = 0;
        if b.chars().nth(0) == Some('-') {
            sign = -1;
            start = 1;
        }
        if b.chars().nth(0) == Some('+') {
            sign = 1;
            start = 1
        }

        for i in b.chars().skip(start) {
            if !i.is_digit(10) {
                break;
            }
            sum = sum * 10 + i.to_digit(10).unwrap_or(0) as i64;
            if sum * sign > std::i32::MAX.into() {
                return std::i32::MAX;
            }
            if sum * sign < std::i32::MIN.into() {
                return std::i32::MIN;
            }
        }
        return (sign * sum) as i32;
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_my_atoi() {
        let t1 = String::from("42");
        assert_eq!(Solution::my_atoi(t1), 42);

        let t2 = String::from("   -42");
        assert_eq!(Solution::my_atoi(t2), -42);

        let t3 = String::from("4193 with words");
        assert_eq!(Solution::my_atoi(t3), 4193);

        let t4 = String::from("words and 987");
        assert_eq!(Solution::my_atoi(t4), 0);

        let t5 = String::from("-91283472332");
        assert_eq!(Solution::my_atoi(t5), -2147483648);

        let t6 = String::from("");
        assert_eq!(Solution::my_atoi(t6), 0);

        let t6 = String::from(" ");
        assert_eq!(Solution::my_atoi(t6), 0);

        let t7 = String::from("3.14159");
        assert_eq!(Solution::my_atoi(t7), 3);

        let t8 = String::from("+1");
        assert_eq!(Solution::my_atoi(t8), 1);
    }
}
