
\connect fruitst;

CREATE TABLE "order" (
    id character varying PRIMARY KEY,
    date double precision NOT NULL
);


ALTER TABLE "order" OWNER TO fruitst;

CREATE TABLE order_item (
    fruit_name character varying NOT NULL,
    amount double precision NOT NULL,
    order_id character varying NOT NULL,
    PRIMARY KEY (fruit_name, order_id),
    CONSTRAINT order_item_order_id_fkey FOREIGN KEY (order_id) REFERENCES "order"(id)
);


ALTER TABLE order_item OWNER TO fruitst;
