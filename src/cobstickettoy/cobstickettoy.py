import pandas as pd
import typer


def aj_count(keyword: str , asorde : bool ):
    
    df = pd.read_csv("data/AJ.csv")
    df['name']=df['name'].astype(str).str.strip()
    fdf = df[df['name'].str.contains(keyword,case=False,na=False)]
    sdf = fdf.sort_values(by="average_sale_price", ascending=asorde).reset_index(drop=True)
    return sdf

def print_aj_count(keyword: str, asorde : bool ):

    sdf = aj_count(keyword, asorde)
    print(sdf.to_string(index=False))

def entry_point():
    typer.run(print_aj_count)
