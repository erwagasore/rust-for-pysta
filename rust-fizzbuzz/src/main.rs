fn main() {
    for number in 1..101 {
        let x;

        let fzb = if number % 3 == 0 && number & 5 == 0 {
            "FizzBuzz"
        } else if number % 3 == 0 {
            "Fizz"
        } else if number % 5== 0 {
            "Buzz"
        } else {
            x = number.to_string();
            &*x
        };

        println!("{}", fzb);
    };
}
