DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS products;
DROP TABLE IF EXISTS reserved;

CREATE TABLE users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  username TEXT UNIQUE NOT NULL,
  password TEXT NOT NULL,
  fitbit_user_id TEXT NOT NULL
);

CREATE TABLE products (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  price FLOAT NOT NULL
);

CREATE TABLE reserved (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	user_id INTEGER NOT NULL,
	product_id INTEGER NOT NULL,
	amount_paid FLOAT NOT NULL,
	last_step_count INTEGER NOT NULL,
	FOREIGN KEY (user_id) REFERENCES users (id),
	FOREIGN KEY (product_id) REFERENCES products (id)
);

INSERT INTO users
VALUES (1, 'asankar', 'abcd', 'who knows');

