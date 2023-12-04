-- 用户表
CREATE TABLE Users (
    UserID INT PRIMARY KEY AUTO_INCREMENT,
    UserName VARCHAR(255),
    RealName VARCHAR(255),
    Gender VARCHAR(10),
    IDCard VARCHAR(20),
    Email VARCHAR(255),
    Address VARCHAR(255),
    Account VARCHAR(255),
    Password VARCHAR(255)
);

-- 管理员表
CREATE TABLE Administrators (
    AdminID INT PRIMARY KEY AUTO_INCREMENT,
    AdminType VARCHAR(20), -- 剧院管理员或系统管理员
    Account VARCHAR(255),
    Password VARCHAR(255),
    Permissions VARCHAR(255)
);

-- 功能表
CREATE TABLE AdminFunctions (
    FunctionID INT PRIMARY KEY AUTO_INCREMENT,
    Name VARCHAR(255),
    Permissions VARCHAR(255)
);

-- 演出表
CREATE TABLE Shows (
    ShowID INT PRIMARY KEY AUTO_INCREMENT,
    TheaterID INT, -- 外键，关联剧院
    ShowName VARCHAR(255),
    Description TEXT,
    ShowDate DATE,
    Duration INT,
    AdminID INT, -- 外键，关联管理员
    Image VARCHAR(255),
    Category VARCHAR(255),
    City VARCHAR(255)
);

-- 剧院表
CREATE TABLE Theaters (
    TheaterID INT PRIMARY KEY AUTO_INCREMENT,
    TheaterName VARCHAR(255),
    Address VARCHAR(255),
    Capacity INT,
    AdminID INT -- 外键，关联管理员
);

-- 票价管理表
CREATE TABLE TicketPrices (
    TicketID INT PRIMARY KEY AUTO_INCREMENT,
    ShowID INT, -- 外键，关联演出
    Price DECIMAL(10, 2),
    Category VARCHAR(255),
    TotalQuantity INT,
    RemainingQuantity INT
);

-- 订单表
CREATE TABLE Orders (
    OrderID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT, -- 外键，关联用户
    TicketID INT, -- 外键，关联票价管理
    PurchaseTime TIMESTAMP,
    OrderStatus VARCHAR(20),
    Quantity INT
);

-- 退票表
CREATE TABLE Refunds (
    RefundID INT PRIMARY KEY AUTO_INCREMENT,
    UserID INT, -- 外键，关联用户
    AdminID INT, -- 外键，关联管理员
    RefundTime TIMESTAMP,
    RefundReason TEXT,
    TicketStatus VARCHAR(20),
    OrderID INT -- 外键，关联订单
);
