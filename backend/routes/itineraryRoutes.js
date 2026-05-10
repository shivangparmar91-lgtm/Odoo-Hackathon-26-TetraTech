const express = require('express');
const router = express.Router();
const { addStop, getItinerary, updateStop, deleteStop } = require('../controllers/itineraryController');
const { protect } = require('../middleware/authMiddleware');

router.use(protect);

router.post('/add-stop', addStop);
router.get('/:tripId', getItinerary);
router.put('/:id', updateStop);
router.delete('/:id', deleteStop);

module.exports = router;
