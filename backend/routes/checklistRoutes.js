const express = require('express');
const router = express.Router();
const { addChecklistItem, getChecklist, toggleChecklistItem, deleteChecklistItem } = require('../controllers/checklistController');
const { protect } = require('../middleware/authMiddleware');

router.use(protect);

router.post('/add', addChecklistItem);
router.get('/:tripId', getChecklist);
router.put('/toggle/:id', toggleChecklistItem);
router.delete('/:id', deleteChecklistItem);

module.exports = router;
