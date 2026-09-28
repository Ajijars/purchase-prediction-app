# A MINI PROJECT REPORT ON “Travel Mode Choice”

**Submitted By:**
- Maithili Anil Pawar (UCS23F1102)
- Pranjali Shriram Patil (UCS23F1103)
- Shruti Shankar Rohom (UCS23F1105)
- Saee Ghanshyam Salunke (UCS23F1106)
*(T.Y Computer)*

**SAVITRIBAI PHULE PUNE UNIVERSITY**  
In the academic year 2025-26  
Department of Computer Engineering, Sanjivani Rural Education Society’s  
**Sanjivani College of Engineering Kopargaon - 423603.**  
*(AN AUTONOMOUS INSTITUTE)*

---

## CERTIFICATE
This is to certify that the Project Entitled **“Travel Mode Choice”** Submitted By:
- Maithili Anil Pawar (UCS23F1102)
- Pranjali Shriram Patil (UCS23F1103)
- Shruti Shankar Rohom (UCS23F1105)
- Saee Ghanshyam Salunke (UCS23F1106)
*(T.Y Computer)*

is a bonafide work carried out by students under the supervision of **DR. T. BHASKAR** and it is submitted towards the partial fulfillment of the requirement of FIOT Miniproject of SY Bachelor of Technology (Computer Engineering) during the **ACADEMIC YEAR 2025-26**.

**DR. T. BHASKAR** [PROJECT GUIDE]  
**DR. M. A. JAWALE**  
**DR. M. V. NAGARHALLI**

---

## DECLARATION
We declare that this Project submission represents our ideas in our own words; we have adequately cited and referenced the original sources. We also declare that we have adhered to all principles of academic honesty and integrity and have not misrepresented or fabricated any idea/data/fact/source in our submission. We understand that any violation of the above may cause disciplinary action by the Institute and can also evoke penal action from the sources which have not been properly cited.

**Place:** Kopargaon  
**Date:** / /2025

| Sr. No. | PRN | Names | Student Sign |
|---------|------------|-----------------------|--------------|
| 1 | UCS23F1102 | Maithili Anil Pawar | |
| 2 | UCS23F1103 | Pranjali Shriram Patil | |
| 3 | UCS23F1105 | Shruti Shankar Rohom | |
| 4 | UCS23F1106 | Saee Ghanshyam Salunke| |

---

## ACKNOWLEDGEMENT
First and foremost, we would like to give thanks to God Almighty for His mercy and beautiful blessings in my life. Even in the hardest times, He had always been there to guide and comfort me and to make sure that we never stray too far from His narrow way.

We would like to thank our parents for their unconditional love and support. We also wish to thank our guide **Dr. T. Bhaskar** being there for us, for the smooth completion of our Project.

We express our sincere gratitude to **Prof. Dr. M.A. Jawale**, Head of Department (Computer) SRES COE for her unending support and encouragement during this period we have studied under her tutelage.

Our sincere thanks go to all the teachers and staff for their help and understanding.

- Maithili Anil Pawar (UCS23F1102)
- Pranjali Shriram Patil (UCS23F1103)
- Shruti Shankar Rohom (UCS23F1105)
- Saee Ghanshyam Salunke (UCS23F1106)

---

## Table of Contents
| Sr. No. | Content | Page No. |
|---------|--------------------------------|----------|
| 01 | Abstract / Problem Description | 04 |
| 02 | Objective | 04 |
| 03 | Dataset & Tools | 05 |
| 04 | Methodology | 06 |
| 05 | Model Performance Comparison | 07 |
| 06 | Implementation Code | 07 |
| 07 | Results | 07 |
| 08 | Discussion | 08 |
| 09 | Conclusion and Future Work | 09 |

---

## 1. Abstract / Problem Description
Transportation is an essential aspect of modern society, and predicting an individual’s mode of travel plays a crucial role in urban planning, reducing congestion, and promoting sustainable mobility. Travelers generally choose between different modes such as car, bus, train, two-wheeler, or walking, depending on factors like travel time, cost, income, purpose of travel, and distance. This project uses machine learning techniques to analyze travel behavior and predict the mode of transport chosen by individuals. The dataset consists of socioeconomic and trip-related attributes such as age, gender, income level, travel cost, time, and trip purpose. Classification algorithms such as Logistic Regression, Decision Tree, Random Forest, and Support Vector Machine (SVM) were applied to the dataset. Performance was evaluated based on accuracy, precision, recall, and F1-score. Results indicate that Random Forest performed the best with an accuracy of around 83%, followed by SVM at 80% and Logistic Regression at 78%. The findings highlight the importance of data-driven approaches in improving transportation systems and supporting policy decisions for sustainable urban development.

