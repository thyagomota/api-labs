DROP TABLE IF EXISTS quote_tags;
DROP TABLE IF EXISTS quotes;

CREATE TABLE quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text VARCHAR(255) NOT NULL, 
    author VARCHAR(100) NOT NULL, 
    popularity FLOAT
);

CREATE TABLE quote_tags (
    id INT NOT NULL, 
    tag VARCHAR(30) NOT NULL,
    PRIMARY KEY (id, tag), 
    FOREIGN KEY (id) REFERENCES quotes (id) 
);