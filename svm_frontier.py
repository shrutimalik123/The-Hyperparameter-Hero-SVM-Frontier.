import random

def svm_frontier_game():
    # 1. Scenario Setup
    # Features: Scan Accuracy (0-10) and Pulse Rate (0-10)
    # Authorized (A) vs. Intruders (I)
    print("--- 🛡️ THE HYPERPARAMETER HERO: SVM FRONTIER 🛡️ ---")
    print("Mission: Tune your SVM biometric scanner to separate data points.")
    print("Authorized Users: High Accuracy, Steady Pulse.")
    print("Intruders: Variable Accuracy, High Stress Pulse.")

    # 2. Hyperparameter Tuning
    print("\n--- STEP 1: CONFIGURE THE KERNEL ---")
    print("1) Linear: Draw a straight line (Good for simple data).")
    print("2) RBF (Radial Basis Function): Create circular boundaries (Good for complex patterns).")
    kernel = input("Select Kernel (1-2): ")

    print("\n--- STEP 2: SET REGULARIZATION (C) ---")
    print("C determines the trade-off between a smooth boundary and classifying points correctly.")
    print("Low C: Smooth, simple boundary (permits some errors).")
    print("High C: Complex boundary (tries to get every point right).")
    try:
        c_val = float(input("Enter C value (e.g., 0.1, 1.0, 100.0): "))
    except ValueError:
        c_val = 1.0

    # 3. Model Simulation Logic
    print("\n--- 🖥️ CALCULATING HYPERPLANE... ---")
    
    # Decision Logic
    if kernel == "1": # Linear
        if c_val < 1:
            result = "The scanner is too relaxed. 🔓 Security Breach! Intruders slipped through."
        elif c_val > 10:
            result = "The scanner is too rigid. 🚫 System Lockout! Valid employees can't get in."
        else:
            result = "Optimal Linear Fit. Simple and effective security."
            
    else: # RBF (Complex pattern)
        if c_val < 5:
            result = "The circle is too wide. ⚠️ Over-generalization. Accuracy is low."
        elif c_val > 50:
            result = "The model is OVERFITTING. It's chasing 'outliers' (noise). 📉 Unstable performance."
        else:
            result = "🏆 MASTER CLASSIFIER: The RBF Kernel with balanced C perfectly captured the pattern!"

    # 4. Final Output
    print(f"\nRESULTS for Kernel={'Linear' if kernel=='1' else 'RBF'} and C={c_val}:")
    print(f"Outcome: {result}")

if __name__ == "__main__":
    svm_frontier_game()