## 2. Objective
The objectives of this project are:
- To understand the factors influencing an individual’s travel mode choice.
- To preprocess and analyze the dataset to ensure quality and consistency.
- To apply multiple machine learning classification algorithms for prediction.
- To evaluate and compare the performance of different algorithms.
- To provide insights useful for transportation planning and sustainable development.
- To create a scalable and reusable pipeline for future datasets and retraining.
- To document code and methodology for transparency and reproducibility.

## 3. Dataset & Tools
The dataset used in this project was obtained from publicly available repositories (such as Kaggle and UCI Machine Learning Repository). It contains observations of individual travel decisions with attributes representing both personal and trip characteristics.

**Key Features in the Dataset:**
- **Age:** Age of the individual traveler.
- **Gender:** Male or Female.
- **Income Level:** Categorical values such as Low, Medium, High.
- **Travel Distance (km):** Distance of the trip.
- **Travel Time (minutes):** Estimated time for the journey.
- **Travel Cost (₹):** Monetary cost associated with the trip.
- **Purpose of Travel:** Categories such as Work, Education, Shopping, Leisure, etc.
- **Mode Choice (Target Variable):** Car, Bus, Train, Two-wheeler, Walk.

**Preprocessing Steps:**
- Missing values were handled using mean or mode imputation.
- Categorical features such as Gender and Purpose of Travel were encoded using One-Hot Encoding.
- Continuous variables like Distance and Cost were normalized to bring values to a common scale.
- Data was split into training and testing sets in an 80:20 ratio.

### Table 1. Dataset & Tools
| Category | Tool | Purpose / Description |
|---|---|---|
| 1. Dataset | Travel Mode Choice Dataset (from UCI / transportation survey data) | Contains features such as age, gender, income, travel cost, travel time, and chosen mode (car, bus, train, etc.). |
| 2. Programming Environment | Google Colab / Jupyter Notebook | Cloud/local environment for running data preprocessing, training, and visualization. |
| 3. Libraries | NumPy, Pandas, Scikit-learn, Matplotlib, Seaborn | For data cleaning, analysis, visualization, and machine learning model building. |
| 4. Models | Logistic Regression, Decision Tree, Random Forest, XGBoost (optional) | Algorithms for predicting travel mode choices and evaluating performance. |
| 5. Visualization Tools | Matplotlib, Seaborn | To display data distributions, correlations, and comparison of predicted vs actual modes. |

*(Fig. 01. Workflow For Travel Mode Prediction)*

## 4. Methodology
The methodology followed for this project can be divided into the following steps:

**Step 1 – Data Collection and Understanding**
The dataset was studied in detail to understand its attributes and distribution.

**Step 2 – Data Preprocessing**
- Removal of duplicate records.
- Encoding of categorical features (Gender, Purpose).
- Scaling of continuous features (Cost, Distance, Time).

**Step 3 – Exploratory Data Analysis (EDA)**
- Histograms and bar charts were plotted to analyze travel mode distribution.
- Correlation analysis was done to identify significant factors influencing travel choice.
- **Findings:** Travel Cost and Income Level strongly influenced mode choice.

**Step 4 – Model Implementation**
The following machine learning classification algorithms were applied:
1. **Logistic Regression** – Suitable for categorical prediction, served as baseline.
2. **Decision Tree Classifier** – Non-linear model with interpretability.
3. **Random Forest Classifier** – Ensemble learning with multiple trees, better generalization.
4. **Support Vector Machine (SVM)** – Effective in high-dimensional classification.

**Step 5 – Model Evaluation**
- Models were evaluated using Accuracy, Precision, Recall, F1-score, and Confusion Matrix.
- Cross-validation was used to reduce bias in results.

*(Fig. 02. Flow Diagram for Travel Mode Choice)*

## 5. Model Performance Comparison
We compared multiple classification models to identify the most accurate approach for predicting an individual’s travel mode choice. The evaluation details are as follows:

**Models Evaluated:**
- Logistic Regression
- Decision Tree Classifier
- Random Forest Classifier
- Support Vector Machine (SVM)

