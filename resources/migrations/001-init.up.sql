CREATE EXTENSION pgcrypto;
--;;
CREATE TABLE players (
    id          UUID PRIMARY KEY DEFAULT gen_random_uuid(),
    firstname   TEXT,
    lastname    TEXT,
    email       TEXT
);