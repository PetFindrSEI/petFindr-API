DROP DATABASE petfindr;
DROP USER petfindruser;

CREATE DATABASE petfindr;
CREATE USER petfindruser WITH PASSWORD 'petfindr';
GRANT ALL PRIVILEGES ON DATABASE petfindr TO petfindruser;