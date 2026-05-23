def compare_models(current_model, best_model, x_test, y_test):
    """
    Compare the current model with the best model and return the better one.
    """
    current_score = current_model.score(x_test, y_test)
    if best_model is None or current_score > best_model.score(x_test, y_test):
        return current_model
    return best_model
