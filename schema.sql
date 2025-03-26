DROP TABLE IF EXISTS posts;

CREATE TABLE posts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    title TEXT NOT NULL,
    content TEXT NOT NULL
);

CREATE TABLE jobs (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    job_title TEXT NOT NULL,
    company TEXT NOT NULL,
    remote_q TEXT CHECK(remote_q IN ('yes', 'no', 'hybrid')) NOT NULL,
    applied TEXT CHECK (applied IN ('applied', 'interested', 'interviewing', 'hired', 'denied')) NOT NULL,
    applied_date DATE,
    link TEXT,
    comments TEXT
);