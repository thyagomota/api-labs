DROP TABLE IF EXISTS quote_tags;
DROP TABLE IF EXISTS quotes;

CREATE TABLE quotes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    text VARCHAR(255) NOT NULL, 
    author VARCHAR(100) NOT NULL, 
    popularity DECIMAL(7, 2), 
    category VARCHAR(100)
);

CREATE TABLE quote_tags (
    id INT NOT NULL, 
    tag VARCHAR(30) NOT NULL,
    PRIMARY KEY (id, tag), 
    FOREIGN KEY (id) REFERENCES quotes (id) 
);

CREATE TABLE keys (
    key VARCHAR(32) PRIMARY KEY
);

INSERT INTO keys VALUES
    ('TyA0BhKO5SgCmodHzGyFlv1PqI4BqOzk0tu1gMr0Gsc'), 
    ('NQs7PF3MvoVQazuiYj2T7m9-jMji53WOuE_kyo6CHV4'), 
    ('g29suJUerHjHqeWTl04jSDg12eTyvaAV9q_0zekffKo');