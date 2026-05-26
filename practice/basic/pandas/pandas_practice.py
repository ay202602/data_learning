import pandas as pd
from pathlib import Path
"""東海地方の労働人口・就業者数を割合で表示する"""
FILE_PATH = Path(__file__).parent / "FEI_PREF_260525140950.csv"

df = pd.read_csv(FILE_PATH, thousands= ",")
print(df.dtypes)

#都道府県ごとに労働力人口・労働者数（性別）を割合で集計

labor_man = df.groupby("地域")["労働力人口（男）"].sum()
ratio_man = labor_man / labor_man.sum() * 100
print(f"labor_man : {labor_man.dtype}")

labor_woman = df.groupby("地域")["労働力人口（女）"].sum()
ratio_woman = labor_woman / labor_woman.sum() * 100
print(f"labor_woman : {labor_woman.dtype}")

result = pd.DataFrame({
    "労働力人口（男）": labor_man.map("{:,.0f}".format),
    "割合（男）（％）": ratio_man.round(1),
    "労働力人口（女）": labor_woman.map("{:,.0f}".format),
    "割合（女）（％）": ratio_woman.round(1)
})

print(result)
print(f"pandas version  {pd.__version__}")