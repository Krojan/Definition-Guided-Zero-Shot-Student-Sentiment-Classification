from sklearn.metrics import (
    confusion_matrix,
    classification_report,
)
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

sample = {
    "comment": [
        "i think there needs to be an expansion. one question is not enough.",
        "not too sure. don't have a ton of exposure to the services.",
        "i have looked at group counseling but they are not for me.",
        "not much in my opinion i’d working well. i think it’s fine.",
        "the group sessions for stress relief and meditation were helpful.",
        "i am a fully online student and i wish i was able to attend in-person sessions.",
        "access to counselors is simple (from my experience).",
        "the counseling center is just burdened with the number of students.",
        "i believe that for many, the addition of having peer counselors helped.",
        "many students base assumptions on all staff based on one experience.",
    ],
    "Validated_Labels": [
        "dissatisfied",
        "neutral",
        "dissatisfied",
        "dissatisfied",
        "satisfied",
        "dissatisfied",
        "mixed",
        "dissatisfied",
        "satisfied",
        "dissatisfied",
    ],
    "Predicted_labels": [
        "dissatisfied",
        "neutral",
        "dissatisfied",
        "dissatisfied",
        "mixed",
        "dissatisfied",
        "mixed",
        "dissatisfied",
        "satisfied",
        "dissatisfied",
    ],
}


def compute_confusion_matrix(y_actual, y_predicted):
    labels = y_actual.unique()
    cm = confusion_matrix(y_actual, y_predicted, labels=labels)
    # C[i, j] = no of examples in group i predicted as group j so i = y-axis = actual, j = x-axis = predicted
    cm_df = pd.DataFrame(
        cm,
        index=[f"{x}" for x in labels],  # actual
        columns=[f"{x}" for x in labels],  # predicted
    )
    cm_norm = confusion_matrix(y_actual, y_predicted, labels=labels, normalize="true")
    cm_norm_df = pd.DataFrame(
        cm_norm * 100,
        index=[f"{x}" for x in labels],
        columns=[f"{x}" for x in labels],
    )
    return cm_df, cm_norm_df, labels


def compute_classification_report(y_actual, y_predicted):
    print("Classification Report:")
    report = classification_report(y_actual, y_predicted, digits=2)
    print(report)


def plot_confusion_matrix(
    cm_df, x_label="Predicted", y_label="Actual", title="Confusion Matrix"
):
    plt.figure(figsize=(8, 6))
    sns.heatmap(
        cm_df,
        annot=True,
        fmt=".1f",
        cmap="Blues",
    )
    plt.title(title)
    plt.ylabel(y_label)
    plt.xlabel(x_label)
    plt.tight_layout()
    plt.show()


def run_analysis(df):
    cm_count, cm_norm, _ = compute_confusion_matrix(
        df["Validated_Labels"], df["Predicted_labels"]
    )
    plot_confusion_matrix(cm_count)
    plot_confusion_matrix(cm_norm, title="Confusion Matrix (Normalized)")
    compute_classification_report(df["Validated_Labels"], df["Predicted_labels"])


# df = pd.DataFrame(sample)
# run_analysis(df)
