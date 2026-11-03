const connectToMongo = require('./db');
const express = require('express');

const app = express();
const port = Number(process.env.PORT) || 3000;

app.get('/', (req, res) => {
    res.send('Hello World!');
});

const startServer = async () => {
    await connectToMongo();
    app.listen(port, () => {
        console.log(`Server listening at http://localhost:${port}`);
    });
};

startServer().catch(() => {
    process.exitCode = 1;
});