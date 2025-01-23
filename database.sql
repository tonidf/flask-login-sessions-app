-- CREATE DATABASE flask_login_2024_2025;
-- USE flask_login_2024_2025;

-- CREATE TABLE user(
--     id INT UNSIGNED AUTO_INCREMENT PRIMARY KEY,
--     username VARCHAR(30) NOT NULL, -- <-- Falta UNIQUE
--     password VARCHAR(255) NOT NULL,
--     fullname VARCHAR(50) NOT NULL
-- );

INSERT INTO user VALUES(NULL, 'Toni', 'scrypt:32768:8:1$7CCn4qspKKhBbLxU$67c3757bf0acee9266402ddf7b8e8f9fe38269b8bf4fe46876ad0546558c4b2dfbae002811511e7993d1e9ed288f6340f858fbdfddcfee3c53690223186ab193', 'Toni Díaz')