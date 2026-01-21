import json
import joblib
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, f1_score, confusion_matrix


def main():
    # ======================
    # 1. Cargar dataset
    # ======================
    iris = load_iris(as_frame=True)
    X = iris.data
    y = iris.target

    df = pd.concat([X, y.rename("target")], axis=1)

    # ======================
    # 2. Info básica
    # ======================
    print("HEAD:")
    print(df.head())

    print("\nDESCRIBE:")
    print(df.describe())

    # ======================
    # 3. EDA mínima
    # ======================
    plt.figure()
    df["sepal length (cm)"].hist(bins=20)
    plt.title("Distribución de Sepal Length")
    plt.xlabel("cm")
    plt.ylabel("Frecuencia")
    plt.tight_layout()
    plt.show()

    # Observación:
    # La longitud del sépalo parece concentrarse en rangos definidos,
    # lo que sugiere que puede ser una variable útil para separar clases.

    # ======================
    # 4. Train / Test split
    # ======================
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )

    # ======================
    # 5. Pipeline
    # ======================
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LogisticRegression(max_iter=200))
    ])

    pipeline.fit(X_train, y_train)

    # ======================
    # 6. Evaluación
    # ======================
    y_pred = pipeline.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred, average="macro")
    cm = confusion_matrix(y_test, y_pred)

    print("\nAccuracy:", accuracy)
    print("F1 macro:", f1)
    print("Confusion matrix:\n", cm)

    # ======================
    # 7. Persistencia
    # ======================
    joblib.dump(pipeline, "model.joblib")

    metrics = {
        "accuracy": accuracy,
        "f1_macro": f1,
        "confusion_matrix": cm.tolist()
    }

    with open("metrics.json", "w") as f:
        json.dump(metrics, f, indent=4)

    print("\nModelo y métricas guardados correctamente.")


if __name__ == "__main__":
    main()
