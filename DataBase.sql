-- Crear la base de datos
CREATE DATABASE IF NOT EXISTS RealEstateDB;
USE RealEstateDB;


CREATE TABLE Properties (
    PropertyID INT AUTO_INCREMENT PRIMARY KEY,
    Address VARCHAR(100),
    Price DECIMAL(12,2)
);


CREATE TABLE Agents (
    AgentID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    Phone VARCHAR(15)
);


CREATE TABLE Clients (
    ClientID INT AUTO_INCREMENT PRIMARY KEY,
    Name VARCHAR(50),
    Email VARCHAR(50)
);


CREATE TABLE Sales (
    SaleID INT AUTO_INCREMENT PRIMARY KEY,
    PropertyID INT,
    ClientID INT,
    FOREIGN KEY (PropertyID) REFERENCES Properties(PropertyID),
    FOREIGN KEY (ClientID) REFERENCES Clients(ClientID)
);


CREATE TABLE Offices (
    OfficeID INT AUTO_INCREMENT PRIMARY KEY,
    Location VARCHAR(50),
    Phone VARCHAR(15)
);


INSERT INTO Properties (Address, Price) VALUES
('123 Maple St, Springfield', 250000.00),
('456 Oak Ave, Springfield', 320000.00),
('789 Pine Rd, Shelbyville', 180000.00);


INSERT INTO Agents (Name, Phone) VALUES
('Juan Pérez', '555-1234'),
('María López', '555-5678'),
('Carlos Gómez', '555-9012');


INSERT INTO Clients (Name, Email) VALUES
('Ana Martínez', 'ana.martinez@email.com'),
('Luis Rodríguez', 'luis.rodriguez@email.com'),
('Sofía García', 'sofia.garcia@email.com');


INSERT INTO Sales (PropertyID, ClientID) VALUES
(1, 2),
(2, 3),
(3, 1);


INSERT INTO Offices (Location, Phone) VALUES
('Downtown Springfield', '555-0001'),
('Uptown Springfield', '555-0002'),
('Shelbyville Central', '555-0003');

