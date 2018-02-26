var fs = require("fs");

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

    Object.keys(requiredYears).forEach(year => {
        var excelname = config['years'][year]
        console.log("studying " + year + " with " + excelname);
        // TODO Load Excel spreadsheet
    });

    // TODO Store ids in a file
}

if (!module.parent) {
    main();
}
