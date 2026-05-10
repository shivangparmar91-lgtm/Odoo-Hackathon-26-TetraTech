CREATE DATABASE IF NOT EXISTS traveloop_db;
USE traveloop_db;

-- 1. Users Table
CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  full_name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  location VARCHAR(255),
  profile_image VARCHAR(255),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- 2. Trips Table
CREATE TABLE IF NOT EXISTS trips (
  id INT AUTO_INCREMENT PRIMARY KEY,
  user_id INT,
  trip_name VARCHAR(255) NOT NULL,
  trip_type ENUM('india', 'intl') DEFAULT 'india',
  destination VARCHAR(255) NOT NULL,
  start_date DATE,
  end_date DATE,
  travelers INT DEFAULT 1,
  total_budget DECIMAL(10, 2),
  notes TEXT,
  status ENUM('upcoming', 'ongoing', 'completed') DEFAULT 'upcoming',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

-- 3. Trip Stops Table
CREATE TABLE IF NOT EXISTS trip_stops (
  id INT AUTO_INCREMENT PRIMARY KEY,
  trip_id INT,
  city_name VARCHAR(255) NOT NULL,
  arrival_date DATE,
  departure_date DATE,
  order_no INT,
  FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE
);

-- 4. Activities Table
CREATE TABLE IF NOT EXISTS activities (
  id INT AUTO_INCREMENT PRIMARY KEY,
  trip_id INT,
  city_name VARCHAR(255),
  activity_name VARCHAR(255) NOT NULL,
  category VARCHAR(100),
  activity_date DATE,
  activity_time TIME,
  cost DECIMAL(10, 2),
  FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE
);

-- 5. Expenses Table
CREATE TABLE IF NOT EXISTS expenses (
  id INT AUTO_INCREMENT PRIMARY KEY,
  trip_id INT,
  category VARCHAR(100),
  description VARCHAR(255),
  qty INT DEFAULT 1,
  unit_cost DECIMAL(10, 2),
  amount DECIMAL(10, 2),
  FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE
);

-- 6. Checklist Items Table
CREATE TABLE IF NOT EXISTS checklist_items (
  id INT AUTO_INCREMENT PRIMARY KEY,
  trip_id INT,
  item_name VARCHAR(255) NOT NULL,
  category VARCHAR(100),
  is_completed BOOLEAN DEFAULT FALSE,
  FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE
);

-- 7. Notes Table
CREATE TABLE IF NOT EXISTS notes (
  id INT AUTO_INCREMENT PRIMARY KEY,
  trip_id INT,
  title VARCHAR(255) NOT NULL,
  content TEXT,
  note_day VARCHAR(50),
  city_name VARCHAR(100),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE
);

-- 8. Shared Links Table
CREATE TABLE IF NOT EXISTS shared_links (
  id INT AUTO_INCREMENT PRIMARY KEY,
  trip_id INT,
  public_token VARCHAR(255) NOT NULL UNIQUE,
  FOREIGN KEY (trip_id) REFERENCES trips(id) ON DELETE CASCADE
);

-- End of schema

