SELECT 
products.name,
providers.name
FROM products
LEFT JOIN providers
ON products.id_providers = providers.id
WHERE id_categories = 6 ;
