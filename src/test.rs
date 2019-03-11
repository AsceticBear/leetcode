fn test() {
    let item = "list".to_string();
    let collection = vec!("string".to_string(), "long".to_string(), "list".to_string());
    
    if let Some(found) = collection.iter().find(|&&x| x == item) {
        println!("find it");
    } else {
        println!(" not find it");
    }
}