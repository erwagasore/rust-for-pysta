fn main() {
    for number in 1..101 {
        if number % 5 == 0 && number % 3 == 0 {
            println!("Fizzbuzz");
        }
        else if number % 5 == 0 {
            println!("Buzz");
        }
        else if number % 3 == 0 {
            println!("Fizz");
        }
        else {
            println!("{}", number);
        }
    }
}
