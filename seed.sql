DROP DATABASE IF EXISTS feedback;

CREATE DATABASE feedback;

\c feedback
CREATE TABLE users (
    username varchar(20) PRIMARY KEY,
    password text NOT NULL,
    email varchar(50) NOT NULL UNIQUE,
    first_name varchar(30) NOT NULL,
    last_name varchar(30) NOT NULL
);

CREATE TABLE feedback (
    id INTEGER serial PRIMARY KEY,
    title varchar(100) NOT NULL,
    content text NOT NULL,
    username text REFERENCES users (username)
);

