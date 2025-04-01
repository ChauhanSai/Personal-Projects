import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
import tensorflow as tf
from tensorflow.keras import layers
from tensorflow.keras.models import Model
from sklearn.metrics import classification_report, confusion_matrix
import matplotlib.pyplot as plt
import seaborn as sns
import joblib  # For saving the scaler

# Global variables for model configuration
NUM_HEADS = 4  # Number of attention heads
KEY_DIM = 64   # Key dimension for MultiHeadAttention
DENSE_LAYER_1_UNITS = 128  # Units in the first dense layer
DENSE_LAYER_2_UNITS = 64   # Units in the second dense layer
EPOCHS = 20  # Number of training epochs
BATCH_SIZE = 32  # Batch size for training

# Load the dataset
data_path = 'data/thedevastator/cancer-patients-and-air-pollution-a-new-link.csv'
data = pd.read_csv(data_path)

# Preprocessing
# Drop unnecessary columns
data.drop(['index', 'Patient Id'], axis=1, inplace=True)

# Encode categorical variables
label_encoders = {}
for column in ['Gender']:
    le = LabelEncoder()
    data[column] = le.fit_transform(data[column])
    label_encoders[column] = le

# Separate features and target
X = data.drop('Level', axis=1)

# Encode target variable with custom mapping
level_mapping = {'Low': 0, 'Medium': 1, 'High': 2}  # Updated mapping to start from 0
y = data['Level'].map(level_mapping)

# Print the mapping for reference
print("Level Mapping:", level_mapping)

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Scale the features
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Save the fitted scaler
joblib.dump(scaler, 'model/severityScaler.pkl')

# Transformer model
def create_transformer_model(input_dim):
    inputs = layers.Input(shape=(input_dim,))
    x = layers.Dense(DENSE_LAYER_1_UNITS, activation='relu')(inputs)
    x = layers.LayerNormalization()(x)
    
    # Reshape input for MultiHeadAttention (add a time dimension)
    x = layers.Reshape((1, x.shape[-1]))(x)
    attention_output = layers.MultiHeadAttention(num_heads=NUM_HEADS, key_dim=KEY_DIM)(x, x)
    
    # Flatten the output back to 2D
    x = layers.Flatten()(attention_output)
    x = layers.LayerNormalization()(x)  # Normalize after attention
    x = layers.Dense(DENSE_LAYER_2_UNITS, activation='relu')(x)
    outputs = layers.Dense(3, activation='softmax')(x)  # Updated to softmax for multi-class classification
    model = Model(inputs, outputs)
    return model

# Create the model
input_dim = X_train.shape[1]
model = create_transformer_model(input_dim)

# Compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])  # Updated loss for multi-class classification

# Train the model
history = model.fit(X_train, y_train, validation_data=(X_test, y_test), epochs=EPOCHS, batch_size=BATCH_SIZE)

# Save the model
model.save('model/severityModel.h5')

# Evaluate the model
loss, accuracy = model.evaluate(X_test, y_test)
print(f"Test Accuracy: {accuracy:.2f}")

# Generate predictions
y_pred = model.predict(X_test)
y_pred = np.argmax(y_pred, axis=1)  # No need to add 1, as labels are already in the range [0, 2]

# Classification report and confusion matrix
print("Classification Report:")
print(classification_report(y_test, y_pred, target_names=['Low', 'Medium', 'High'], zero_division=0))

print("Confusion Matrix:")
cm = confusion_matrix(y_test, y_pred)
print(cm)

# Plot confusion matrix
def plot_confusion_matrix(cm, class_names):
    plt.figure(figsize=(8, 6))
    sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_names, yticklabels=class_names)
    plt.xlabel('Predicted Labels')
    plt.ylabel('True Labels')
    plt.title('Confusion Matrix')
    plt.show()

# Generate and plot confusion matrix
class_names = ['Low', 'Medium', 'High']  # Updated class names
plot_confusion_matrix(cm, class_names)