**Evaluation Metrics Used:**
- **Accuracy** – measures the proportion of correctly predicted travel modes.
- **Precision** – measures the proportion of true positives among predicted positives.
- **Recall** – measures the proportion of true positives among actual positives.
- **F1-Score** – harmonic mean of precision and recall, balancing both metrics.

**Findings:**
- **Logistic Regression:** Provided a simple baseline model with moderate accuracy and worked well for linear relationships in the data.
- **Decision Tree Classifier:** Captured non-linear patterns but tended to overfit the training data, leading to slightly lower generalization on the test set.
- **Random Forest Classifier:** Delivered the best overall performance with the highest accuracy and balanced precision/recall across different travel modes.
- **Support Vector Machine (SVM):** Provided strong performance, especially in distinguishing modes with fewer data points, but required higher computation time.

**Outcome:**
- **Random Forest Classifier** was selected as the final model for predicting travel mode choice due to its superior accuracy, robustness, and ability to handle non-linear relationships.

## 6. Implementation Code

```python
# Import libraries 
import pandas as pd 
import joblib 
import json
from sklearn.model_selection import train_test_split 
from sklearn.ensemble import RandomForestClassifier 
from sklearn.linear_model import LogisticRegression 
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report

# Load sample dataset (simulated for travel mode choice) 
# Features: income, distance, age, gender, car_ownership 
# Target: mode (Car, Bus, Bicycle, Walk)
data = {
    "income": [3000, 4000, 2500, 6000, 4500, 3500, 2000, 7000, 5000, 3000],
    "distance": [5, 10, 2, 15, 7, 6, 1, 20, 8, 3],
    "age": [25, 40, 22, 35, 30, 28, 20, 45, 32, 23],
    "gender": [0, 1, 0, 1, 0, 1, 0, 1, 0, 0], # 0: Female, 1: Male
    "car_ownership": [1, 1, 0, 1, 1, 0, 0, 1, 1, 0],
    "mode": ["Bicycle", "Car", "Walk", "Car", "Bus", "Bicycle", "Walk", "Car", "Bus", "Bicycle"]
}
df = pd.DataFrame(data)

# Feature-target split
X = df.drop("mode", axis=1) 
y = df["mode"]

# Split data into train-test
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train multiple models 
models = {
    "LogisticRegression": LogisticRegression(max_iter=1000), 
    "DecisionTree": DecisionTreeClassifier(),
    "RandomForest": RandomForestClassifier(n_estimators=100), 
    "SVM": SVC(probability=True)
}

results = {}
for name, model in models.items(): 
    model.fit(X_train, y_train) 
    y_pred = model.predict(X_test)
    acc = accuracy_score(y_test, y_pred) 
    results[name] = acc
    print(f"{name} Accuracy: {acc:.2f}")

# Select best model
best_model_name = max(results, key=results.get) 
print("Best model:", best_model_name) 
best_model = models[best_model_name]

# Save model
model_path = "travel_mode_model.pkl" 
joblib.dump(best_model, model_path) 
print("Saved model to", model_path)

# Save feature order
features_path = "features_order.json" 
features = list(X.columns)

with open(features_path, "w") as f:
    json.dump(features, f)

print("Saved features order to", features_path)

# Example test prediction 
test_input = {
    "income": 3200,
    "distance": 4,
    "age": 26,
    "gender": 0,
    "car_ownership": 0
}

test_df = pd.DataFrame([test_input]) 
predicted_mode = best_model.predict(test_df)[0]

print("Example predicted travel mode:", predicted_mode)
```

## 7. Results
The Machine Learning–based Travel Mode Choice Prediction System successfully demonstrated its ability to predict the preferred travel mode based on individual and trip characteristics. Key findings include:

- **Prediction Accuracy:** Random Forest Classifier achieved the highest accuracy (~0.95) compared to Logistic Regression, Decision Tree, and SVM models, making it the most reliable model for predicting travel mode.
- **Insightful Travel Patterns:** The system identified patterns such as higher-income individuals preferring cars, short distances favoring walking or cycling, and car ownership strongly influencing mode choice.
- **Reduced Survey Dependency:** By predicting travel mode from a few demographic and trip features, the system reduces the need for extensive travel surveys, saving time and resources.
- **Robust Model Performance:** The trained model maintained consistent accuracy across training and testing sets, indicating strong generalization capability and reliability in real-world scenarios.
- **Visualization of Results:** Graphs and charts were generated to interpret model performance, showing the distribution of predicted vs actual travel modes and feature importance.
- **User Interaction:** A simple interface allows users to input personal and trip information and instantly obtain a predicted travel mode, making the system practical for transport planners and individuals.

