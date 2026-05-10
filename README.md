# Traveloop - Full Stack Backend

This is the backend for the Traveloop project, built with Node.js, Express.js, and MySQL.

## Tech Stack
- **Backend**: Node.js + Express.js
- **Database**: MySQL
- **Authentication**: JWT + bcrypt
- **Utilities**: cors, dotenv, multer

## Folder Structure
```text
traveloop/
│── frontend/                     (already exists)
│── backend/
│   │── server.js
│   │── package.json
│   │── .env
│   │── db.js
│   ├── routes/
│   ├── controllers/
│   └── middleware/
└── database/
    └── traveloop.sql
```

## Setup Guide

### STEP 1: Install Node.js
Make sure you have Node.js installed on your system.

### STEP 2: Install MySQL / XAMPP
Ensure you have MySQL running. You can use XAMPP or a standalone MySQL installation.

### STEP 3: Import Database
1. Open your MySQL client.
2. Run the queries in `database/traveloop.sql` to create the `traveloop_db` database and tables.

### STEP 4: Install Dependencies
Navigate to the `backend` folder and run:
```bash
cd backend
npm install
```

### STEP 5: Configure Environment
Open `backend/.env` and update your database credentials:
```env
DB_USER=your_username
DB_PASSWORD=your_password
```

### STEP 6: Run Backend
```bash
npm run dev
```
The server will start on `http://localhost:5000`.

### STEP 7: Run Frontend
Open `frontend/index.html` with Live Server in VS Code.

---

## API List

### Auth
- `POST /api/auth/register` - Register user
- `POST /api/auth/login` - Login user
- `GET /api/auth/me` - Get current user (Protected)

### Trips
- `POST /api/trips/create` - Create trip (Protected)
- `GET /api/api/trips/my-trips` - Get my trips (Protected)
- `GET /api/trips/:id` - Get trip by ID (Protected)
- `PUT /api/trips/:id` - Update trip (Protected)
- `DELETE /api/trips/:id` - Delete trip (Protected)

### Itinerary
- `POST /api/itinerary/add-stop` - Add stop (Protected)
- `GET /api/itinerary/:tripId` - Get itinerary (Protected)

### Budget
- `POST /api/budget/add-expense` - Add expense (Protected)
- `GET /api/budget/summary/:tripId` - Get budget summary (Protected)

---

## Frontend Integration Examples

### Login Example
```javascript
const response = await fetch('http://localhost:5000/api/auth/login', {
  method: 'POST',
  headers: { 'Content-Type': 'application/json' },
  body: JSON.stringify({ email: 'test@example.com', password: 'password' })
});
const data = await response.json();
if (data.success) {
  localStorage.setItem('token', data.token);
  window.location.href = 'pages/dashboard.html';
}
```

### Load Trips Example
```javascript
const token = localStorage.getItem('token');
const response = await fetch('http://localhost:5000/api/trips/my-trips', {
  headers: { 'Authorization': `Bearer ${token}` }
});
const data = await response.json();
console.log(data.data);
```