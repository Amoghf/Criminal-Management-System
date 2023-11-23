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
DELIMITER //
CREATE TRIGGER check_age
BEFORE  INSERT ON criminal
FOR EACH ROW
BEGIN
    IF NEW.age IS NOT NULL AND (NEW.age <= 0 OR NEW.age < 18 OR NEW.age > 120) THEN
        INSERT INTO age_error_messages (error_code) VALUES (1); -- Indication for "Age must be a positive integer"
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Age must be a positive integer';
    ELSEIF NEW.age IS NOT NULL AND (NEW.age < 18 OR NEW.age > 120) THEN
        INSERT INTO age_error_messages (error_code) VALUES (2); -- Indication for "Age must be between 18 and 120"
        SIGNAL SQLSTATE '45000' SET MESSAGE_TEXT = 'Age must be between 18 and 120';
    END IF;
END;
//
DELIMITER ;
DROP TRIGGER check_age;

select * from criminal_management.age_error_messages;

DELIMITER //

CREATE PROCEDURE InsertCriminal(
    IN p_Criminal_no INT,
    IN p_Criminal_name VARCHAR(255),
    IN p_Nick_name VARCHAR(255),
    IN p_arrest_date VARCHAR(50),
    IN p_dateOfcrime VARCHAR(50),
    IN p_address VARCHAR(255),
    IN p_age INT,
    IN p_occupation VARCHAR(255),
    IN p_BirthMark VARCHAR(255),
    IN p_crimetype VARCHAR(255),
    IN p_fatherName VARCHAR(255),
    IN p_gender VARCHAR(10),
    IN p_wanted VARCHAR(5)
)
BEGIN
    INSERT INTO criminal (
        Criminal_no,
        Criminal_name,
        Nick_name,
        arrest_date,
        dateOfcrime,
        address,
        age,
        occupation,
        BirthMark,
        crimetype,
        fatherName,
        gender,
        wanted
    ) VALUES (
        p_Criminal_no,
        p_Criminal_name,
        p_Nick_name,
        p_arrest_date,
        p_dateOfcrime,
        p_address,
        p_age,
        p_occupation,
        p_BirthMark,
        p_crimetype,
        p_fatherName,
        p_gender,
        p_wanted
    );
END //

DELIMITER ;
DELIMITER //

CREATE PROCEDURE UpdateCriminal(
    IN p_Case_id INT,
    IN p_NewAddress VARCHAR(255),
    IN p_NewOccupation VARCHAR(255)
)
BEGIN
    UPDATE criminal
    SET address = p_NewAddress, occupation = p_NewOccupation
    WHERE Case_id = p_Case_id;
END //

DELIMITER ;
-- Call the UpdateCriminal stored procedure with specific parameters
CALL UpdateCriminal(2, 'jahanvi ', 'cab ');
DELIMITER //

CREATE PROCEDURE ShowUpdatedCriminalInfo(IN p_Case_id INT)
BEGIN
    -- Display the original information
    SELECT * FROM criminal WHERE Case_id = p_Case_id;

    -- Call the UpdateCriminal stored procedure
    CALL UpdateCriminal(p_Case_id, 'jahanvi', 'cab');

    -- Display the updated information
    SELECT * FROM criminal WHERE Case_id = p_Case_id;
END //

DELIMITER ;
-- Call the ShowUpdatedCriminalInfo procedure with specific parameters
CALL ShowUpdatedCriminalInfo(2);


DELIMITER //

CREATE FUNCTION GetCriminalCount() RETURNS INT
BEGIN
    DECLARE criminal_count INT;
    SELECT COUNT(*) INTO criminal_count FROM criminal;
    RETURN criminal_count;
END //

DELIMITER ;

DELIMITER //

CREATE FUNCTION GetCriminalCount() RETURNS INT
DETERMINISTIC
BEGIN
    DECLARE criminal_count INT;
    SELECT COUNT(*) INTO criminal_count FROM criminal;
    RETURN criminal_count;
END //

DELIMITER ;

-- Call the GetCriminalCount function in a SELECT statement
SELECT GetCriminalCount() as CriminalCount;
