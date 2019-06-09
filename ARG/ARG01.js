const s = require("sleep");

let welcomeTitle = "SCP FOUNDATION O5 ACESS TERIMNAL";
let passwordPrompt = "PASSWORD:";
let passwordAccept = "PASSWORD ACCEPTED"

// process.stdout.write("\x1b[2J" + "\n\n" + "\x1b[41C" + "\x1b[1m" + "\x1b[4m" + "SCP FOUNDATION O5 ACESS TERMINAL" + "\x1b[0m");
process.stdout.write("\x1b[2J" + "\n\n" + "\x1b[41C" + "\x1b[1m" + "\x1b[4m");
for (var i = 0; i < welcomeTitle.length; i++) {
	process.stdout.write(welcomeTitle[i]);
	s.msleep(50);
}
process.stdout.write("\x1b[0m");



process.stdout.write("\x1b[5;53f");
for (var i = 0; i < passwordPrompt.length; i++) {
	process.stdout.write(passwordPrompt[i]);
	s.msleep(50);
}
process.stdout.write("\x1b[0m");



s.msleep(50);
process.stdout.write("\x1b[6;52f" + "[         ]\n\n" + "\x1b[0m");



s.sleep(1);
let stars = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '];

for (var i = 0; i < 9; i++) {
	stars[i] = '*'
	process.stdout.write("\x1b[6;52f" + `[${stars.join('')}]\n\n` + "\x1b[0m");
	s.msleep(Math.floor(Math.random() * 500))
}

s.msleep(1000);



process.stdout.write("\x1b[48C" + "\x1b[32m");
for (var i = 0; i < passwordAccept.length; i++) {
	process.stdout.write(passwordAccept[i]);
	s.msleep(50);
}
process.stdout.write("\x1b[0m");
// s.msleep(1000);



for (var i = 0; i < 10; i++) {
	process.stdout.write("\x1b[9;57f" + "/\n\n" + "\x1b[0m");
	s.msleep(100);
	process.stdout.write("\x1b[9;57f" + "-\n\n" + "\x1b[0m");
	s.msleep(100);
	process.stdout.write("\x1b[9;57f" + "\\\n\n" + "\x1b[0m");
	s.msleep(100);
	process.stdout.write("\x1b[9;57f" + "|\n\n" + "\x1b[0m");
	s.msleep(100);
}

process.stdout.write("\x1b[2J" + "\n\n" + "\x1b[50C" + "\x1b[1m" + "\x1b[4m" + "WELCOME, O5-██" + "\x1b[0m" + "\n\n\n\n\n\n\n\n\n\n");