var fs = require("fs");
var excel = require("./excel");

/**
 * The main procedure of this project.
 */
function main() {
    var configSrc = process.argv[2];

    if (configSrc === undefined) {
        configSrc = "./config.json"
    }

    console.log("--- # Alluvial Diagrams!");
    console.log("steps:");
    console.log("- loading configuration from " + configSrc);
    var config = loadConfig(configSrc);

    console.log("- let's load xls?");
    getAllIndividualIds(config);

    console.log("...\n");
}

/**
 * Loads the configuration file.
 */
function loadConfig(src) {
    return JSON.parse(fs.readFileSync(src));
}

/**
 * Generates a set with all individuals ids and stores them in a list.
 */
function getAllIndividualIds(config) {
    var ids = new Set();
    var requiredYears = config['years'];
    var dir = config['working'];

    Object.keys(requiredYears).forEach(year => {
        var excelname = config['years'][year]
        console.log("studying " + year + " with " + dir + excelname);
        var currentIds = excel.getIds(excelname);
        console.log(currentIds);
    });

    // TODO Store ids in a file
}

if (!module.parent) {
    main();
}
