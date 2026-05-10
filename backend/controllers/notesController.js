const db = require('../db');

// @desc    Add a note
// @route   POST /api/notes/add
// @access  Private
const addNote = async (req, res) => {
  const { trip_id, title, content, note_day, city_name } = req.body;

  try {
    const [result] = await db.query(
      'INSERT INTO notes (trip_id, title, content, note_day, city_name) VALUES (?, ?, ?, ?, ?)',
      [trip_id, title, content, note_day, city_name]
    );

    res.status(201).json({
      success: true,
      message: 'Note saved successfully',
      noteId: result.insertId
    });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Get notes for a trip
// @route   GET /api/notes/:tripId
// @access  Private
const getNotes = async (req, res) => {
  const trip_id = req.params.tripId;

  try {
    const [rows] = await db.query('SELECT * FROM notes WHERE trip_id = ? ORDER BY created_at DESC', [trip_id]);
    res.json({ success: true, data: rows });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Delete a note
// @route   DELETE /api/notes/:id
// @access  Private
const deleteNote = async (req, res) => {
  const note_id = req.params.id;

  try {
    const [result] = await db.query('DELETE FROM notes WHERE id = ?', [note_id]);
    if (result.affectedRows === 0) {
      return res.status(404).json({ success: false, message: 'Note not found' });
    }
    res.json({ success: true, message: 'Note deleted successfully' });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

module.exports = { addNote, getNotes, deleteNote };
