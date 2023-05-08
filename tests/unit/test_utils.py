import pandas as pd
import pytest

from utils.utils import transform_pv_plant, pivot_to_daily_normalized_production_curves


@pytest.fixture
def plant_df():
 return pd.DataFrame(
  [
   {'DATE_TIME': '15-05-2020 10:00',
    'PLANT_ID': 4135001,
    'SOURCE_KEY': '1BY6WEcLGh8j5v7',
    'DC_POWER': 6008.375,
    'AC_POWER': 588.775,
    'DAILY_YIELD': 1161.25,
    'TOTAL_YIELD': 6260720.25},
   {'DATE_TIME': '15-05-2020 10:15',
    'PLANT_ID': 4135001,
    'SOURCE_KEY': '1BY6WEcLGh8j5v7',
    'DC_POWER': 6637.285714,
    'AC_POWER': 650.0285713999999,
    'DAILY_YIELD': 1307.5714289999999,
    'TOTAL_YIELD': 6260866.571},
   {'DATE_TIME': '15-05-2020 10:30',
    'PLANT_ID': 4135001,
    'SOURCE_KEY': '1BY6WEcLGh8j5v7',
    'DC_POWER': 4399.75,
    'AC_POWER': 431.875,
    'DAILY_YIELD': 1440.0,
    'TOTAL_YIELD': 6260999.0},
   {'DATE_TIME': '15-05-2020 10:45',
    'PLANT_ID': 4135001,
    'SOURCE_KEY': '1BY6WEcLGh8j5v7',
    'DC_POWER': 4360.571429,
    'AC_POWER': 428.22857139999996,
    'DAILY_YIELD': 1549.0,
    'TOTAL_YIELD': 6261108.0},
   {'DATE_TIME': '15-05-2020 11:00',
    'PLANT_ID': 4135001,
    'SOURCE_KEY': '1BY6WEcLGh8j5v7',
    'DC_POWER': 6829.5,
    'AC_POWER': 668.725,
    'DAILY_YIELD': 1693.0,
    'TOTAL_YIELD': 6261252.0},
   {'DATE_TIME': '15-05-2020 11:15',
    'PLANT_ID': 4135001,
    'SOURCE_KEY': '1BY6WEcLGh8j5v7',
    'DC_POWER': 5969.0,
    'AC_POWER': 584.7857142999999,
    'DAILY_YIELD': 1843.714286,
    'TOTAL_YIELD': 6261402.714},
   {'DATE_TIME': '15-05-2020 11:30',
    'PLANT_ID': 4135001,
    'SOURCE_KEY': '1BY6WEcLGh8j5v7',
    'DC_POWER': 6226.125,
    'AC_POWER': 609.8625,
    'DAILY_YIELD': 1994.5,
    'TOTAL_YIELD': 6261553.5},
   {'DATE_TIME': '15-05-2020 11:45',
    'PLANT_ID': 4135001,
    'SOURCE_KEY': '1BY6WEcLGh8j5v7',
    'DC_POWER': 9420.285714,
    'AC_POWER': 920.0428571,
    'DAILY_YIELD': 2155.0,
    'TOTAL_YIELD': 6261714.0},
  ]
 )

