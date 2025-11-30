"""
Simple scikit-learn starter: Predicting house prices
This demonstrates the core ML workflow that applies to all scikit-learn models
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import fetch_california_housing
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Step 1: Load data
print("Loading California housing dataset...")
data = fetch_california_housing(as_frame=True)
df = data.frame  # Pandas DataFrame
print(f"Dataset shape: {df.shape}")
print(f"\nFirst few rows:\n{df.head()}")

# Step 2: Prepare features (X) and target (y)
X = df.drop('MedHouseVal', axis=1)  # All columns except target
y = df['MedHouseVal']  # Target: median house value

print(f"\nFeatures: {list(X.columns)}")
print(f"Target: Median House Value (in $100,000s)")

# Step 3: Split into training and testing sets
# 80% for training, 20% for testing
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)
print(f"\nTraining samples: {len(X_train)}")
print(f"Testing samples: {len(X_test)}")

# Step 4: Create and train the model
print("\nTraining Linear Regression model...")
model = LinearRegression()
model.fit(X_train, y_train)
print("Training complete!")

# Step 5: Make predictions
y_pred = model.predict(X_test)

# Step 6: Evaluate performance
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print(f"\nModel Performance:")
print(f"  RMSE: ${rmse * 100000:.2f}")  # Convert back to dollars
print(f"  R² Score: {r2:.3f}")
print(f"  (R² of 1.0 = perfect predictions, 0.0 = baseline)")

# Step 7: Visualize predictions vs actual values
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.plot([y_test.min(), y_test.max()], [y_test.min(), y_test.max()],
         'r--', lw=2, label='Perfect prediction')
plt.xlabel('Actual Price ($100k)')
plt.ylabel('Predicted Price ($100k)')
plt.title('Predicted vs Actual House Prices')
plt.legend()
plt.tight_layout()
plt.savefig('predictions.png')
print(f"\nVisualization saved as 'predictions.png'")

# Bonus: Show feature importance (coefficients)
feature_importance = pd.DataFrame({
    'Feature': X.columns,
    'Coefficient': model.coef_
}).sort_values('Coefficient', key=abs, ascending=False)

print(f"\nFeature Importance (coefficients):")
print(feature_importance)
