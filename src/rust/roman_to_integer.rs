/**
 * Symbol       Value
 * I             1
 * V             5
 * X             10
 * L             50
 * C             100
 * D             500
 * M             1000
 *
 * I can be placed before V (5) and X (10) to make 4 and 9.
 * X can be placed before L (50) and C (100) to make 40 and 90.
 * C can be placed before D (500) and M (1000) to make 400 and 900.
 */

#[allow(dead_code)]
struct Solution {}

impl Solution {
    #[allow(dead_code)]
    pub fn roman_to_int(mut s: String) -> i32 {
        let mut result = 0;
        let mut temp: char = 'a';
        while let Some(c) = s.pop() {
            match c {
                'I' => {
                    if temp == 'V' || temp == 'X' {
                        result = result - 1;
                    } else {
                        result = result + 1;
                    }
                }
                'V' => result = result + 5,
                'X' => {
                    if temp == 'L' || temp == 'C' {
                        result = result - 10;
                    } else {
                        result = result + 10;
                    }
                }
                'L' => result = result + 50,
                'C' => {
                    if temp == 'D' || temp == 'M' {
                        result = result - 100;
                    } else {
                        result = result + 100;
                    }
                }
                'D' => result = result + 500,
                'M' => result = result + 1000,
                _ => unimplemented!(),
            }
            temp = c;
        }
        result
    }
}

#[cfg(test)]
mod tests {

    use super::Solution;

    #[test]
    fn test() {
        let str1 = String::from("III");
        assert_eq!(Solution::roman_to_int(str1), 3);

        let str2 = String::from("IV");
        assert_eq!(Solution::roman_to_int(str2), 4);

        let str3 = String::from("IX");
        assert_eq!(Solution::roman_to_int(str3), 9);

        let str4 = String::from("LVIII");
        assert_eq!(Solution::roman_to_int(str4), 58);

        let str5 = String::from("MCMXCIV");
        assert_eq!(Solution::roman_to_int(str5), 1994);
    }
}
