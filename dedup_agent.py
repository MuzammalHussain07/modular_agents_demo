import pandas as pd
from fuzzywuzzy import fuzz

def deduplicate_customers(customers: list[dict]):
    df = pd.DataFrame(customers)
    deduped = []
    seen = []

    for _, row in df.iterrows():
        record = row.to_dict()
        if not any(fuzz.ratio(record["email"], s["email"]) > 90 for s in seen):
            seen.append(record)
            deduped.append(record)

    return {
        "original_count": len(customers),
        "deduplicated_count": len(deduped),
        "cleaned_data": deduped
    }
