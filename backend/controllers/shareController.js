const db = require('../db');
const crypto = require('crypto');

// @desc    Generate public share link for a trip
// @route   POST /api/share/:tripId
// @access  Private
const shareTrip = async (req, res) => {
  const trip_id = req.params.tripId;

  try {
    // Check if link already exists
    const [existing] = await db.query('SELECT public_token FROM shared_links WHERE trip_id = ?', [trip_id]);
    if (existing.length > 0) {
      return res.json({ success: true, token: existing[0].public_token });
    }

    // Generate token
    const token = crypto.randomBytes(16).toString('hex');

    await db.query('INSERT INTO shared_links (trip_id, public_token) VALUES (?, ?)', [trip_id, token]);

    res.json({ success: true, token });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Get public trip data by token
// @route   GET /api/public/:token
// @access  Public
const getPublicTrip = async (req, res) => {
  const token = req.params.token;

  try {
    // Find trip ID by token
    const [linkRows] = await db.query('SELECT trip_id FROM shared_links WHERE public_token = ?', [token]);
    if (linkRows.length === 0) {
      return res.status(404).json({ success: false, message: 'Invalid or expired link' });
    }
    const trip_id = linkRows[0].trip_id;

    // Get trip data
    const [tripRows] = await db.query('SELECT * FROM trips WHERE id = ?', [trip_id]);
    const [itineraryRows] = await db.query('SELECT * FROM trip_stops WHERE trip_id = ? ORDER BY order_no ASC', [trip_id]);
    const [activityRows] = await db.query('SELECT * FROM activities WHERE trip_id = ?', [trip_id]);

    res.json({
      success: true,
      data: {
        trip: tripRows[0],
        itinerary: itineraryRows,
        activities: activityRows
      }
    });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

module.exports = { shareTrip, getPublicTrip };
