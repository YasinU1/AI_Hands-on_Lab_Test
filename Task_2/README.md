# AI_Hands-on_Lab_Test
# Task 2
Improvements to the original model are below, implemented in the task2.ipynb notebook
1. Feature Engineering and Selection:
    - Car Age Calculation: Determining the age of the car allows us to better understand its depreciation, which is critical for price prediction.
    - Mileage Per Year: This feature provides information about the car's usage intensity. A car that has a high mileage in a short period of time may depreciate faster.
2. Data Augmentation: 
    - Enhancing the dataset by creating synthetic variations can help improve model robustness and generalization.
3. Recursive Feature Elimination (RFECV): 
    - Recursive Feature Elimination (RFECV): This method aids in selecting the most relevant features while preventing noise from distracting the model.
4. Cross-validation:
    - Stratified K-Fold : This ensures that each fold is a good representation of the entire dataset, resulting in a more robust model evaluation.
5. Hyperparameter Tuning:
    - Using Bayesian Optimisation: It is a more efficient hyperparameter tuning method that finds the best parameters faster than traditional grid or random search methods.
6. Ensemble Methods:
    - Gradient Boosting with Early Stopping: Gradient Boosting constructs trees sequentially, correcting errors from previous trees. By halting training when performance reaches a plateau, early stopping ensures that the model does not overfit.
7. Model Evaluation: 
    - RMSE and MAE Metrics: These metrics provide a quantitative measure of model errors, which aids in understanding the accuracy of prediction.
    - Visualisation of Feature Importance: By visualising which features contribute the most, we can focus on gathering quality data for those features in the future.

# Model Comparison:

**Old Model (Model 1):**
- Root Mean Squared Error (RMSE): 4537.93
- Mean Absolute Error (MAE): 3281.50

**New Model (Model 2):**
- Root Mean Squared Error (RMSE): 3265.65
- Mean Absolute Error (MAE): 2315.96

In comparison to Model 1, Model 2 has a lower RMSE and MAE. As a result of these metrics, Model 2 outperforms Model 1 in terms of prediction accuracy.

# Recommendations for Future Work:

1. **Regularization Techniques:**
   - Consider both L1 and L2 regularization or dropout methods to reduce overfitting.

2. **Data Cleaning:**
   - Ensure a clean dataset, free of outliers and missing values, to improve model performance significantly.

3. **Advanced Feature Engineering:**
   - Explore interaction terms or polynomial features, which may be more effective at capturing non-linear relationships.

4. **Model Stacking:**
   - Implement model stacking, a technique that combines predictions from multiple models to produce more accurate results.

5. **Deep Learning:**
   - Explore the potential of neural networks for capturing complex patterns more effectively in large datasets.
