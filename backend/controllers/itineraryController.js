const db = require('../db');

// @desc    Add a stop to itinerary
// @route   POST /api/itinerary/add-stop
// @access  Private
const addStop = async (req, res) => {
  const { trip_id, city_name, arrival_date, departure_date, order_no } = req.body;

  try {
    const [result] = await db.query(
      'INSERT INTO trip_stops (trip_id, city_name, arrival_date, departure_date, order_no) VALUES (?, ?, ?, ?, ?)',
      [trip_id, city_name, arrival_date, departure_date, order_no]
    );

    res.status(201).json({
      success: true,
      message: 'Stop added successfully',
      stopId: result.insertId
    });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Get itinerary for a trip
// @route   GET /api/itinerary/:tripId
// @access  Private
const getItinerary = async (req, res) => {
  const trip_id = req.params.tripId;

  try {
    const [rows] = await db.query('SELECT * FROM trip_stops WHERE trip_id = ? ORDER BY order_no ASC', [trip_id]);
    res.json({ success: true, data: rows });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Update a stop
// @route   PUT /api/itinerary/:id
// @access  Private
const updateStop = async (req, res) => {
  const stop_id = req.params.id;
  const { city_name, arrival_date, departure_date, order_no } = req.body;

  try {
    const [result] = await db.query(
      'UPDATE trip_stops SET city_name = ?, arrival_date = ?, departure_date = ?, order_no = ? WHERE id = ?',
      [city_name, arrival_date, departure_date, order_no, stop_id]
    );

    if (result.affectedRows === 0) {
      return res.status(404).json({ success: false, message: 'Stop not found' });
    }

    res.json({ success: true, message: 'Stop updated successfully' });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Delete a stop
// @route   DELETE /api/itinerary/:id
// @access  Private
const deleteStop = async (req, res) => {
  const stop_id = req.params.id;

  try {
    const [result] = await db.query('DELETE FROM trip_stops WHERE id = ?', [stop_id]);
    if (result.affectedRows === 0) {
      return res.status(404).json({ success: false, message: 'Stop not found' });
    }
    res.json({ success: true, message: 'Stop deleted successfully' });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

module.exports = { addStop, getItinerary, updateStop, deleteStop };
