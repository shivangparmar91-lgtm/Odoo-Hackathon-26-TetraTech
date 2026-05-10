const db = require('../db');

// @desc    Get user profile
// @route   GET /api/profile
// @access  Private
const getProfile = async (req, res) => {
  const user_id = req.user.id;

  try {
    const [rows] = await db.query('SELECT id, full_name, email, location, profile_image FROM users WHERE id = ?', [user_id]);
    if (rows.length === 0) {
      return res.status(404).json({ success: false, message: 'User not found' });
    }
    res.json({ success: true, data: rows[0] });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Update user profile
// @route   PUT /api/profile/update
// @access  Private
const updateProfile = async (req, res) => {
  const user_id = req.user.id;
  const { full_name, location } = req.body;

  try {
    const [result] = await db.query(
      'UPDATE users SET full_name = ?, location = ? WHERE id = ?',
      [full_name, location, user_id]
    );

    res.json({ success: true, message: 'Profile updated successfully' });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

module.exports = { getProfile, updateProfile };
