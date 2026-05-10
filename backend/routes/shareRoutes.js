const express = require('express');
const router = express.Router();
const { shareTrip, getPublicTrip } = require('../controllers/shareController');
const { protect } = require('../middleware/authMiddleware');

router.post('/share/:tripId', protect, shareTrip);
router.get('/public/:token', getPublicTrip);

module.exports = router;
