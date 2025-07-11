# Kumbh Management System

A Python-based management system for Kumbh Mela, supporting ticket reservations, lodging, public helpline, and police helpline functionalities. Data is stored in a MySQL database.

---

## Table of Contents

- [Kumbh Management System](#kumbh-management-system)
  - [Table of Contents](#table-of-contents)
  - [Features](#features)
  - [Requirements](#requirements)
  - [Database Schema](#database-schema)
  - [MySQL Setup](#mysql-setup)
  - [Project Setup](#project-setup)
  - [How to Run](#how-to-run)
  - [Module Details](#module-details)
  - [Usage Guide](#usage-guide)
  - [Troubleshooting](#troubleshooting)

---

## Features

- Ticket reservation and viewing
- Lodging reservation with room availability
- Public helpline (Lost & Found, Medical Emergency, Information Center)
- Police helpline for incident reporting

---

## Requirements

- Python 3.10+
- MySQL Server
- `mysql-connector-python` package

---

## Database Schema

```sql
CREATE TABLE tickets (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  id_proof VARCHAR(50),
  ticket_type VARCHAR(50),
  booking_time DATETIME
);

CREATE TABLE lodging (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  location VARCHAR(100),
  price DECIMAL(10,2),
  available_rooms INT
);

CREATE TABLE lodging_reservations (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  id_proof VARCHAR(50),
  lodge_id INT,
  checkin_date DATE,
  checkout_date DATE,
  FOREIGN KEY (lodge_id) REFERENCES lodging(id)
);

CREATE TABLE police_reports (
  id INT AUTO_INCREMENT PRIMARY KEY,
  reporter_name VARCHAR(100),
  incident_type VARCHAR(100),
  description TEXT,
  report_time DATETIME
);

CREATE TABLE public_helpline_logs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(100),
  issue_type VARCHAR(100),
  description TEXT,
  logged_time DATETIME
);
```

---

## MySQL Setup

1. **Install MySQL Server**  
   Download and install MySQL from [https://dev.mysql.com/downloads/mysql/](https://dev.mysql.com/downloads/mysql/).

2. **Create Database and Tables**  
   Open MySQL shell and run:

   ```sql
   CREATE DATABASE kumbh;
   USE kumbh;
   -- Paste the schema from above here
   ```

3. **(Optional) Add Sample Lodges**

   ```sql
   INSERT INTO lodging (name, location, price, available_rooms) VALUES
   ('Ganga Lodge', 'Sector 1', 1200.00, 10),
   ('Yamuna Stay', 'Sector 2', 1500.00, 8),
   ('Triveni Guest House', 'Sector 3', 1000.00, 15);
   ```

---

## Project Setup

1. **Clone or Download the Repository**

2. **Install Python Dependencies**

   ```sh
   pip install mysql-connector-python
   ```

3. **Configure Database Connection**  
   Edit `db_config.py` if your MySQL credentials differ.

---

## How to Run

Run the main application:

```sh
python main.py
```

---

## Module Details

- `main.py`: Main menu and application loop.
- `ticket_module.py`: Ticket booking and viewing.
- `lodging_module.py`: Lodge viewing and reservation.
- `helpline_module.py`: Public helpline menu.
- `police_module.py`: Police incident reporting.
- `db_config.py`: MySQL connection setup.

---

## Usage Guide

1. **Ticket Reservation:**  
   Choose option 1 to book a ticket. Enter your name, ID proof, and ticket type.

2. **Lodging Reservation:**  
   Choose option 2 to view available lodges and reserve a room.

3. **Public Helpline:**  
   Choose option 3 for Lost & Found, Medical Emergency, or Information Center.

4. **Police Helpline:**  
   Choose option 4 to report an incident to the police.

5. **View Ticket:**  
   Choose option 5 and enter your Ticket ID to view details.

6. **Exit:**  
   Choose option 6 to exit the application.

---

## Troubleshooting

- **MySQL Connection Error:**  
  Ensure MySQL server is running and credentials in `db_config.py` are correct.

- **Module Not Found:**  
  Ensure all `.py` files are in the same directory.

- **Missing Tables:**  
  Double-check that all tables are created as per the [Database Schema](#database-schema) section.

---

**For any issues, please raise an issue or contact the maintainer.**
