fn disemowel(s: &str) -> String {
	let s = s.to_string(); // type String

	let mut line = String::new(); // out string

	for word in s.chars() {
		match word {
			'a'|'e'|'o'|'y'|'i' => continue,
			'A'|'E'|'I'|'O'|'U'|'Y' => continue,
			_ => line.push(word),
		}
	}

	line
}

fn main() {
	let text = "HellO World";
	println!("{}", disemowel(text));
	assert_eq!(disemowel("hello"), "hll");
	assert_eq!(disemowel("Max KonoVAlov"), "Mx KnVlv");
}