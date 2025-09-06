**🍄 Mushroom Edibility Classification Project**

## 📋 Project Overview
A comprehensive machine learning pipeline to classify mushrooms as edible or poisonous based on their physical characteristics. Achieves **99.8% accuracy** using optimized ensemble methods.

## 🎯 Key Features
- **99.8% Test Accuracy** with Random Forest
- **Automated Preprocessing** (handles missing values, scaling, encoding)
- **Feature Selection** (21 → 13 most important features)
- **Hyperparameter Tuning** for optimal performance
- **Production-ready** pipeline with pickle files

## 📊 Dataset
- **60,000+ samples** with 21 features
- **Physical characteristics**: cap diameter, stem dimensions, odor, gill properties, spore print color, habitat
- **Binary classification**: Edible (0) vs Poisonous (1)

## 🔧 Technical Implementation

### Phase 1: Data Preprocessing
```python
# Automated pipeline handling:
- Missing value imputation (Median/Mode)
- Outlier treatment (Winsorization)
- Feature scaling (RobustScaler)
- Categorical encoding (OneHot/Ordinal)
- Power transformation for skewed features
```

### Phase 2: Model Training & Evaluation
**Algorithms Compared:**
- ✅ Random Forest (Best: 99.8% accuracy)
- ✅ Decision Tree (99.3%)
- ✅ Logistic Regression (77.3%)
- ✅ SVM (77.3%)
- ✅ K-Nearest Neighbors (99.7%)
- ✅ Naive Bayes (67.4%)

### Phase 3: Feature Selection
- **Filter Methods**: ANOVA F-test, Mutual Information
- **Wrapper Methods**: Recursive Feature Elimination
- **Embedded Methods**: Random Forest feature importance
- **Result**: 21 → 13 most predictive features

### Phase 4: Hyperparameter Tuning
- **Bayesian Optimization** for efficient search
- **Grid/Random Search** for different algorithms
- **Cross-validation** with stratified sampling

## 📦 Saved Models
```
models/
├── best_mushroom_model.pkl          # Complete pipeline
├── mushroom_preprocessor.pkl        # Preprocessing steps
├── mushroom_model.pkl               # Random Forest model
└── deployment_package.pkl           # Deployment package dictionary
```

## 🚀 Usage
```python
import pickle

# Load Full Pipeline (preprocessor + model)
with open("best_mushroom_model.pkl", "rb") as f:
    model = pickle.load(f)

# Predict
prediction = model.predict(X)
```

## 📈 Results
| Model | Accuracy | F1-Score | ROC-AUC |
|-------|----------|----------|---------|
| Random Forest | 99.8% | 99.8% | 99.9% |
| K-Nearest Neighbors | 99.7% | 99.7% | 99.8% |
| Decision Tree | 99.3% | 99.3% | 99.3% |

## 💡 Insights
- **Top predictive features**: Odor, gill characteristics, spore print color
- **Tree-based models** outperformed linear models significantly
- **Feature selection** improved model interpretability without sacrificing accuracy
- **Hyper Parameter Tuning** improved overall performance especially for weak learners 

## 🛠️ Technologies
- Python 3.8+
- Scikit-learn
- Imbalanced-learn (SMOTE)
- Pickle
- Matplotlib, Seaborn

---

**Tags**: `machine-learning` `classification` `scikit-learn` `feature-engineering` `model-deployment`

---

**⭐ Star this repo if you found it useful! Contributions welcome.**