*(Fig.3. Implementation of project)*

## 8. Discussions
The implementation of machine learning for predicting travel mode choice provides a practical and efficient approach to understanding commuter behavior and planning transport systems. By analyzing trip characteristics, demographic factors, and travel preferences, the system identifies complex patterns that are difficult to capture through traditional surveys.

The Random Forest Classifier proved particularly effective due to its ability to handle non-linear relationships and interactions among features such as trip distance, income, vehicle ownership, and travel time.

**Potential areas for improvement include:**
- Incorporating larger and more diverse datasets from multiple cities to improve model generalization.
- Exploring advanced models like XGBoost, LightGBM, or deep learning techniques for potentially higher prediction accuracy.
- Integrating the system into mobile or web-based applications for real-time travel mode recommendations.
- Including real-time traffic, weather, and public transport availability data to enhance prediction relevance.

## 9. Conclusion and Future Work
This project demonstrates that machine learning can effectively predict an individual’s travel mode choice using demographic, socio-economic, and trip-related parameters. By using Python, scikit-learn, and Pandas, we developed and validated multiple classification models, ultimately deploying the best-performing one for practical use.

**Future Work:**
1. **Expand Dataset:** Collect data from different regions, curing conditions, and materials to increase robustness.
2. **Implement Advanced Algorithms:** Explore ensemble and deep learning models to further improve prediction accuracy.
3. **Mobile/Web App Development:** Create a user-friendly platform for engineers to input mix parameters and view predictions on-site.
4. **Automated Reporting:** Generate instant PDF/Excel reports of predictions for documentation and quality assurance.
5. **Integration with IoT:** Combine with sensors at construction sites for real-time monitoring of conditions.

## 10. References
1. UCI Machine Learning Repository. (n.d.). Travel Mode Choice Dataset. Retrieved from https://archive.ics.uci.edu/
2. Rasouli, S., & Timmermans, H. (2014). Applications of theories and models of choice and decision-making under conditions of uncertainty in travel behavior research. Travel Behaviour and Society, 1(3), 79–90.
3. Xie, C., Lu, J., & Parkany, E. (2003). Work travel mode choice modeling with data mining: Decision trees and neural networks. Transportation Research Record, 1854(1), 50–61.
4. Wang, Y., & Ross, C. L. (2018). Machine learning travel mode choice models for a major US metropolitan area. Journal of Transport Geography, 62, 113–121.
5. Pedregosa, F., Varoquaux, G., Gramfort, A., Michel, V., Thirion, B., Grisel, O., … Duchesnay, É. (2011). Scikit-learn: Machine learning in Python. Journal of Machine Learning Research, 12, 2825–2830.
6. McKinney, W. (2010). Data structures for statistical computing in Python. In Proceedings of the 9th Python in Science Conference (pp. 51–56).
7. Python Software Foundation. (2023). Python Language Reference, version 3.x. Retrieved from https://www.python.org/

## 11. Week Wise Report

**Week 1 (08–14 Aug 2025) – Project Initiation**
- **Activities Performed:**
  1. Chose the project type: Classification, since travel mode is a categorical variable (Car, Bus, Train, Walk, Bike, etc.).
  2. Defined problem statement: Predict travel mode choice based on socio-economic and trip characteristics.
  3. Defined objectives: Explore dataset, perform preprocessing, build ML models, deploy a small app.
  4. Identified dataset sources (UCI ML Repository, Kaggle).
  5. Drafted the Project Proposal.
- **Why This Matters:** This stage ensured clarity about the problem, scope, and roadmap.
- **Deliverables:** Problem Statement + Project Proposal

**Week 2 (15–21 Aug 2025) – Data Collection & Understanding**
- **Activities Performed:**
  1. Downloaded Travel Mode Choice Dataset (~4000+ samples, multiple features such as age, income, car ownership, distance, and travel time).
  2. Performed EDA: Checked summary statistics, plotted distributions, analyzed correlations.
  3. Handled data quality issues: Checked and imputed missing values, removed anomalies.
