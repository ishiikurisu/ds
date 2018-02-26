var fs = require("fs");

function main() {
    var configSrc = process.argv[2];

    if (configSrc === undefined) {
        configSrc = "./config.json"
    }

    console.log("--- # Alluvial Diagrams!");
    console.log("steps:");
    console.log("- loading stuff from " + configSrc);
    var config = loadConfig(configSrc);

    console.log("...\n");
}

function loadConfig(src) {
    return JSON.parse(fs.readFileSync(src));
}

if (!module.parent) {
    main();
}
