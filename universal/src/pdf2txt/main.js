var fs = require('fs');
var PDFParser = require("pdf2json");

/* ##################
   # MAIN PROCEDURE #
   ################## */
var fromFile = process.argv[2];
var toFile = process.argv[3];
var pdfParser = new PDFParser(this, 1);

pdfParser.on("pdfParser_dataError", errData => console.error(errData.parserError));
pdfParser.on("pdfParser_dataReady", pdfData => {
    fs.writeFile(toFile, pdfParser.getRawTextContent(), err => {
        if (err) throw err;
    });
});
pdfParser.loadPDF(fromFile);
