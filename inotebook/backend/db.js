const path = require('path');
const dotenv = require('dotenv');
const mongoose = require('mongoose');

dotenv.config({ path: path.join(__dirname, '.env') });

const connectToMongo = async () => {
    const mongoURI = process.env.mongoURI;

    if (!mongoURI) {
        throw new Error('mongoURI is missing from backend/.env');
    }

    try {
        await mongoose.connect(mongoURI);
        console.log('Connected to Mongo successfully');
    } catch (err) {
        console.error('Failed to connect to Mongo', err);
        throw err;
    }
};

module.exports = connectToMongo;