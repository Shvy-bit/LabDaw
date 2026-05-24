CREATE TABLE person (
    id SERIAL PRIMARY KEY,
    "name" VARCHAR(50) NOT NULL,
    dni_ruc VARCHAR(15) UNIQUE NOT NULL,
    "number" VARCHAR(15),
    email VARCHAR(50)
);
CREATE TABLE shops (
    id SERIAL PRIMARY KEY,
    shop_name VARCHAR(20) NOT NULL,
    street VARCHAR(20)
);
CREATE TABLE users (
    id_person INT PRIMARY KEY,
    id_shop INT NOT NULL,
    username VARCHAR(15) NOT NULL,
    password_hash VARCHAR(255) NOT NULL,

    FOREIGN KEY (id_person) REFERENCES person(id),
    FOREIGN KEY (id_shop) REFERENCES shops(id)
);
CREATE TABLE clients (
    id_person INT PRIMARY KEY,
    wholesaler BOOLEAN NOT NULL,
    city VARCHAR(20),
    street VARCHAR(20) NOT NULL,

    FOREIGN KEY (id_person) REFERENCES person(id)
);
CREATE TABLE sale (
    id SERIAL PRIMARY KEY,
    id_user INT NOT NULL,
    id_client INT NOT NULL,
    total DECIMAL NOT NULL,
    "date" DATE NOT NULL,
    "hour" TIME NOT NULL,

    FOREIGN KEY (id_user) REFERENCES users(id_person),
    FOREIGN KEY (id_client) REFERENCES clients(id_person)
);
CREATE TABLE units (
    id SERIAL PRIMARY KEY,
    unit_name VARCHAR(20)  NOT NULL
);
CREATE TABLE products (
    id SERIAL PRIMARY KEY,
    prod_name VARCHAR(20) NOT NULL,
    prod_description VARCHAR(50) NOT NULL,
    price_buy DECIMAL NOT NULL,
    price_sale DECIMAL NOT NULL,
    price_wholesale DECIMAL NOT NULL,
    id_unit INT NOT NULL,

    FOREIGN KEY (id_unit) REFERENCES units(id)
);
CREATE TABLE inventory (
    id SERIAL PRIMARY KEY,
    id_prod INT NOT NULL,
    id_shop INT NOT NULL,
    amount INT NOT NULL,
    amount_min INT NOT NULL,

    FOREIGN KEY (id_prod) REFERENCES products(id),
    FOREIGN KEY (id_shop) REFERENCES shops(id)
);
CREATE TABLE sale_detail (
    id SERIAL PRIMARY KEY,
    id_sale INT NOT NULL,
    id_prod INT NOT NULL,
    amount INT NOT NULL,
    price_unit DECIMAL NOT NULL,
    subtotal DECIMAL NOT NULL,

    FOREIGN KEY (id_sale) REFERENCES sale(id),
    FOREIGN KEY (id_prod) REFERENCES products(id)
);