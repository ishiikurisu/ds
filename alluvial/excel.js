var Excel = require('exceljs');

/**
 * Loads all ids from an excel file.
 * @param excelname the path to the excel file.
 * @return an array with all identification numbers.
 */
function getIds(excelname) {
    var workbook = new Excel.Workbook();
    var ids = [];

    workbook.xlsx.readFile(excelname)
                 .then(function() {
                     // TODO Understand worksheet structure
                 });

    return ids;
}
