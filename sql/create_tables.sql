-- Criação da tabela user
CREATE TABLE "user" (
    id SERIAL PRIMARY KEY,
    username VARCHAR(80) UNIQUE NOT NULL,
    email VARCHAR(255) UNIQUE NOT NULL,
    password VARCHAR(320) NOT NULL,
    created_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- Criação da tabela record
CREATE TABLE "record" (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES "user"(id),
    action VARCHAR(255) NOT NULL,
    timestamp TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP
);


-- Criação da tabela freelancers
CREATE TABLE freelancer (
    id SERIAL PRIMARY KEY,
    user_id INTEGER NOT NULL REFERENCES "user"(id),
    nome_completo VARCHAR(255) NOT NULL,
    celular VARCHAR(15) NOT NULL,
    sexo VARCHAR(1) NOT NULL, -- M, F, O
    email VARCHAR(255) NOT NULL,
    rg VARCHAR(20) NOT NULL,
    chave_pix VARCHAR(77) NOT NULL -- Chave PIX obrigatória com até 77 caracteres
);
