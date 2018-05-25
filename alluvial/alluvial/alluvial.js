const fs = require("fs");

function parseTsv(raw) {
	lines = raw.split("\n");
	return lines.slice(1, lines.length).map(line => {
		var fields = line.split("\t");
		return fields.slice(2, fields.length);
	});
}

function getBars(table) {
	bars = [];

	table.map(line => {
		line.forEach((item, index, array) => {
			if (bars[index] === undefined) {
				bars[index] = { };
			}
			if (bars[index][item] === undefined) {
				bars[index][item] = 0;
			}
			bars[index][item]++;
		});
	});

	return bars;
}

var sourceFile = process.argv[2];
fs.readFile(sourceFile, 'utf8', (err, contents) => {
	if (err) throw err;
	var table = parseTsv(contents);
	var bars = getBars(table);
	console.log(bars);
	// TODO Create list of transistions between years from table
	// TODO Draw graph as an alluvial diagram
});
