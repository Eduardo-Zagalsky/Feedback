DROP DATABASE IF EXISTS feedback;

CREATE DATABASE feedback;

\c feedback
CREATE TABLE users (
    username varchar(20) PRIMARY KEY,
    pwd text NOT NULL,
    email varchar(50) NOT NULL UNIQUE,
    first_name varchar(30) NOT NULL,
    last_name varchar(30) NOT NULL
);

