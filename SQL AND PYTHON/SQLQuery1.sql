DROP TABLE IF EXISTS bills;
DROP TABLE IF EXISTS users;
CREATE TABLE users (
    user_id INT PRIMARY KEY IDENTITY(1,1),
    name NVARCHAR(100),
    address NVARCHAR(255)
);

CREATE TABLE bills (
    bill_id INT PRIMARY KEY IDENTITY(1,1),
    user_id INT,
    month VARCHAR(20),
    usage_kwh FLOAT,
    bill_amount FLOAT,
    FOREIGN KEY (user_id) REFERENCES users(user_id)
);

INSERT INTO users (name, address)
VALUES ('Ravi Kumar', 'Bangalore');

INSERT INTO bills (user_id, month, usage_kwh, bill_amount)
VALUES
(1, '2021-01', 160, 1120),
(1, '2021-02', 165, 1160),
(1, '2021-03', 170, 1190),
(1, '2021-04', 180, 1260),
(1, '2021-05', 175, 1230),
(1, '2021-06', 185, 1290),
(1, '2021-07', 190, 1330),
(1, '2021-08', 200, 1400),
(1, '2021-09', 195, 1380),
(1, '2021-10', 205, 1440),
(1, '2021-11', 210, 1470),
(1, '2021-12', 215, 1500),
(1, '2022-01', 180, 1260),
(1, '2022-02', 185, 1300),
(1, '2022-03', 190, 1330),
(1, '2022-04', 195, 1360),
(1, '2022-05', 200, 1400),
(1, '2022-06', 205, 1440),
(1, '2022-07', 210, 1470),
(1, '2022-08', 215, 1500),
(1, '2022-09', 225, 1580),
(1, '2022-10', 230, 1610),
(1, '2022-11', 235, 1650),
(1, '2022-12', 240, 1680),
(1, '2023-01', 245, 1720),
(1, '2023-02', 250, 1750),
(1, '2023-03', 260, 1800),
(1, '2023-04', 265, 1850),
(1, '2023-05', 270, 1880),
(1, '2023-06', 275, 1920);

select * from [dbo].[users]
SELECT * FROM bills WHERE user_id = 1 ORDER BY month;