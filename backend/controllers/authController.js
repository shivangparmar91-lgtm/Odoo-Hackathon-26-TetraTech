const bcrypt = require('bcrypt');
const jwt = require('jsonwebtoken');
const db = require('../db');

// @desc    Register a new user
// @route   POST /api/auth/register
// @access  Public
const register = async (req, res) => {
  const { full_name, name, email, password } = req.body;
  const actual_full_name = full_name || name;

  try {
    // Check if user exists
    const [rows] = await db.query('SELECT * FROM users WHERE email = ?', [email]);
    if (rows.length > 0) {
      return res.status(400).json({ success: false, message: 'User already exists' });
    }

    // Hash password
    const salt = await bcrypt.genSalt(10);
    const hashedPassword = await bcrypt.hash(password, salt);

    // Insert user
    const [result] = await db.query(
      'INSERT INTO users (full_name, email, password) VALUES (?, ?, ?)',
      [actual_full_name, email, hashedPassword]
    );


    res.status(201).json({
      success: true,
      message: 'User registered successfully',
      userId: result.insertId
    });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Login user
// @route   POST /api/auth/login
// @access  Public
const login = async (req, res) => {
  const { email, password } = req.body;

  try {
    const [rows] = await db.query('SELECT * FROM users WHERE email = ?', [email]);
    if (rows.length === 0) {
      return res.status(400).json({ success: false, message: 'Invalid credentials' });
    }

    const user = rows[0];

    // Check password
    const isMatch = await bcrypt.compare(password, user.password);
    if (!isMatch) {
      return res.status(400).json({ success: false, message: 'Invalid credentials' });
    }

    // Generate JWT
    const token = jwt.sign({ id: user.id, email: user.email }, process.env.JWT_SECRET, {
      expiresIn: '30d'
    });

    res.json({
      success: true,
      token,
      user: {
        id: user.id,
        full_name: user.full_name,
        email: user.email
      }
    });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Get current user
// @route   GET /api/auth/me
// @access  Private
const getMe = async (req, res) => {
  try {
    const [rows] = await db.query('SELECT id, full_name, email, location, profile_image FROM users WHERE id = ?', [req.user.id]);
    if (rows.length === 0) {
      return res.status(404).json({ success: false, message: 'User not found' });
    }
    res.json({ success: true, user: rows[0] });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

module.exports = { register, login, getMe };
