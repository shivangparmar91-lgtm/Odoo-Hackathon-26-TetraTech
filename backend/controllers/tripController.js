const db = require('../db');

// @desc    Create a new trip
// @route   POST /api/trips/create
// @access  Private
const createTrip = async (req, res) => {
  const { trip_name, trip_type, destination, start_date, end_date, travelers, total_budget, notes } = req.body;
  const user_id = req.user.id;

  try {
    const [result] = await db.query(
      'INSERT INTO trips (user_id, trip_name, trip_type, destination, start_date, end_date, travelers, total_budget, notes) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)',
      [user_id, trip_name, trip_type, destination, start_date, end_date, travelers, total_budget, notes]
    );

    res.status(201).json({
      success: true,
      message: 'Trip created successfully',
      tripId: result.insertId
    });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Get all trips for logged in user
// @route   GET /api/trips/my-trips
// @access  Private
const getMyTrips = async (req, res) => {
  const user_id = req.user.id;

  try {
    const [rows] = await db.query('SELECT * FROM trips WHERE user_id = ? ORDER BY created_at DESC', [user_id]);
    res.json({ success: true, data: rows });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Get trip by ID
// @route   GET /api/trips/:id
// @access  Private
const getTripById = async (req, res) => {
  const trip_id = req.params.id;
  const user_id = req.user.id;

  try {
    const [rows] = await db.query('SELECT * FROM trips WHERE id = ? AND user_id = ?', [trip_id, user_id]);
    if (rows.length === 0) {
      return res.status(404).json({ success: false, message: 'Trip not found' });
    }
    res.json({ success: true, data: rows[0] });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Update a trip
// @route   PUT /api/trips/:id
// @access  Private
const updateTrip = async (req, res) => {
  const trip_id = req.params.id;
  const user_id = req.user.id;
  const { trip_name, trip_type, destination, start_date, end_date, travelers, total_budget, notes, status } = req.body;

  try {
    const [result] = await db.query(
      'UPDATE trips SET trip_name = ?, trip_type = ?, destination = ?, start_date = ?, end_date = ?, travelers = ?, total_budget = ?, notes = ?, status = ? WHERE id = ? AND user_id = ?',
      [trip_name, trip_type, destination, start_date, end_date, travelers, total_budget, notes, status, trip_id, user_id]
    );

    if (result.affectedRows === 0) {
      return res.status(404).json({ success: false, message: 'Trip not found or not authorized' });
    }

    res.json({ success: true, message: 'Trip updated successfully' });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Delete a trip
// @route   DELETE /api/trips/:id
// @access  Private
const deleteTrip = async (req, res) => {
  const trip_id = req.params.id;
  const user_id = req.user.id;

  try {
    const [result] = await db.query('DELETE FROM trips WHERE id = ? AND user_id = ?', [trip_id, user_id]);
    if (result.affectedRows === 0) {
      return res.status(404).json({ success: false, message: 'Trip not found or not authorized' });
    }
    res.json({ success: true, message: 'Trip deleted successfully' });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

module.exports = { createTrip, getMyTrips, getTripById, updateTrip, deleteTrip };
