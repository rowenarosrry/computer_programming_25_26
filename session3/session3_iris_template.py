# <<<<<<< Updated upstream


# Session 2 continuity variables (Rule settings). Do not change these.
THRESHOLD = 2.0
FEATURE_NAME = "petal_length"
POSITIVE_LABEL = "setosa"
NEGATIVE_LABEL = "not_setosa"
LABEL_KEY = "species"




# >>>>>>> Stashed changes
correct = 0      # Count of correct predictions
wrong = 0        # Count of wrong predictions
total = 0        # Total samples processed
y_pred_list = []  # List of all predictions made


flower1 = {
    "id": "flower1",
    "sepal_length": 5.1,
    "sepal_width": 3.5,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

# Task 1: Create A dictionary for second flower

flower2 = {
    "id": "flower2",
    "sepal_length": 4.9,
    "sepal_width": 3.0,
    "petal_length": 1.4,
    "petal_width": 0.2,
    "species": "setosa"
}

# <your code here> remember to close me for a dict


# Task 2: Create list of dictionaries
dataset= [flower1, flower2]  # Add more flowers to the list as needed}
threshold = 2.0
feature_name = "petal_length"
positive_label = "setosa"
negative_label = "not_setosa"
label_key = "species"

# Task 3: Create a for loop to process the dataset
for sample in dataset:
    print(sample["id"], sample["petal_length"], sample["species"])

    # Task 4: Use an if-else statement to classify each sample
    if sample["petal_length"] < threshold:
        y_pred = positive_label
    else:
        y_pred = negative_label

    # Task 5
    if sample[LABEL_KEY] == POSITIVE_LABEL:
        y_true = POSITIVE_LABEL
    else:
        y_true = NEGATIVE_LABEL

    # Task 6
    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1

    # Task 7
    total += 1

    # Task 8
    y_pred_list.append(y_pred)

    # Task 9
    print(f"id={sample['id']} | true={y_true} | pred={y_pred} | "
        f"petal_length={sample['petal_length']}")
    
# Task 10: Print final results
accuracy = (correct / total) * 100 if total > 0 else 0.0

print("\n=== session 3 Summary ===")
print("Correct:", correct)
print("Wrong:", wrong)
print("Total:", total)
print("Accuracy (%):", round(accuracy, 2))
print("All predictions:", y_pred_list)