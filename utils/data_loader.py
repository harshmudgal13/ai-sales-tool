import pandas as pd

def load_data(file):

    # -------------------------------------------------
    # ✅ FORCE CORRECT HEADER READING
    # -------------------------------------------------
    try:
        df = pd.read_csv(
            file,
            encoding="utf-8",
            engine="python"
        )
    except:
        df = pd.read_csv(
            file,
            encoding="latin1",
            engine="python"
        )

    # -------------------------------------------------
    # 🧠 CLEAN COLUMN NAMES
    # -------------------------------------------------
    df.columns = df.columns.astype(str).str.strip()

    # -------------------------------------------------
    # 🧠 REMOVE COMPLETELY EMPTY ROWS
    # -------------------------------------------------
    df = df.dropna(how="all")

    # -------------------------------------------------
    # 🧠 RESET INDEX (CRITICAL FOR STREAMLIT)
    # -------------------------------------------------
    df = df.reset_index(drop=True)

    return df