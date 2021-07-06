// To declare a Variable

const first_name = "Mohammed";
const middle_name = "Amaan";
const last_name = "Ansari";

const english_age = 18
const islamic_age = 19

// We can declare an array using const and put any type of object inside that array

const arr = [
	'string',
	12,
	function () {
		console.log('My age according to Gregorian Calender is ', english_age);
	}
]

// To access the function inside the array we use array index and () to execute that function

arr[2]();

// To access a value in the array we use console.log(arr[index])

console.log(arr[1]);

// javacript uses for loop just like C

for (let i = 0; i <= arr.length; i += 1) {
	console.log(arr[i]);
}

// String Concatenation

const full_name = first_name + " " + middle_name + " " + last_name;

console.log("Hello there, My name is " + full_name)

// Typecasting 

const x = 21;

// Explicit method

y = String(x);

// implicit method

z = x + "";

console.log(typeof(x));
console.log(typeof(y));
console.log(typeof(z));