const express = require('express');
const cors = require('cors');
require('dotenv').config();

const app = express();
const PORT = process.env.PORT || 5000;

// Middleware
app.use(cors({
  origin: ['http://127.0.0.1:5500', 'http://localhost:5500'], // Allow Live Server origins
  credentials: true
}));
app.use(express.json());
app.use('/uploads', express.static('uploads')); // Serve profile images

// Import Routes
const authRoutes = require('./routes/authRoutes');
const tripRoutes = require('./routes/tripRoutes');
const itineraryRoutes = require('./routes/itineraryRoutes');
const activityRoutes = require('./routes/activityRoutes');
const budgetRoutes = require('./routes/budgetRoutes');
const checklistRoutes = require('./routes/checklistRoutes');
const notesRoutes = require('./routes/notesRoutes');
const profileRoutes = require('./routes/profileRoutes');
const adminRoutes = require('./routes/adminRoutes');
const shareRoutes = require('./routes/shareRoutes');

// Use Routes
app.use('/api/auth', authRoutes);
app.use('/api/trips', tripRoutes);
app.use('/api/itinerary', itineraryRoutes);
app.use('/api/activity', activityRoutes);
app.use('/api/budget', budgetRoutes);
app.use('/api/checklist', checklistRoutes);
app.use('/api/notes', notesRoutes);
app.use('/api/profile', profileRoutes);
app.use('/api/admin', adminRoutes);
app.use('/api', shareRoutes);


// Error Handling Middleware
const { errorHandler } = require('./middleware/errorMiddleware');
app.use(errorHandler);

app.get('/', (req, res) => {
  res.send('Traveloop API is running');
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
