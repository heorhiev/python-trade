CREATE TABLE trade_price (
    id SERIAL PRIMARY KEY,
    symbol VARCHAR NOT NULL,
    platform VARCHAR NOT NULL,

    price INT NOT NULL,
    
    created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),
    updated_at TIMESTAMPTZ NULL
);
