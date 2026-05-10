const express = require('express');
const router = express.Router();
const { addActivity, getActivities, deleteActivity } = require('../controllers/activityController');
const { protect } = require('../middleware/authMiddleware');

router.use(protect);

router.post('/add', addActivity);
router.get('/:tripId', getActivities);
router.delete('/:id', deleteActivity);

module.exports = router;
