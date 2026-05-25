import pandas as pd
from pathlib import Path
"""東海地方の労働人口・就業者数を割合で表示する"""

FILE_PATH = Path(__file__).parent / "FEI_PREF_260525140950.csv"

df = pd.read_csv(FILE_PATH, thousands=",")
print(df.head())
print(f"\n{df.dtypes}")

#都道府県ごとに労働力人口・労働者数（性別）を割合で集計

grouped = df.groupby("地域")["労働力人口（男）"].sum()
ratio = grouped / grouped.sum() * 100

result = pd.DataFrame({
    "労働力人口（男）": grouped,
    "割合（％）": ratio.round(2)
})

print(result)