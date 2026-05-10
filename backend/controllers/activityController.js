const db = require('../db');

// @desc    Add an activity
// @route   POST /api/activity/add
// @access  Private
const addActivity = async (req, res) => {
  const { trip_id, city_name, activity_name, category, activity_date, activity_time, cost } = req.body;

  try {
    const [result] = await db.query(
      'INSERT INTO activities (trip_id, city_name, activity_name, category, activity_date, activity_time, cost) VALUES (?, ?, ?, ?, ?, ?, ?)',
      [trip_id, city_name, activity_name, category, activity_date, activity_time, cost]
    );

    res.status(201).json({
      success: true,
      message: 'Activity added successfully',
      activityId: result.insertId
    });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Get activities for a trip
// @route   GET /api/activity/:tripId
// @access  Private
const getActivities = async (req, res) => {
  const trip_id = req.params.tripId;

  try {
    const [rows] = await db.query('SELECT * FROM activities WHERE trip_id = ? ORDER BY activity_date ASC', [trip_id]);
    res.json({ success: true, data: rows });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Delete an activity
// @route   DELETE /api/activity/:id
// @access  Private
const deleteActivity = async (req, res) => {
  const activity_id = req.params.id;

  try {
    const [result] = await db.query('DELETE FROM activities WHERE id = ?', [activity_id]);
    if (result.affectedRows === 0) {
      return res.status(404).json({ success: false, message: 'Activity not found' });
    }
    res.json({ success: true, message: 'Activity deleted successfully' });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

module.exports = { addActivity, getActivities, deleteActivity };
