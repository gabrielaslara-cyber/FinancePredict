"""Educational credit-risk classification; never use for lending decisions."""
from functools import lru_cache
import pandas as pd
from sklearn.datasets import fetch_openml
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, average_precision_score, balanced_accuracy_score, confusion_matrix

@lru_cache(maxsize=1)
def load_data():
    """Downloads OpenML credit-g dataset (German Credit), 1000 records."""
    d = fetch_openml(name="credit-g", version=1, as_frame=True)
    X = d.data.copy()
    y = (d.target.astype(str) == 'bad').astype(int)
    return X, y

def make_pipeline(X, method="Regressão logística"):
    categorical = X.select_dtypes(include=["object", "category", "string"]).columns.tolist()
    numerical = X.select_dtypes(exclude=["object", "category", "string"]).columns.tolist()
    pre = ColumnTransformer([
        ('num', Pipeline([('impute', SimpleImputer(strategy='median')), ('scale', StandardScaler())]), numerical),
        ('cat', Pipeline([('impute', SimpleImputer(strategy='most_frequent')), ('encode', OneHotEncoder(handle_unknown='ignore'))]), categorical),
    ])
    model = LogisticRegression(max_iter=2000, class_weight='balanced', random_state=42) if method == 'Regressão logística' else RandomForestClassifier(n_estimators=200, min_samples_leaf=3, class_weight='balanced', random_state=42, n_jobs=-1)
    return Pipeline([('prep', pre), ('model', model)])

def evaluate_models(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=.25, stratify=y, random_state=42)
    rows, models = [], {}
    for name in ('Regressão logística', 'Random Forest'):
        pipe = make_pipeline(X_train, name).fit(X_train, y_train)
        scores = pipe.predict_proba(X_test)[:, 1]
        pred = (scores >= 0.5).astype(int)
        rows.append({'Modelo':name,'ROC-AUC':roc_auc_score(y_test, scores),'PR-AUC':average_precision_score(y_test,scores),'Acurácia balanceada':balanced_accuracy_score(y_test,pred)})
        models[name] = {'pipeline':pipe,'matrix':confusion_matrix(y_test,pred),'test_size':len(y_test)}
    return pd.DataFrame(rows), models
