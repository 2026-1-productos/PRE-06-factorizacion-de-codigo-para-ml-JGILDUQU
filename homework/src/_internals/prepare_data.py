import pandas as pd
from sklearn.model_selection import train_test_split


def prepare_data(
    file_path="http://archive.ics.uci.edu/ml/machine-learning-databases/"
    "wine-quality/winequality-red.csv",
    test_size=0.25,
    random_state=123456,
):
    df = pd.read_csv(file_path, sep=";")

    y = df["quality"]
    x = df.copy()
    x.pop("quality")

    x_train, x_test, y_train, y_test = train_test_split(
        x,
        y,
        test_size=test_size,
        random_state=random_state,
    )

    return x_train, x_test, y_train, y_test
