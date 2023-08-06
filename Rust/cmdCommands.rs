use std::io;

 
fn main() {

    // let int_input: i64 = input.trim().parse().unwrap();
    let mut program = true;
    let text = "help - vyjede seznam příkazů\n
    exit - konec programů\n
    echo - zopakuje input  ";
    println!("{}", text);

    while program == true{
        let mut input = String::new();
        io::stdin().read_line(&mut input).expect("fail to read line");

        let words: Vec<&str> = input.split_whitespace().collect();
        
        if input.trim() == "exit"{
            program = false
        }

        else if input.trim() == "help"{
            println!("{}", text);
        }
        else if let Some(first_word) = words.first(){
            if *first_word == "echo"{
                for word in &words[1..]{
                    echo(word);
                    println!("{:?}", words)
                }
            } 
        else{
                println!("Unknown command!")
            }

        }
    }
}

fn echo(input: &str){
    println!("{}", input);
}