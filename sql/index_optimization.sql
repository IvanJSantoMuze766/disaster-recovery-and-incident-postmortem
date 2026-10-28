-- =====================================================================
-- POST-MORTEM SQL: Optimización de Índices y Resolución de Deadlocks
-- =====================================================================

-- 1. Análisis de consultas lentas que provocaron bloqueos en producción
-- Identificando transacciones sin indexar en tablas de alto tráfico
EXPLAIN QUERY PLAN 
SELECT * FROM orders 
WHERE user_id = 45892 AND status = 'PROCESSING';

-- 2. Creación de índices compuestos para acelerar búsquedas y evitar bloqueos de tabla
CREATE INDEX IF NOT EXISTS idx_orders_user_status 
ON orders(user_id, status);

-- 3. Limpieza de registros huérfanos que rompían las Foreign Keys
DELETE FROM order_items 
WHERE order_id NOT IN (SELECT id FROM orders);

-- 4. Optimización final del vacuum de la base de datos para recuperar espacio en disco
VACUUM;
