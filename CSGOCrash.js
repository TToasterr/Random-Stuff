var stdin = process.openStdin();
var games = 0;
var wins = 0;
var losses = 0;

var cash = 5;

console.log("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nWhat would you like the auto out to be? (You gamble 1 dollar/turn)");

stdin.addListener("data", function(autoOut)
{
	var random = Math.random();
	var coef = Math.round((0.01 + 0.99 / (1 - random)) * 100) / 100;
	var done = false;
	var start = Date.now();
	var count = 0;
	var many = "\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n";

	cash -= 1;

	while (!done)
	{
		count++;
		var now = Date.now();
		var time = (now - start) / 1000;
		var timeString = `${time}`;

		if (autoOut <= time)
		{
			done = 1;
			wins++;
			games++;
			cash += Math.round((1 * autoOut) * 100) / 100;
			cash = Math.round(cash * 100) / 100;
			console.log(`${many}----\nWIN\n----\n\n\nTIME = ${time}s\nAUTO OUT = ${autoOut}COEF = ${coef}\n\n\nWINS = ${wins}\nLOSSES = ${losses}\nTOTAL = ${games}\n\n\nCASH = \$${cash}\nPROFIT = \$${Math.round(((1 * autoOut) - 1) * 100) / 100}\n\n\n\nWhat would you like the auto out to be?`);
		}
		else if (coef <= time)
		{
			done = 1;
			losses++;
			games++;
			console.log(`${many}----\nLOSS\n----\n\n\nTIME = ${time}s\nAUTO OUT = ${autoOut}COEF = ${coef}\n\n\nWINS = ${wins}\nLOSSES = ${losses}\nTOTAL = ${games}\n\n\nCASH = \$${cash}\nLOSS = $1\n\n\n\nWhat would you like the auto out to be?`);
		}
		else
		{
			console.log(`${many}TIME = ${timeString.substring(0,4)}s`);
		}
	}
});