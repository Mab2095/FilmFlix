DROP TABLE IF EXISTS films;

CREATE TABLE films (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
	title TEXT NOT NULL,
	yearReleased  TEXT NOT NULL,
	rating TEXT NOT NULL,
    duration TEXT NOT NULL,
    genre TEXT NOT NULL
);