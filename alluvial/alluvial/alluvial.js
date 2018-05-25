const fs = require("fs");

/**
 * Loads contents from a TSV string.
 * @param raw The raw contents from the file
 * @return the table in the string
 */
function parseTsv(raw) {
	let lines = raw.split("\n");
	return lines.slice(1, lines.length).map(line => {
		let fields = line.split("\t");
		return fields.slice(2, fields.length);
	});
}

/**
 * Extracts the bars in the alluvial table.
 * @param table the alluvial table
 * @return the bars for each step
 */
function getBars(table) {
	let bars = [];

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

/**
 * Extracts the transitions between bars in an alluvial table.
 * @param table the alluvial table
 * @return the transitions between nodes in each step
 */
function getTransitions(table) {
	let transitions = [];

	table.map(line => {
		let limit = line.length;
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

/**
 * Generates a SVG description on the graph in bars and transitions
 * as an alluvial diagram.
 * @param bars the bars in the plot
 * @param transitions the transitions between different bars
 * @return the SVG description of an alluvial diagram in these conditions
 */
function drawAlluvial(bars, transitions) {
	let svg = "";

	// TODO Draw graph as an alluvial diagram

	return svg;
}

var sourceFile = process.argv[2];
fs.readFile(sourceFile, 'utf8', (err, contents) => {
	if (err) throw err;
	let table = parseTsv(contents);
	let barsPromise = new Promise((resolve, reject) => {
		let bars = getBars(table);
		if (bars === null) {
			reject(bars);
		} else {
			resolve(bars);
		}
	});
	let transitionsPromise = new Promise((resolve, reject) => {
		let transitions = getTransitions(table);
		if (transitions === null) {
			reject(transitions);
		} else {
			resolve(transitions);
		}
	});

	Promise.all([
		barsPromise,
		transitionsPromise
	]).then(stuff => {
		var svg = drawAlluvial(stuff[0], stuff[1]);
		console.log(svg);
		// TODO Save SVG contents in file
	}).catch(error => {
		console.log(error);
	});
});
