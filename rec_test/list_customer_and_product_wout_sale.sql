SELECT "customer", customer.id, customer.customer_name
FROM customer
LEFT JOIN invoice ON customer.id = invoice.customer_id
WHERE invoice.customer_id IS NULL

UNION

SELECT "product", product.id, product_name
FROM product
LEFT JOIN invoice_item ON product.id = invoice_item.product_id
WHERE invoice_item.product_id IS NULL;
