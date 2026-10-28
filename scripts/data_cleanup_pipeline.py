import pandas as pd

def limpiar_datos_corruptos():
    print("--- INICIANDO PIPELINE DE RECUPERACIÓN Y LIMPIEZA DE DATOS ---")
    
    # Simulando una base de datos heredada (Legacy) llena de errores y caos
    raw_data = {
        'id_usuario': [101, 102, 102, 103, 104, 105], # Hay un ID duplicado
        'email': ['JUAN@EMAIL.COM', 'maria@email.com', 'MARIA@EMAIL.COM', None, 'carlos@email.com ', 'ana@email.com'], # Mayúsculas, nulos, espacios
        'monto_transaccion': [1500.0, 3200.5, 3200.5, -500.0, None, 4100.0], # Monto negativo absurdo y nulos
        'estado': ['COMPLETADO', 'FALLIDO', 'FALLIDO', 'COMPLETADO', 'PENDIENTE', 'COMPLETADO']
    }
    
    df = pd.DataFrame(raw_data)
    print(f"\n[!] Registros crudos iniciales detectados: {len(df)}")
    
    # 1. Eliminar duplicados exactos
    df = df.drop_duplicates()
    
    # 2. Normalizar correos (minúsculas y espacios limpios)
    df['email'] = df['email'].str.strip().str.lower()
    
    # 3. Filtrar anomalías críticas (montos negativos o nulos)
    df = df.dropna(subset=['email', 'monto_transaccion'])
    df = df[df['monto_transaccion'] > 0]
    
    print(f"[✔] Registros limpios y normalizados tras el pipeline: {len(df)}")
    print("\nDataFrame optimizado listo para re-ingesta segura:")
    print(df)

if __name__ == "__main__":
    limpiar_datos_corruptos()
