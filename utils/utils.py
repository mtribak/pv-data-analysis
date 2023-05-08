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
        {inverters_list[inverter]: "inverter_" + str(inverter + 1) for inverter in range(len(inverters_list))})

    plant_df['inverter_production_of_day'] = plant_df['inverter'].astype(str) + "_day_" + plant_df[
        'day_of_year'].astype(str)

    plant_df['max_ac_power'] = plant_df.groupby('inverter')["ac_power"].transform('max')
    plant_df['ac_power_normalized'] = plant_df['ac_power'] / plant_df['max_ac_power']

    plant_df = plant_df.drop(['source_key', "total_yield", "dc_power", "daily_yield", "max_ac_power"], axis=1)
    return plant_df


def pivot_to_daily_normalized_production_curves(plant_df: pd.DataFrame) -> pd.DataFrame:
    mask = (plant_df['hour'] >= 5) & (plant_df['hour'] <= 18)

    pivot_plant_df = plant_df.loc[
        mask, ['hour', "min", "inverter_production_of_day", "ac_power_normalized"]].pivot(
        index=["hour", "min", ], columns=["inverter_production_of_day"], values="ac_power_normalized").reset_index()

    return pivot_plant_df


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


def plot_cluster_curves(daily_curves_df: pd.DataFrame, clustering_result_df: pd.DataFrame, cluster: int = -1):
    clustering_inverters = list(
        clustering_result_df[clustering_result_df['clustering_labels'] == cluster]['days_names'])
    clustering_inverters.append("time")
    fig = px.line(daily_curves_df, x="time", y=clustering_inverters, range_y=[-0.1, 1])
    fig.show()


def plot_cluster_analysis(clustering_result_df: pd.DataFrame,
                          plant_daily_curves_df: pd.DataFrame,
                          day: str,
                          cluster: int) -> None:
    print(f"Inverters in the cluster {cluster} for {day}")
    clustering_inverters = list(
        clustering_result_df[clustering_result_df['clustering_labels'] == cluster]['days_names'])
    clustering_inverters.append("time")
    fig = px.line(plant_daily_curves_df, x="time", y=clustering_inverters, range_y=[-0.1, 1])
    fig.show()
    print("====================================================")
    print(f"Inverters not in the cluster {cluster} for {day}")
    day_inverters = list(clustering_result_df[clustering_result_df['day'] == day]['days_names'])
    day_inverters.append("time")
    inverters_not_in_cluster = list(set(clustering_inverters) ^ set(day_inverters))
    fig = px.line(plant_daily_curves_df, x="time", y=inverters_not_in_cluster, range_y=[-0.1, 1])
    fig.show()
    print("====================================================")
    print(clustering_result_df[clustering_result_df['days_names'].isin(inverters_not_in_cluster)])
