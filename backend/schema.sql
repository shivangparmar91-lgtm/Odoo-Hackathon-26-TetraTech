CREATE DATABASE IF NOT EXISTS travelloop;
USE travelloop;

CREATE TABLE IF NOT EXISTS users (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  email VARCHAR(255) NOT NULL UNIQUE,
  password VARCHAR(255) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS trips (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(255) NOT NULL,
  destination VARCHAR(255) NOT NULL,
  start_date DATE,
  end_date DATE,
  budget DECIMAL(10, 2),
  trip_type ENUM('india', 'intl') DEFAULT 'india',
  user_id INT,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id)
);

-- Insert some dummy data for testing
INSERT INTO trips (name, destination, start_date, end_date, budget, trip_type) VALUES
('Rajasthan Heritage Trail', 'Jaipur', '2025-06-01', '2025-06-10', 42000.00, 'india'),
('Goa Escape', 'Goa', '2026-05-01', '2026-05-05', 18400.00, 'india'),
('Paris & Rome Adventure', 'Paris', '2025-06-01', '2025-06-15', 22000.00, 'intl');
