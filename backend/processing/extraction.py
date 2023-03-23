import pandas as pd
import numpy as np
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns

# Load the pre-trained language model
pretrained_model = fasttext.load_model('cc.en.300.bin')


# Define a function to fine-tune the pre-trained model on the training data
def train_model(training_data):
    # Convert the training data to a format compatible with FastText
    training_data['text'] = training_data['text'].apply(lambda x: ' '.join(x))
    training_data['label'] = '__label__' + training_data['label'].astype(str)
    training_data.to_csv('training_data.txt', sep=' ', index=False, header=False)

    # Fine-tune the pre-trained model on the training data
    model = fasttext.train_supervised(input='training_data.txt')

    # Return the fine-tuned model
    return model


# Define a function to evaluate the performance of the trained model
def evaluate_model(model, test_data):
    # Predict the labels for the test data
    y_pred = [model.predict(text)[0][0].replace('__label__', '') for text in test_data['text']]

    # Calculate various performance metrics
    accuracy = np.mean(y_pred == test_data['label'])
    report = classification_report(test_data['label'], y_pred)
    conf_matrix = confusion_matrix(test_data['label'], y_pred, labels=test_data['label'].unique())

    # Print the performance metrics
    print(f"Accuracy: {accuracy:.3f}\n")
    print(f"Classification Report:\n{report}\n")
    print(f"Confusion Matrix:\n{conf_matrix}\n")

    # Plot the confusion matrix as a heatmap
    sns.set(font_scale=1.2)
    plt.figure(figsize=(10, 8))
    sns.heatmap(conf_matrix, annot=True, fmt='g', cmap='Blues', xticklabels=test_data['label'].unique(),
                yticklabels=test_data['label'].unique())
    plt.title('Confusion Matrix')
    plt.xlabel('Predicted label')
    plt.ylabel('True label')
    plt.show()


# Load the training data from a Pandas DataFrame
training_data = pd.DataFrame({
    'text': [
        ['hard', 'working', 'developer', 'experienced', 'python'],
        ['creative', 'designer', 'experience', 'adobe', 'photoshop'],
        ['team', 'player', 'good', 'communication', 'skills'],
        ['javascript', 'expert', 'react', 'redux', 'angular'],
        ['problem', 'solver', 'critical', 'thinking', 'skills']
    ],
    'label': ['python', 'adobe', 'communication', 'javascript', 'problem_solving']
})

# Train the model on the training data
model = train_model(training_data)

# Load the test data from a Pandas DataFrame
test_data = pd.DataFrame({
    'text': [
        ['skilled', 'python', 'developer'],
        ['creative', 'web', 'designer'],
        ['team', 'player', 'good', 'communication'],
        ['react', 'redux', 'expert'],
        ['critical', 'thinker', 'problem', 'solver']
    ],
    'label': ['python', 'design', 'communication', 'javascript', 'problem_solving']
})

# Evaluate the performance of the trained model on the test data
evaluate_model(model, test_data)
