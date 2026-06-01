✈️ Traveloop – Smart Travel Planning Platform

🌍 Overview

Traveloop is a full-stack travel planning platform built by Team Tetratech during the Odoo x Parul Hackathon.

It helps travelers manage itineraries, weather updates, activities, budgets, packing lists, and travel notes from a single dashboard, eliminating the need to switch between multiple apps.

🚀 Features

🔐 Secure Authentication 
- User Registration & Login
- JWT Authentication
- Password Encryption (bcrypt)
- Protected Routes

🗺️ Multi-City Trip Planning
- Create and manage trips
- Add multiple destinations
- Set travel dates
- Organize travelers

📅 Smart Itinerary Builder
- Build day-wise travel plans
- Add destinations and activities
- Dynamic itinerary management

🎯 Activity Discovery
- Search destinations worldwide
- Discover location-based activities
- Add activities directly to itineraries

🌤️ Weather Advisory System
- Real-time weather updates
- Rainfall and storm alerts
- UV index information
- Travel recommendations

💰 Budget & Expense Tracking
- Set trip budgets
- Record expenses
- Track spending and remaining balance
- Generate expense reports

📦 Smart Packing Checklist
- Create custom packing lists
- Categorize items
- Track packing progress

📝 Travel Notes & Journal
- Create, edit, and manage trip notes
- Store travel memories and plans

🔗 Shareable Trip Plans
- Generate shareable itineraries
- Read-only public trip views

📊 Admin Dashboard
- User analytics
- Trip statistics
- Platform monitoring

🛠️ Technology Stack
Frontend
- HTML5
- CSS3
- JavaScript
Backend
- Node.js
- Express.js
Database
- MySQL
Authentication
- JWT
- bcrypt
APIs
- Open-Meteo API
- Geocoding API
- Places & City Search APIs

👨‍💻 Team Tetratech

Team Leader : 
- Shivang Parmar

Team Members :
- Tirth Gevariya
- Srushti Donga
- Vaishvi Dholakia

⚙️ Setup & Installation : 

Prerequisites

Make sure you have the following installed:

* Node.js (v18 or later recommended)
* MySQL Server
* Git

Clone the Repository

```bash
git clone <repository-url>
cd Traveloop
```

Backend Setup

Navigate to the backend folder:

```bash
cd backend
```

Install dependencies:

```bash
npm install
```

Create a `.env` file and add:

```env
PORT=5000

DB_HOST=localhost
DB_USER=root
DB_PASSWORD=your_password
DB_NAME=traveloop

JWT_SECRET=your_jwt_secret
```

Start the backend server:

```bash
npm start
```
or

```bash
npm run dev
```

Database Setup

1. Create a MySQL database:

```sql
CREATE DATABASE traveloop;
```

2. Import the provided SQL schema (if included).

3. Verify database credentials in the `.env` file.

---

Frontend Setup

Open a new terminal:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the frontend:

```bash
npm start
```

The application will typically run at:

```text
http://localhost:3000
```

API Configuration

Ensure the frontend API URL points to the backend server:

```javascript
const API_URL = "http://localhost:5000/api";
```

Running the Project

1. Start MySQL Server.
2. Start the Backend Server.
3. Start the Frontend Application.
4. Open the application in your browser.

🚀 Future Enhancements
- AI-powered itinerary recommendations
- Hotel and transport integration
- Expense prediction
- Offline itinerary access
- Group trip collaboration
- AI travel assistant

🌍 Traveloop
- Plan Smarter. Travel Better. Explore More.
