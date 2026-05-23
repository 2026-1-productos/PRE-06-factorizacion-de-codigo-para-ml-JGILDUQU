def print_metrics(mse, mae, r2, titulo):
    """
    Imprime las metricas de error de un modelo
    """
    print()
    print(titulo)
    print(f"  MSE: {mse}")
    print(f"  MAE: {mae}")
    print(f"  R2: {r2}")
