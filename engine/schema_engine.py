import pandas as pd

# 🧠 AUTO DATA STRUCTURE DETECTOR
def detect_schema(df):

    schema = {
        "metrics": [],
        "categories": [],
        "dates": []
    }

    # Detect numeric metrics
    for col in df.select_dtypes(include="number").columns:
        schema["metrics"].append(col)

    # Detect category columns
    for col in df.select_dtypes(include="object").columns:
        if df[col].nunique() < 50:
            schema["categories"].append(col)

    # Detect date columns
    for col in df.columns:
        if "date" in col.lower():
            schema["dates"].append(col)

    return schema
