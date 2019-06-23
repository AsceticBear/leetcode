#[allow(dead_code)]
struct Solution {}

impl Solution {
    #[allow(dead_code)]
    pub fn is_match(s: String, p: String) -> bool {
        if p.is_empty() {
            return s.is_empty();
        }

        let mut first_match = false;
        if let (Some(s), Some(p)) = (s.chars().nth(0), p.chars().nth(0)) {
            first_match = s == p || p == '.';
        }
        if p.chars().nth(1) == Some('*') {
            return (first_match && Solution::is_match(s[1..].to_string(), p.to_string()))
                || Solution::is_match(s.to_string(), p[2..].to_string());
        }
        return first_match && Solution::is_match(s[1..].to_string(), p[1..].to_string());
    }
}

#[cfg(test)]
mod tests {
    use super::Solution;

    #[test]
    fn test_is_match() {
        // Example 1
        let s = "aa";
        let p = "a";
        assert_eq!(false, Solution::is_match(s.to_owned(), p.to_owned()));

        // Example 2
        let s = "aa";
        let p = "a*";
        assert_eq!(true, Solution::is_match(s.to_owned(), p.to_owned()));

        // // Example 3
        let s = "ab";
        let p = ".*";
        assert_eq!(true, Solution::is_match(s.to_owned(), p.to_owned()));

        // // Example 4
        let s = "aab";
        let p = "c*a*b";
        assert_eq!(true, Solution::is_match(s.to_owned(), p.to_owned()));

        // // Example 5
        let s = "mississippi";
        let p = "mis*is*p*.";
        assert_eq!(false, Solution::is_match(s.to_owned(), p.to_owned()));
    }
}
