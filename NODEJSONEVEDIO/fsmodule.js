const fs = require('fs');
const path = require('path');

const textFilePath = path.join(__dirname, 'text.txt');

fs.readFile(textFilePath, 'utf-8', (err, data) => {
    if (err) {
        console.log("Error reading file:", err);
    } else {
        console.log(data);
    }
});
fs.writeFile(textFilePath, 'This is a sample text written to the file.', (err) => {
    if (err) {
        console.log("Error writing to file:", err); 
    } else {
        console.log("File written successfully.");
    }
});
