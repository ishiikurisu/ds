var fs = require('fs');
var PDFParser = require("pdf2json");

/* ##################
   # TEST PROCEDURE #
   ################## */
var fromFile = process.argv[2];
var pdfParser = new PDFParser(this, 1);

console.log("Testing "  + fromFile);
pdfParser.on("pdfParser_dataError", errData => console.error(errData.parserError));
pdfParser.on("pdfParser_dataReady", pdfData => {
    fs.writeFile("./output.log", pdfParser.getRawTextContent());
});
pdfParser.loadPDF(fromFile);
