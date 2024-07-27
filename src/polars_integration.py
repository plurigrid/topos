import polars as pl
from typing import List, Dict, Any

def create_sample_dataframe() -> pl.DataFrame:
    data = {
        "A": [1, 2, 3, 4, 5],
        "B": ["a", "b", "c", "d", "e"],
        "C": [1.1, 2.2, 3.3, 4.4, 5.5]
    }
    return pl.DataFrame(data)

def perform_basic_operations(df: pl.DataFrame) -> Dict[str, Any]:
    results = {}
    
    # Basic statistics
    results["mean_A"] = df["A"].mean()
    results["max_C"] = df["C"].max()
    
    # Filtering
    results["filtered_df"] = df.filter(pl.col("A") > 2)
    
    # Grouping and aggregation
    results["grouped_df"] = df.groupby("B").agg(pl.sum("A").alias("sum_A"))
    
    return results

def main():
    print("Creating sample Polars DataFrame:")
    df = create_sample_dataframe()
    print(df)
    
    print("\nPerforming basic operations:")
    results = perform_basic_operations(df)
    
    print(f"Mean of column A: {results['mean_A']}")
    print(f"Max of column C: {results['max_C']}")
    
    print("\nFiltered DataFrame (A > 2):")
    print(results['filtered_df'])
    
    print("\nGrouped DataFrame (sum of A grouped by B):")
    print(results['grouped_df'])

if __name__ == "__main__":
    main()
