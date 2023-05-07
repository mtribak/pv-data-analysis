import pandas as pd
import plotly.express as px


def transform_pv_plant(plant_df: pd.DataFrame, date_format: str) -> pd.DataFrame:
    plant_df.columns = plant_df.columns.str.lower()

    plant_df["date_time"] = pd.to_datetime(plant_df["date_time"], format=date_format)

    plant_df["year"] = plant_df["date_time"].dt.year
    plant_df["month"] = plant_df["date_time"].dt.month
    plant_df["day"] = plant_df["date_time"].dt.day
    plant_df["hour"] = plant_df["date_time"].dt.hour
    plant_df["min"] = plant_df["date_time"].dt.minute
    plant_df["day_of_year"] = plant_df["date_time"].dt.dayofyear
    plant_df["date_time"] = plant_df["date_time"].dt.strftime('%Y-%m-%d %H:%M')

    plant_df['inverter'] = plant_df['source_key'].astype('category')
    inverters_list = list(plant_df['source_key'].unique())
    plant_df['inverter'] = plant_df['inverter'].cat.rename_categories(
        {inverters_list[inverter]: "inverter_" + str(inverter+1) for inverter in range(len(inverters_list))})

    plant_df = plant_df.drop(['source_key', "total_yield", "dc_power", "daily_yield"], axis=1)
    return plant_df


def _quantile25(x):
    return x.quantile(0.25)


def _quantile50(x):
    return x.median()


def _quantile75(x):
    return x.quantile(0.75)


def summarize_inverter_production(plant_df: pd.DataFrame) -> pd.DataFrame:
    return plant_df.groupby("inverter").agg({'date_time': ['min', 'max', 'count'],
                                             'ac_power': ["min", _quantile25, _quantile50, _quantile75, "max", 'mean',
                                                          'std',
                                                          ]}).reset_index()


def plot_boxplots(plant_df: pd.DataFrame) -> None:
    fig = px.box(plant_df, x="inverter", y="ac_power", width=900, height=700)
    fig.show()


def plot_inverter_production_curve(plant_df: pd.DataFrame, inverter_name: str) -> None:
    fig = px.line(plant_df[plant_df['inverter'] == inverter_name], x='date_time', y='ac_power')
    fig.show()
