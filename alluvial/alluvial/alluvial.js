const fs = require("fs");

function parseTsv(raw) {
	lines = raw.split("\n");
	return lines.slice(1, lines.length).map(line => {
		var fields = line.split("\t");
		return fields.slice(2, fields.length);
	});
}

var sourceFile = process.argv[2];
fs.readFile(sourceFile, 'utf8', (err, contents) => {
	if (err) throw err;
	var table = parseTsv(contents);
	// TODO Create list of bars in each year from table
	// TODO Create list of transistions between years from table
	// TODO Draw graph as an alluvial diagram
});
