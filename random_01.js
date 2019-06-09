var xArray = [];
var yArray = [];
var zArray = [];

for (var i = 0; i < 20; i++) {
	xArray.push(i);
}
for (var i = 0; i < 20; i++) {
	yArray.push(xArray);
}
for (var i = 0; i < 20; i++) {
	zArray.push(yArray);
}

// console.log(zArray);
// console.log(yArray);
// console.log(xArray);

for (var x in xArray) {
	console.log(xArray[x]);
}

console.log("\n--------------------------\n");

for (var y in yArray) {
	console.log(yArray[y].join(" "));
}

console.log("\n--------------------------\n");

for (var z in zArray) {
	console.log(zArray[z].join("\n"));
	console.log("");
}

// console.log("\n--------------------------\n");
var charAmount = 0;

for (var z in zArray) {
	for (var y in zArray[z]) {
		for (var x in yArray[y]) {
			// console.log(x);
			charAmount++;
		}
	}
}

console.log("\n--------------------------\n");
console.log(charAmount + " characters total.");