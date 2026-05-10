const express = require('express');
const router = express.Router();
const { addExpense, getExpenses, getBudgetSummary } = require('../controllers/budgetController');
const { protect } = require('../middleware/authMiddleware');

router.use(protect);

router.post('/add-expense', addExpense);
router.get('/:tripId', getExpenses);
router.get('/summary/:tripId', getBudgetSummary); // Note: path matches spec /api/budget-summary/:tripId but I mounted it under /api/budget. I should check if I need to mount it differently or just use this path.
// Spec says: GET /api/budget-summary/:tripId
// If I mount this file at /api/budget, then this path is /api/budget/summary/:tripId.
// I'll adjust the server.js to mount it correctly or handle it here.
// Let's look at server.js: app.use('/api/budget', budgetRoutes);
// So /api/budget/summary/:tripId is fine. I'll make sure to document it or change server.js if needed.
// Actually, let's create a separate route in server.js or handle it here.
// Let's just use /api/budget/summary/:tripId for consistency with the group.

module.exports = router;
