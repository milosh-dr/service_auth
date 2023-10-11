CREATE USER 'auth_user'@'localhost' IDENTIFIED BY 'auth123';

CREATE DATABASE auth;

GRANT ALL PRIVILEGES ON auth.* TO 'auth_user'@'localhost';

USE auth;

CREATE TABLE user (
    id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
    e_mail VARCHAR(255) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL
);

INSERT INTO user(e_mail, password) VALUES('milosh-dr@wp.pl', 'D@nusia12')