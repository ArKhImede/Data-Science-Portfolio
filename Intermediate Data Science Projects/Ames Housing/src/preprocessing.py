from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer

def create_preprocessor(num_features, cat_features) -> ColumnTransformer:
    
    preprocessor = ColumnTransformer( transformers=[
        ("num", StandardScaler(), num_features),
        ("cat", OneHotEncoder(handle_unknown="ignore"), cat_features)
    ])
    
    return preprocessor