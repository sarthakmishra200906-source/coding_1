const express = require('express');
const User = require('../models/User'); // 1. Make sure to import your User model!
const router = express.Router();
const { body, validationResult } = require('express-validator');

// Route 1: Create a user using: POST "/api/auth/". Doesn't require authentication
router.post('/', [
    body('name', 'Enter a valid name must be at least 3 characters').isLength({ min: 3 }),
    body('email', 'Enter a valid email').isEmail(),
    body('password', 'Enter a valid password must be at least 5 characters').isLength({ min: 5 })
], async (req, res) => {

    // 2. If there are validation errors, return Bad Request
    const errors = validationResult(req);
    if (!errors.isEmpty()) {
        return res.status(400).json({ errors: errors.array() });
    }

    try {
        // Check whether the user with this email exists already
      let user = await User.findOne({ email: req.body.email });
       if (user) {
       return res.status(400).json({ error: "Sorry a user with this email already exists" });
}
        // 3. Create a new user in the database
         user = await User.create({
            name: req.body.name,
            email: req.body.email,
            password: req.body.password,
        });

        // 4. Send back the created user (or a success message)
        res.json(user);

    } catch (error) {
        console.error(error.message);
        res.status(500).send("Internal Server Error");
    }
});

module.exports = router;