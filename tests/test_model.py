import pandas as pd
from model import make_pipeline, evaluate_models

def synthetic_data():
    X = pd.DataFrame({'income':[1,2,3,4,5,6,7,8,9,10,11,12], 'account':['a','b']*6})
    y = pd.Series([0,1]*6)
    return X,y

def test_pipeline_handles_unseen_category():
    X,y = synthetic_data()
    model = make_pipeline(X).fit(X,y)
    out = model.predict_proba(pd.DataFrame({'income':[3],'account':['not_seen']}))
    assert out.shape == (1,2)
    assert 0 <= out[0,1] <= 1

def test_evaluation_two_models():
    X,y = synthetic_data()
    scores, details = evaluate_models(X,y)
    assert set(scores['Modelo']) == {'Regressão logística','Random Forest'}
    assert scores['ROC-AUC'].between(0,1).all()
    assert all(d['matrix'].shape == (2,2) for d in details.values())
