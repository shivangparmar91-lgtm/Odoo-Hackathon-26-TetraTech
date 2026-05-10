const db = require('../db');

// @desc    Add a checklist item
// @route   POST /api/checklist/add
// @access  Private
const addChecklistItem = async (req, res) => {
  const { trip_id, item_name, category } = req.body;

  try {
    const [result] = await db.query(
      'INSERT INTO checklist_items (trip_id, item_name, category) VALUES (?, ?, ?)',
      [trip_id, item_name, category]
    );

    res.status(201).json({
      success: true,
      message: 'Item added successfully',
      itemId: result.insertId
    });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Get checklist for a trip
// @route   GET /api/checklist/:tripId
// @access  Private
const getChecklist = async (req, res) => {
  const trip_id = req.params.tripId;

  try {
    const [rows] = await db.query('SELECT * FROM checklist_items WHERE trip_id = ?', [trip_id]);
    res.json({ success: true, data: rows });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Toggle checklist item status
// @route   PUT /api/checklist/toggle/:id
// @access  Private
const toggleChecklistItem = async (req, res) => {
  const item_id = req.params.id;

  try {
    // Get current status
    const [rows] = await db.query('SELECT is_completed FROM checklist_items WHERE id = ?', [item_id]);
    if (rows.length === 0) {
      return res.status(404).json({ success: false, message: 'Item not found' });
    }
    const newStatus = !rows[0].is_completed;

    const [result] = await db.query('UPDATE checklist_items SET is_completed = ? WHERE id = ?', [newStatus, item_id]);
    res.json({ success: true, message: 'Item updated successfully', is_completed: newStatus });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Delete checklist item
// @route   DELETE /api/checklist/:id
// @access  Private
const deleteChecklistItem = async (req, res) => {
  const item_id = req.params.id;

  try {
    const [result] = await db.query('DELETE FROM checklist_items WHERE id = ?', [item_id]);
    if (result.affectedRows === 0) {
      return res.status(404).json({ success: false, message: 'Item not found' });
    }
    res.json({ success: true, message: 'Item deleted successfully' });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

module.exports = { addChecklistItem, getChecklist, toggleChecklistItem, deleteChecklistItem };