@pytest.fixture
def transformed_plant_df():
 df = pd.DataFrame(
  [{'date_time': '2020-05-15 10:00',
    'plant_id': 4135001,
    'ac_power': 588.775,
    'year': 2020,
    'month': 5,
    'day': 15,
    'hour': 10,
    'min': 0,
    'day_of_year': 136,
    'inverter': 'inverter_1',
    'inverter_production_of_day': 'inverter_1_day_136',
    'ac_power_normalized': 0.639943015106747},
   {'date_time': '2020-05-15 10:15',
    'plant_id': 4135001,
    'ac_power': 650.0285713999999,
    'year': 2020,
    'month': 5,
    'day': 15,
    'hour': 10,
    'min': 15,
    'day_of_year': 136,
    'inverter': 'inverter_1',
    'inverter_production_of_day': 'inverter_1_day_136',
    'ac_power_normalized': 0.7065198826160203},
   {'date_time': '2020-05-15 10:30',
    'plant_id': 4135001,
    'ac_power': 431.875,
    'year': 2020,
    'month': 5,
    'day': 15,
    'hour': 10,
    'min': 30,
    'day_of_year': 136,
    'inverter': 'inverter_1',
    'inverter_production_of_day': 'inverter_1_day_136',
    'ac_power_normalized': 0.4694074810398308},
   {'date_time': '2020-05-15 10:45',
    'plant_id': 4135001,
    'ac_power': 428.22857139999996,
    'year': 2020,
    'month': 5,
    'day': 15,
    'hour': 10,
    'min': 45,
    'day_of_year': 136,
    'inverter': 'inverter_1',
    'inverter_production_of_day': 'inverter_1_day_136',
    'ac_power_normalized': 0.465444156318748},
   {'date_time': '2020-05-15 11:00',
    'plant_id': 4135001,
    'ac_power': 668.725,
    'year': 2020,
    'month': 5,
    'day': 15,
    'hour': 11,
    'min': 0,
    'day_of_year': 136,
    'inverter': 'inverter_1',
    'inverter_production_of_day': 'inverter_1_day_136',
    'ac_power_normalized': 0.7268411409744969},
   {'date_time': '2020-05-15 11:15',
    'plant_id': 4135001,
    'ac_power': 584.7857142999999,
    'year': 2020,
    'month': 5,
    'day': 15,
    'hour': 11,
    'min': 15,
    'day_of_year': 136,
    'inverter': 'inverter_1',
    'inverter_production_of_day': 'inverter_1_day_136',
    'ac_power_normalized': 0.6356070369844078},
   {'date_time': '2020-05-15 11:30',
    'plant_id': 4135001,
    'ac_power': 609.8625,
    'year': 2020,
    'month': 5,
    'day': 15,
    'hour': 11,
    'min': 30,
    'day_of_year': 136,
    'inverter': 'inverter_1',
    'inverter_production_of_day': 'inverter_1_day_136',
    'ac_power_normalized': 0.6628631430521651},
   {'date_time': '2020-05-15 11:45',
    'plant_id': 4135001,
    'ac_power': 920.0428571,
    'year': 2020,
    'month': 5,
    'day': 15,
    'hour': 11,
    'min': 45,
    'day_of_year': 136,
    'inverter': 'inverter_1',
    'inverter_production_of_day': 'inverter_1_day_136',
    'ac_power_normalized': 1.0}]
 )
 df['inverter'] = df['inverter'].astype('category')
 return df


def test_transform_pv_plant(plant_df, transformed_plant_df):
    actual_df = transform_pv_plant(plant_df, date_format="%d-%m-%Y %H:%M")
    pd.testing.assert_frame_equal(actual_df, transformed_plant_df)


def test_pivot_to_daily_normalized_production_curves(transformed_plant_df):
    actual_df = pivot_to_daily_normalized_production_curves(transformed_plant_df)
    expected_df = pd.DataFrame(
     [{'hour': 10, 'min': 0, 'inverter_1_day_136': 0.639943015106747},
      {'hour': 10, 'min': 15, 'inverter_1_day_136': 0.7065198826160203},
      {'hour': 10, 'min': 30, 'inverter_1_day_136': 0.4694074810398308},
      {'hour': 10, 'min': 45, 'inverter_1_day_136': 0.465444156318748},
      {'hour': 11, 'min': 0, 'inverter_1_day_136': 0.7268411409744969},
      {'hour': 11, 'min': 15, 'inverter_1_day_136': 0.6356070369844078},
      {'hour': 11, 'min': 30, 'inverter_1_day_136': 0.6628631430521651},
      {'hour': 11, 'min': 45, 'inverter_1_day_136': 1.0}]
    )
    pd.testing.assert_frame_equal(actual_df, expected_df, check_names=False)

