const db = require('../db');

// @desc    Get admin stats
// @route   GET /api/admin/stats
// @access  Private (Admin)
const getStats = async (req, res) => {
  try {
    const [userCountRows] = await db.query('SELECT COUNT(*) as total_users FROM users');
    const [tripCountRows] = await db.query('SELECT COUNT(*) as total_trips FROM trips');
    
    const [popularCitiesRows] = await db.query(
      'SELECT city_name, COUNT(*) as count FROM trip_stops GROUP BY city_name ORDER BY count DESC LIMIT 5'
    );
    
    const [popularActivitiesRows] = await db.query(
      'SELECT activity_name, COUNT(*) as count FROM activities GROUP BY activity_name ORDER BY count DESC LIMIT 5'
    );

    res.json({
      success: true,
      data: {
        total_users: userCountRows[0].total_users,
        total_trips: tripCountRows[0].total_trips,
        popular_cities: popularCitiesRows,
        popular_activities: popularActivitiesRows,
        monthly_growth: '15%' // Mock data for simplicity in hackathon
      }
    });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

const getUsers = async (req, res) => {
  try {
    const [rows] = await db.query(`
      SELECT u.id, u.full_name, u.email, COUNT(t.id) as trips_count 
      FROM users u 
      LEFT JOIN trips t ON u.id = t.user_id 
      GROUP BY u.id
    `);
    
    res.json({
      success: true,
      data: rows
    });
  } catch (error) {
    res.status(500).json({ success: false, message: error.message });
  }
};

module.exports = { getStats, getUsers };
