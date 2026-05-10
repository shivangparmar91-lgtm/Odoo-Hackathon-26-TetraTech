const db = require('../db');

// @desc    Add an expense
// @route   POST /api/budget/add-expense
// @access  Private
const addExpense = async (req, res) => {
  const { trip_id, category, description, qty, unit_cost } = req.body;
  const amount = qty * unit_cost;

  try {
    const [result] = await db.query(
      'INSERT INTO expenses (trip_id, category, description, qty, unit_cost, amount) VALUES (?, ?, ?, ?, ?, ?)',
      [trip_id, category, description, qty, unit_cost, amount]
    );

    res.status(201).json({
      success: true,
      message: 'Expense added successfully',
      expenseId: result.insertId
    });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Get expenses for a trip
// @route   GET /api/budget/:tripId
// @access  Private
const getExpenses = async (req, res) => {
  const trip_id = req.params.tripId;

  try {
    const [rows] = await db.query('SELECT * FROM expenses WHERE trip_id = ?', [trip_id]);
    res.json({ success: true, data: rows });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

// @desc    Get budget summary
// @route   GET /api/budget/summary/:tripId
// @access  Private
const getBudgetSummary = async (req, res) => {
  const trip_id = req.params.tripId;

  try {
    // Get total budget
    const [tripRows] = await db.query('SELECT total_budget FROM trips WHERE id = ?', [trip_id]);
    if (tripRows.length === 0) {
      return res.status(404).json({ success: false, message: 'Trip not found' });
    }
    const total_budget = tripRows[0].total_budget;

    // Get total spent
    const [spentRows] = await db.query('SELECT SUM(amount) as total_spent FROM expenses WHERE trip_id = ?', [trip_id]);
    const total_spent = spentRows[0].total_spent || 0;

    // Get category wise breakdown
    const [categoryRows] = await db.query('SELECT category, SUM(amount) as amount FROM expenses WHERE trip_id = ? GROUP BY category', [trip_id]);

    res.json({
      success: true,
      data: {
        total_budget,
        total_spent,
        remaining_budget: total_budget - total_spent,
        category_wise_breakdown: categoryRows
      }
    });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

module.exports = { addExpense, getExpenses, getBudgetSummary };
