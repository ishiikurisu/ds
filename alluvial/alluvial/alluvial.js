const fs = require("fs");

if (!String.format) {
  String.format = function(format) {
    var args = Array.prototype.slice.call(arguments, 1);
    return format.replace(/{(\d+)}/g, function(match, number) {
      return typeof args[number] != 'undefined'
        ? args[number]
        : match
      ;
    });
  };
}

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
 * @return the bars for each step. They are a list of maps relating each group to a their size.
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
 * @return the transitions between nodes in each step. they are a list of maps relating the source group to the target group by the size of the transition.
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
	let svg = `<svg width="1300" height="800" xmlns="http://www.w3.org/2000/svg" version="1.1">`;
	let weight = 1300;
	let height = 800;
	let w = 0.95*weight;
	let h = 0.95*weight;
	let p = 10;

	// Calculating proportion factor
	max_sbij = -1;
	max_i = -1;
	for (var i = 0; i < bars.length; i++) {
		var bar = bars[i];
		var sbij = 0;
		var b = -1;

		for (var key in bar) {
			sbij += bar[key];
			b++;
		}
		sbij += p*b;

		if (max_sbij < sbij) {
			max_sbij = sbij;
			max_i = i;
		}
	}
	var sbij = 0;
	for (var key in bars[max_i]) {
		sbij += bars[max_i][key];
	}
	let fc = (h - sbij)/max_sbij;

	// Drawing bars
	var w0 = weight - w;
	var dw = w / bars.length;
	for (var i = 0; i < bars.length; i++) {
		var h0 = height - h;
		for (var key in bars[i]) {
			var dh = bars[i][key] * fc;
			svg += String.format(
				`<line x1="{0}" y1="{1}" x2="{0}" y2="{2}" stroke="#000" stroke-width="2"/>`,
				w0, h0, h0+dh
			);
			h0 += dh + p;
		}
		w0 += dw;
	}

	// TODO Draw transitions

	svg += "</svg>"
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
		// TODO Rename file
		fs.writeFile("b/output.svg", svg, (error) => {
			if (error) throw error;
		});
	}).catch(error => {
		console.log(error);
	});
});
