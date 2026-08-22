"""
AI Student Attendance Tracker - ML Model Training Script
Trains a Random Forest Classifier to predict student attendance risk.
"""

import os
import json
import numpy as np
import pandas as pd
from datetime import datetime
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
import joblib

def generate_synthetic_data(num_samples=2500, random_state=42):
    """
    Generates a realistic synthetic dataset simulating student attendance,
    academic participation, and performance metrics.
    """
    np.random.seed(random_state)
    
    # 1. Base Attendance Percentage (bounded between 25 and 100)
    attendance_pct = np.clip(np.random.normal(loc=76, scale=14, size=num_samples), 25.0, 100.0)
    
    # 2. Total classes simulated (e.g. 50 classes)
    total_classes = 50
    absent_days = np.round((100.0 - attendance_pct) / 100.0 * total_classes).astype(int)
    absent_days = np.clip(absent_days, 0, total_classes)
    
    # 3. Consecutive Absences (correlated with absent_days and low attendance)
    consecutive_absences = []
    for att, abs_d in zip(attendance_pct, absent_days):
        if att < 50:
            c = np.random.choice([3, 4, 5, 6, 7], p=[0.15, 0.25, 0.3, 0.2, 0.1])
        elif att < 65:
            c = np.random.choice([1, 2, 3, 4, 5], p=[0.1, 0.3, 0.35, 0.15, 0.1])
        elif att < 75:
            c = np.random.choice([0, 1, 2, 3], p=[0.2, 0.45, 0.25, 0.1])
        elif att < 85:
            c = np.random.choice([0, 1, 2], p=[0.5, 0.4, 0.1])
        else:
            c = np.random.choice([0, 1], p=[0.85, 0.15])
        consecutive_absences.append(c)
    consecutive_absences = np.array(consecutive_absences)
    
    # 4. Attendance Trend (recent 10-day attendance percentage)
    # Trend can be deteriorating, stable, or improving
    trend_noise = np.random.normal(loc=0, scale=8, size=num_samples)
    attendance_trend = np.clip(attendance_pct + trend_noise, 15.0, 100.0)
    
    # 5. Internal Marks (0 - 100, correlated with attendance)
    internal_marks = np.clip(0.6 * attendance_pct + np.random.normal(loc=28, scale=12, size=num_samples), 10.0, 100.0)
    
    # 6. Assignment Completion (0 - 100%, correlated with attendance and marks)
    assignment_completion = np.clip(0.5 * attendance_pct + 0.3 * internal_marks + np.random.normal(loc=15, scale=10, size=num_samples), 15.0, 100.0)
    
    # 7. Activity Score (0 - 100, engagement/lab activity)
    activity_score = np.clip(0.4 * attendance_pct + 0.4 * assignment_completion + np.random.normal(loc=15, scale=12, size=num_samples), 10.0, 100.0)
    
    # Logical Target Generation: SAFE, AT_RISK, CRITICAL
    labels = []
    for att, abs_d, cons, trend, marks, assign, act in zip(
        attendance_pct, absent_days, consecutive_absences, attendance_trend, internal_marks, assignment_completion, activity_score
    ):
        # Critical criteria:
        # Very low attendance (<60%) OR heavy consecutive absences (>=4) OR severe academic lag with attendance < 68%
        if att < 58.0 or cons >= 4 or (att < 65.0 and marks < 50.0) or (trend < 50.0 and att < 65.0):
            labels.append("CRITICAL")
        # At Risk criteria:
        # Attendance between 58% and 74.9% OR consecutive absences 2-3 with declining trend OR low marks with borderline attendance
        elif att < 75.0 or cons >= 2 or (att < 80.0 and marks < 55.0) or (trend < 65.0 and att < 78.0) or (assign < 50.0 and att < 76.0):
            labels.append("AT_RISK")
        # Safe criteria:
        else:
            labels.append("SAFE")
            
    df = pd.DataFrame({
        "attendance_percentage": np.round(attendance_pct, 2),
        "absent_days": absent_days,
        "consecutive_absences": consecutive_absences,
        "attendance_trend": np.round(attendance_trend, 2),
        "internal_marks": np.round(internal_marks, 2),
        "assignment_completion": np.round(assignment_completion, 2),
        "activity_score": np.round(activity_score, 2),
        "target": labels
    })
    
    return df

def train_and_evaluate():
    print("=" * 60)
    print("AI Student Attendance Tracker - Model Training")
    print("=" * 60)
    print("Generating synthetic student dataset...")
    
    df = generate_synthetic_data(num_samples=2500, random_state=42)
    print(f"Dataset generated successfully. Total records: {len(df)}")
    print("Class distribution:")
    print(df['target'].value_counts())
    
    feature_cols = [
        "attendance_percentage",
        "absent_days",
        "consecutive_absences",
        "attendance_trend",
        "internal_marks",
        "assignment_completion",
        "activity_score"
    ]
    
    X = df[feature_cols]
    y = df["target"]
    
    # 80% Train, 20% Test stratified split
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y
    )
    
    print("\nTraining Random Forest model...")
    rf_model = RandomForestClassifier(
        n_estimators=120,
        max_depth=9,
        min_samples_split=4,
        min_samples_leaf=2,
        random_state=42,
        class_weight="balanced"
    )
    rf_model.fit(X_train, y_train)
    
    # Evaluate on actual test set
    y_pred = rf_model.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)
    acc_percentage = round(float(test_accuracy * 100), 2)
    
    print(f"Training completed.")
    print(f"Test Accuracy: {acc_percentage}%")
    print("\nDetailed Classification Report:")
    print(classification_report(y_test, y_pred))
    
    # Feature importances
    importances = dict(zip(feature_cols, [round(float(v), 4) for v in rf_model.feature_importances_]))
    print("Feature Importances:")
    for feat, imp in importances.items():
        print(f"  - {feat}: {imp}")
        
    # Save model and metadata
    os.makedirs("model", exist_ok=True)
    model_path = os.path.join("model", "attendance_risk_model.pkl")
    metadata_path = os.path.join("model", "model_metadata.json")
    
    joblib.dump(rf_model, model_path)
    print(f"\nModel saved successfully at: {model_path}")
    
    metadata = {
        "model_name": "Random Forest Classifier",
        "algorithm": "RandomForestClassifier",
        "n_estimators": 120,
        "max_depth": 9,
        "features": feature_cols,
        "classes": list(rf_model.classes_),
        "dataset_size": len(df),
        "train_samples": len(X_train),
        "test_samples": len(X_test),
        "test_accuracy": acc_percentage,
        "feature_importances": importances,
        "trained_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "status": "Production Ready"
    }
    
    with open(metadata_path, "w") as f:
        json.dump(metadata, f, indent=4)
        
    print(f"Model metadata saved at: {metadata_path}")
    print("=" * 60)
    return acc_percentage

if __name__ == "__main__":
    train_and_evaluate()