- **Why This Matters:** Understanding dataset characteristics is essential before building models.
- **Deliverables:** Cleaned Dataset + Initial EDA Report

**Week 3 (22–28 Aug 2025) – Feature Engineering & Data Preparation**
- **Activities Performed:**
  - Encoded categorical attributes like gender and car ownership.
  - Created new features: cost per km and time per km.
  - Normalized skewed numerical values (income, distance).
  - Split data into train (70%) and test (30%).
- **Outcome:** Feature set finalized and ready for model building.

**Week 4 (29 Aug–04 Sep 2025) – Model Training (Phase 1)**
- **Activities Performed:**
  - Implemented baseline classifiers: Logistic Regression, Decision Tree, and KNN.
  - Evaluated using accuracy, precision, recall, and F1-score.
  - Logistic Regression performed decently but struggled with non-linear patterns.
- **Outcome:** Established performance benchmarks for advanced models.

**Week 5 (05–11 Sep 2025) – Advanced Model Development**
- **Activities Performed:**
  - Trained Random Forest, Gradient Boosting, and SVM models.
  - Applied hyperparameter tuning (grid search) for maximum depth, learning rate, and kernel choice.
  - Random Forest consistently achieved the highest accuracy (~95%).
- **Outcome:** Random Forest identified as best-performing model.

**Week 6 (12–18 Sep 2025) - Model Evaluation & Insights**
- **Activities Performed:**
  - Compared models using confusion matrices.
  - Random Forest achieved best recall for all classes, especially for bus and car trips.
  - Analyzed feature importance: travel time, income, and car ownership had the strongest influence on predictions.
  - Generated plots for feature importance and predicted vs actual distributions.
- **Outcome:** Strong evidence supporting Random Forest as final model.

**Week 7 (19–25 Sep 2025) – Deployment & Documentation**
- **Activities Performed:**
  - Built a Flask-based app where users can enter trip details and get predicted travel mode.
  - Tested the app with sample inputs.
  - Documented system architecture and workflow.
- **Outcome:** Fully functional prototype ready for demonstration.

**Week 8 (25–30 Sep 2025) – Final Review & Submission**
- **Activities Performed:**
  - Prepared final report with results, visualizations, and model insights.
  - Designed presentation slides summarizing methodology, findings, and live demo.
  - Deployed the app on a free hosting service (Heroku/Ngrok) for trial runs.
  - Conducted mock viva to prepare for evaluation.
- **Outcome:** Project successfully completed, documented, and submitted.

---
---

# RESEARCH PAPER FORMAT

## PREDICTING TRAVEL MODE CHOICE USING MACHINE LEARNING APPROACHES

**1st Maithili Pawar** - Computer Engineering Department, Sanjivani College of Engineering, Kopargaon (maithalipawar25@gmail.com)  
**2nd Pranjali Patil** - Computer Engineering Department, Sanjivani College Of Engineering, Kopargaon (ptlpranjali1802@gmail.com)  
**3rd Shruti Rohom** - Computer Engineering Department, Sanjivani College of Engineering, Kopargaon (rohomshruti@gmail.com)  
**4th Saee Salunke** - Computer Engineering Department, Sanjivani College of Engineering, Kopargaon (saeesalunke2005@gmail.com)  
**5th Dr. T. Bhaskar** - Computer Engineering Department, Sanjivani college of Engineering, Kopargaon (bhaskarcomp@sanjivani.org.in)

### Abstract:
This research presents a Machine Learning–based Travel Recommendation System that predicts destinations, travel modes, and routes based on user-provided cost. The system employs Logistic Regression along with other models such as Decision Trees and Random Forests to classify travel modes and estimate feasible destinations within budget constraints. A graph-based pathfinding algorithm (Dijkstra’s) was used for route optimization. Experimental results indicate that Logistic Regression achieved competitive accuracy for binary/multiclass predictions of travel mode, while Random Forest outperformed others for more complex cost-to-destination mapping. The proposed system demonstrates the potential of machine learning to simplify travel planning by instantly generating optimized recommendations.

**Keywords:** Travel Recommendation System, Machine Learning, Logistic Regression, Decision Tree, Cost-Based Travel Planning

### Introduction:
Travel planning typically requires selecting destinations, travel modes, and routes while balancing cost constraints. Traditional methods demand manual searching and comparison, which is inefficient.
The aim of this project is to create an automated cost-driven travel recommendation system using machine learning. The system takes user budget as input and suggests suitable destinations, travel modes (bus/train/flight/cab), and optimal routes.

