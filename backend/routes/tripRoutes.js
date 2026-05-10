const express = require('express');
const router = express.Router();
const { createTrip, getMyTrips, getTripById, updateTrip, deleteTrip } = require('../controllers/tripController');
const { protect } = require('../middleware/authMiddleware');

router.use(protect); // Protect all trip routes

router.get('/', getMyTrips);
router.post('/create', createTrip);
router.get('/my-trips', getMyTrips);
router.get('/:id', getTripById);
router.put('/:id', updateTrip);
router.delete('/:id', deleteTrip);

module.exports = router;
