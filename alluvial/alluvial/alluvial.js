const fs = require("fs");

function parseTsv(raw) {
	var lines = raw.split("\n");
	return lines.slice(1, lines.length).map(line => {
		var fields = line.split("\t");
		return fields.slice(2, fields.length);
	});
}

function getBars(table) {
	var bars = [];

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

function getTransitions(table) {
	var transitions = [];

	table.map(line => {
		var limit = line.length;
		for (var i = 0; i < limit-1; i++) {
			var from = line[i];
			var to = line[i+1];
			if (transitions[i] === undefined) {
				transitions[i] = { };
			}
			if (transitions[i][from] === undefined) {
				transitions[i][from] = { };
			}
			if (transitions[i][from][to] === undefined) {
				transitions[i][from][to] = 0;
			}
			transitions[i][from][to]++;
		}
	});

	return transitions;
}

function drawAlluvial(bars, transitions) {
	var svg = "";

	// TODO Draw graph as an alluvial diagram
	
	return svg;
}

var sourceFile = process.argv[2];
fs.readFile(sourceFile, 'utf8', (err, contents) => {
	if (err) throw err;
	// IDEA Make these things run in parallel
	var table = parseTsv(contents);
	var bars = getBars(table);
	var transitions = getTransitions(table);
	var svg = drawAlluvial(bars, transitions);
	console.log(svg);
	// TODO Save SVG contents in file
});