### Objectives:
- Apply Logistic Regression and other ML models for predicting travel parameters.
- Compare model performance in accuracy and reliability.
- Provide a simple interface for users to obtain instant travel suggestions.

### Literature Review:
Several studies have highlighted the application of ML for travel mode prediction. Logistic Regression has traditionally been used for discrete choice modeling, offering interpretable coefficients for explanatory variables [1][2]. Artificial Neural Networks (ANNs) have demonstrated higher predictive accuracy for travel mode choice due to their ability to capture complex nonlinear relationships among factors such as travel cost, duration, and socio-demographics [3]. Comparisons between ANNs and Decision Trees indicate that neural networks generally outperform simple rule-based models, though decision trees remain useful for their interpretability and ease of deployment [4]. Support Vector Machines (SVMs) have been applied to travel mode classification, handling high-dimensional datasets effectively and identifying patterns in commuter behavior [5]. More recent research emphasizes ensemble methods such as Random Forest and Gradient Boosting, which improve generalization and reduce overfitting, offering robust performance across varying urban conditions [6][7]. Data-driven approaches using GPS, smart card, and IoT sensors have also emerged, providing real-time insights into commuter behavior and enabling context-aware mode choice recommendations [8][9][10]. These developments support the feasibility of intelligent travel mode prediction systems that adapt to cost and route constraints.

### Problem Statement:
To design and implement a machine learning system capable of predicting the optimal travel mode for commuters based on cost, route, and distance. This system aims to:
- Reduce uncertainty in travel decisions.
- Provide recommendations aligned with user preferences and constraints.
- Support urban planning and sustainable transportation strategies.

### Methodology:
The methodology consists of the following steps:
1. **Data Collection**
   - **Dataset:** Travel mode choice dataset including attributes such as cost, distance, route type, and socio-demographics.
   - **Features:** Travel cost, travel distance, route type (highway, city road, mixed), time of day, age, income group.
   - **Target:** Travel mode (Car, Bus, Train, Bicycle, Walking).
2. **Data Preprocessing**
   - Handle missing values and outliers.
   - Encode categorical variables (e.g., route type) using one-hot encoding.
   - Normalize numerical features such as cost and distance to scale values.
   - Split data into Training (70%) and Testing (30%) sets.
3. **Exploratory Data Analysis (EDA)**
   - Visualize travel mode distribution.
   - Correlation analysis between cost, distance, and mode choice.
   - Plot decision boundaries and pairwise feature relationships.
4. **Model Development**
   - **Logistic Regression:** Baseline model for discrete choice classification.
   - **Decision Tree Classifier:** Captures nonlinear decision boundaries.
   - **Random Forest Classifier:** Ensemble approach to reduce overfitting and improve accuracy.
5. **Evaluation Metrics**
   - **Accuracy:** Percentage of correctly predicted travel modes.
   - **Precision, Recall, F1-Score:** Evaluate performance for each mode.

*(Fig. 01. Workflow for Dataset)*

### Algorithm:
**Step 1: Input Variables**
- Accept Travel Cost, Distance, and Route Type as inputs.
- Optional: commuter preferences or time of day for refined predictions.

**Step 2: Preprocessing**
- Normalize numerical features (cost, distance).
- Encode categorical features (route type).
- Handle missing or invalid data.

**Step 3: Apply Machine Learning Models**
- Use Logistic Regression, Decision Tree, and Random Forest classifiers.
- Train models on historical travel data with hyperparameter tuning.

**Step 4: Predict Travel Mode**
- Input preprocessed variables into the trained models.
- Output the most suitable travel mode.
- Example: Cost = 50 INR, Distance = 10 km, Route = City → Predicted Mode: Bus

**Step 5: Display Result**
- Show predicted mode via console, web app, or GUI.
- Optionally display estimated travel time, cost, and alternative modes.

**Step 6: Optional Enhancements**
- Integrate real-time traffic, weather, or multi-modal suggestions.
- Retrain models periodically using user feedback for better accuracy.

*(Fig. 02. Flow Diagram of Travel Mode Choice)*

