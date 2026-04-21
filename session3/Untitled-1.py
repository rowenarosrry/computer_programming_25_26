# --- Configuration / Constants ---

def get_threshold():
    """Returns the decision threshold for petal length."""
    return 2.0

def get_feature_name():
    """Returns the feature name used for classification."""
    return "petal_length"

def get_labels():
    """Returns a dictionary containing the label names and keys."""
    return {
        "positive": "setosa",
        "negative": "not_setosa",
        "key": "species"
    }

# --- Dataset Creation ---

def create_flower_data():
    """Creates individual flower dictionaries."""
    flower1 = {
        "id": "flower1",
        "sepal_length": 5.1,
        "sepal_width": 3.5,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }
    flower2 = {
        "id": "flower2",
        "sepal_length": 4.9,
        "sepal_width": 3.0,
        "petal_length": 1.4,
        "petal_width": 0.2,
        "species": "setosa"
    }
    return [flower1, flower2]

# --- Prediction / Classification ---

def classify_sample(petal_length, threshold, pos_label, neg_label):
    """Predicts the species based on the petal length threshold."""
    if petal_length < threshold:
        return pos_label
    else:
        return neg_label

def get_true_label(sample, label_key, pos_label, neg_label):
    """Determines the actual ground truth label for the sample."""
    if sample[label_key] == pos_label:
        return pos_label
    else:
        return neg_label

# --- Metrics Updates ---

def update_accuracy_counts(y_pred, y_true, correct, wrong):
    """Increments the correct or wrong counters based on prediction."""
    if y_pred == y_true:
        correct += 1
    else:
        wrong += 1
    return correct, wrong

def calculate_accuracy(correct, total):
    """Calculates the accuracy percentage."""
    return (correct / total) * 100 if total > 0 else 0.0

# --- Summary Printing ---

def print_sample_log(sample_id, true_label, pred_label, feature_val):
    """Prints the log for an individual sample process."""
    print(f"id={sample_id} | true={true_label} | pred={pred_label} | "
          f"petal_length={feature_val}")

def print_final_summary(correct, wrong, total, accuracy, predictions):
    """Prints the final session summary metrics."""
    print("\n=== session 3 Summary ===")
    print("Correct:", correct)
    print("Wrong:", wrong)
    print("Total:", total)
    print("Accuracy (%):", round(accuracy, 2))
    print("All predictions:", predictions)

# --- main() Execution ---

def main():
    # Initialize Configuration
    threshold = get_threshold()
    feature_name = get_feature_name()
    labels = get_labels()
    
    # Initialize Counters/Lists
    correct = 0
    wrong = 0
    total = 0
    y_pred_list = []

    # Get Dataset
    dataset = create_flower_data()

    # Process Dataset
    for sample in dataset:
        # Initial log print as per original code
        print(sample["id"], sample[feature_name], sample[labels["key"]])

        # Predict
        y_pred = classify_sample(
            sample[feature_name], 
            threshold, 
            labels["positive"], 
            labels["negative"]
        )

        # Get Ground Truth
        y_true = get_true_label(
            sample, 
            labels["key"], 
            labels["positive"], 
            labels["negative"]
        )

        # Update Metrics
        correct, wrong = update_accuracy_counts(y_pred, y_true, correct, wrong)
        total += 1
        y_pred_list.append(y_pred)

        # Print iteration results
        print_sample_log(sample["id"], y_true, y_pred, sample[feature_name])

    # Finalize and Output
    accuracy = calculate_accuracy(correct, total)
    print_final_summary(correct, wrong, total, accuracy, y_pred_list)

if __name__ == "__main__":
    main()