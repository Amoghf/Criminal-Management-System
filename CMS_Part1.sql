-- Create the "criminal_management" database
CREATE DATABASE IF NOT EXISTS criminal_management;

-- Use the "criminal_management" database
USE criminal_management;

-- Create the "criminal" table
CREATE TABLE criminal (
    Case_id INT AUTO_INCREMENT PRIMARY KEY,
    Criminal_no INT,
    Criminal_name VARCHAR(255),
    Nick_name VARCHAR(255),
    arrest_date VARCHAR(50),
    dateOfcrime VARCHAR(50),
    address VARCHAR(255),
    age INT,
    occupation VARCHAR(255),
    BirthMark VARCHAR(255),
    crimetype VARCHAR(255),
    fatherName VARCHAR(255),
    gender VARCHAR(10),
    wanted VARCHAR(5)
);

-- Create the "login" table
CREATE TABLE login (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(255),
    password VARCHAR(255)
);

-- Create the "crime" table with a foreign key reference to the "criminal" table
CREATE TABLE crime (
    crime_id INT AUTO_INCREMENT PRIMARY KEY,
    criminal_id INT,
    crime_type VARCHAR(255),
    crime_date DATE,
    FOREIGN KEY (criminal_id) REFERENCES criminal(Case_id)
);

-- Create the "criminal_family" table with a foreign key reference to the "criminal" table
CREATE TABLE criminal_family (
    family_id INT AUTO_INCREMENT PRIMARY KEY,
    criminal_id INT,
    family_member_name VARCHAR(255),
    relationship VARCHAR(255),
    FOREIGN KEY (criminal_id) REFERENCES criminal(Case_id)
);

-- Create the "lawyer" table with a foreign key reference to the "criminal" table
CREATE TABLE lawyer (
    lawyer_id INT AUTO_INCREMENT PRIMARY KEY,
    criminal_id INT,
    lawyer_name VARCHAR(255),
    specialization VARCHAR(255),
    FOREIGN KEY (criminal_id) REFERENCES criminal(Case_id)
);

-- Create the "admin" table with its own attributes
CREATE TABLE admin (
    admin_id INT AUTO_INCREMENT PRIMARY KEY,
    admin_name VARCHAR(255),
    admin_email VARCHAR(255)
);

-- Create the "evidence" table with a foreign key reference to the "criminal" table
CREATE TABLE evidence (
    evidence_id INT AUTO_INCREMENT PRIMARY KEY,
    criminal_id INT,
    evidence_description VARCHAR(255),
    evidence_date DATE,
    FOREIGN KEY (criminal_id) REFERENCES criminal(Case_id)
);
show tables;
select * from criminal_management.criminal;
CREATE TABLE age_error_messages (
    error_code INT PRIMARY KEY,
    error_message TEXT
);
INSERT INTO age_error_messages (error_code, error_message)
VALUES
    (1, 'Age must be a positive integer'),
    (2, 'Age must be between 18 and 120');