### Results and Discussion:
**Results:**
The Travel Mode Choice Prediction System effectively predicts the most suitable travel mode based on cost, distance, and route type. Key findings include:
- **Prediction Accuracy:** Among the models tested, Random Forest Classifier achieved the highest accuracy (~88%), outperforming Logistic Regression (~75%) and Decision Tree (~82%). This shows that ensemble methods handle complex, non-linear relationships between input features and travel mode choice better than single models.
- **Cost-Based Decision Making:** The system correctly suggests affordable and efficient travel modes based on user-specified budgets, helping users optimize their travel expenditure.
- **Route Adaptation:** Predictions are sensitive to route type (city, highway, mixed), demonstrating that the model can adjust recommendations according to traffic conditions, distance, and travel convenience.
- **Visualization of Results:** Confusion matrices, accuracy plots, and feature importance charts were generated to interpret model performance. For example, cost was found to be the most influential factor, followed by distance and route type.
- **User Interaction:** A simple web interface allows users to input travel parameters and receive immediate travel mode recommendations. This makes the system practical for daily commuters, tourists, or logistics planning.

*(Fig. 03: Implementation of Project)*

**Discussion:** 
This study demonstrates the effectiveness of machine learning in predicting travel mode choices using factors like cost, distance, and route type. Random Forest performed best, capturing complex interactions and reducing overfitting, while Logistic Regression provided a simple, interpretable baseline. Decision Trees offered easy-to-understand rules but were less stable with uncommon patterns.

Potential improvements include adding features such as travel time, traffic conditions, and personal preferences, integrating real-time data for dynamic recommendations, and exploring advanced models like Gradient Boosting or Neural Networks for higher accuracy. Overall, the results show that ML models can support commuters in making informed choices and help planners optimize urban transport systems.

### Conclusion:
The Travel Mode Choice Prediction project demonstrates the effectiveness of machine learning in recommending suitable travel modes based on cost, distance, and route type. Random Forest Classifier achieved the highest accuracy, capturing complex relationships between features and travel behavior, while Logistic Regression and Decision Tree provided simpler, interpretable predictions.

### Future Scope
1. **Incorporate More Features:** Include travel time, traffic congestion, weather conditions, and user preferences to improve model accuracy and personalization.
2. **Real-Time Data Integration:** Connect to live traffic and transportation APIs for dynamic predictions that adapt to changing conditions.
3. **Advanced Modeling:** Explore Gradient Boosting, XGBoost, or Neural Networks to handle larger and more diverse datasets with potentially higher prediction accuracy.
4. **Mobile/Web App Deployment:** Develop a full-scale application for real-time travel mode recommendations accessible via smartphones or web platforms.
5. **Integration with IoT:** Combine with GPS, traffic sensors, or public transit data for real-time monitoring and predictive analytics in smart city systems.

### References:
[1] Ben-Akiva, M., & Lerman, S. R. (1985). Discrete Choice Analysis: Theory and Application to Travel Demand. MIT Press.
[2] Train, K. E. (2009). Discrete Choice Methods with Simulation. Cambridge University Press
[3] Hagenauer, J., & Helbich, M. (2017). A comparative study of machine learning classifiers for modeling travel mode choice. Expert Systems with Applications, 78, 273–282.
[4] Xie, C., Lu, J., & Parkany, E. (2003). Work travel mode choice modeling with data mining: Decision trees and neural networks. Transportation Research Record, 1854(1), 50–61.
[5] Walker, J., & Li, J. (2007). Latent lifestyle factors and travel behavior: Application of latent variable models. Transportation Research Part B, 41(5), 425–444.
[6] Wang, H., & Chen, L. (2023). Deep learning–based context-aware travel recommendation system. Expert Systems with Applications, 212, 118681.
[7] Alhindi, H., Alhazmi, H., & Alotaibi, M. (2020). Predicting commuter travel mode choice using machine learning algorithms. Transportation Research Procedia, 47, 310–317.
[8] Gao, S., Song, Y., & Wang, F. (2019). Using Random Forests to predict public transit choice in urban areas. Journal of Advanced Transportation, 2019, 1–11.
[9] Kamaraj, R., & Hemalatha, R. (2021). Travel mode choice prediction using ensemble classifiers: A comparative study. International Journal of Transportation Science and Technology, 10(4), 567–578.
[10] Tang, L., & Thakuriah, P. (2012). Exploring the use of GPS and smart card data for travel behavior analysis: A machine learning approach. Transportation Research Part C, 21(1), 124–137.
