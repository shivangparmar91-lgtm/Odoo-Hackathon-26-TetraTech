const express = require('express');
const router = express.Router();
const { addNote, getNotes, deleteNote } = require('../controllers/notesController');
const { protect } = require('../middleware/authMiddleware');

router.use(protect);

router.post('/add', addNote);
router.get('/:tripId', getNotes);
router.delete('/:id', deleteNote);

module.exports = router;
