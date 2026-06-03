-- Clean up existing states if re-executed
DROP TABLE IF EXISTS Payments CASCADE;
DROP TABLE IF EXISTS Members CASCADE;
DROP TABLE IF EXISTS Plans CASCADE;
DROP TABLE IF EXISTS Trainers CASCADE;

-- 1. Trainers Table
CREATE TABLE Trainers (
    TrainerID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Specialization VARCHAR(50)
);

-- 2. Membership Plans Table
CREATE TABLE Plans (
    PlanID SERIAL PRIMARY KEY,
    PlanName VARCHAR(50) NOT NULL,
    DurationMonths INT NOT NULL,
    Price DECIMAL(10, 2) NOT NULL
);

-- 3. Members Table
CREATE TABLE Members (
    MemberID SERIAL PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Phone VARCHAR(15) UNIQUE,
    TrainerID INT REFERENCES Trainers(TrainerID) ON DELETE SET NULL,
    PlanID INT REFERENCES Plans(PlanID) ON DELETE RESTRICT
);

-- 4. Payments Table
CREATE TABLE Payments (
    PaymentID SERIAL PRIMARY KEY,
    MemberID INT REFERENCES Members(MemberID) ON DELETE CASCADE,
    Amount DECIMAL(10, 2) NOT NULL,
    PaymentDate DATE DEFAULT CURRENT_DATE,
    Status VARCHAR(20) DEFAULT 'Pending' CHECK (Status IN ('Paid', 'Pending'))
);

-- Seed values directly from the unstructured project report specifications
INSERT INTO Trainers (Name, Specialization) VALUES
('Mike Tyson', 'Cardio & Boxing'),
('Serena Williams', 'Strength Training'),
('David Laid', 'Bodybuilding & Hypertrophy'),
('Chris Bumstead', 'Classic Physique Training'),
('Rhonda Patrick', 'Nutrition & High-Intensity Cardio');

INSERT INTO Plans (PlanName, DurationMonths, Price) VALUES
('Monthly Basic', 1, 1500.00),
('Annual Pro', 12, 12000.00),
('Quarterly Premium', 3, 4000.00),
('Bi-Annual Elite', 6, 7500.00),
('Weekend Warrior', 1, 1000.00);

INSERT INTO Members (Name, Phone, TrainerID, PlanID) VALUES
('Rahul Sharma', '9876543210', 1, 1),
('Ananya Rao', '9123456789', 2, 2),
('Vikram Sinha', '9887766554', 3, 3),
('Rohan Hegde', '8776655443', 4, 4),
('Sneha Murthy', '7665544332', NULL, 1),
('Kabir Mehta', '6554433221', 4, 5),
('Meera Nair', '9911223344', 5, 4);

INSERT INTO Payments (MemberID, Amount, PaymentDate, Status) VALUES
(1, 1500.00, CURRENT_DATE, 'Paid'),
(2, 12000.00, CURRENT_DATE, 'Pending'),
(3, 4000.00, '2026-05-10', 'Paid'),
(4, 7500.00, '2026-05-12', 'Paid'),
(5, 1500.00, '2026-05-15', 'Pending'), 
(6, 12000.00, '2026-05-18', 'Paid'),
(7, 7500.00, '2026-05-20', 'Pending');