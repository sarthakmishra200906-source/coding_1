// Import the function that connects the application to MongoDB.
const connectToMongo = require('./db');

// Import Express to create and configure the backend server.
const express = require('express');

// Create an Express application instance.
const app = express();

// Read the port from the environment, or use port 5000 by default.
const port = Number(process.env.PORT) || 5000;

// Parse incoming JSON request bodies so route handlers can use req.body.
app.use(express.json());

// Register authentication routes under /api/auth.
app.use('/api/auth', require('./routes/auth'));

// Register notes routes under /api/notes.
app.use('/api/notes', require('./routes/notes'));

// Connect to MongoDB before accepting requests.
const startServer = async () => {
    await connectToMongo();

    // Start the HTTP server and display the address in the terminal.
    app.listen(port, () => {
        console.log(`Server listening at http://localhost:${port}`);
    });
};

// Start the application and set a failure exit code if startup fails.
startServer().catch(() => {
    process.exitCode = 1;
});