def apply_filters(df, col, vals):

    if col and vals:
        df = df[df[col].isin(vals)]

    return df
