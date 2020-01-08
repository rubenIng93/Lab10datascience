import pandas as pd


def load_data(path):
    df = pd.read_csv(path, usecols=['FL_DATE', 'TAIL_NUM', 'UNIQUE_CARRIER',
                                    'FL_NUM', 'ORIGIN', 'DEST', 'CRS_DEP_TIME',
                                    'DEP_TIME', 'DEP_DELAY', 'CRS_ARR_TIME', 'ARR_TIME',
                                    'ARR_DELAY', 'CARRIER_DELAY', 'WEATHER_DELAY',
                                    'NAS_DELAY', 'SECURITY_DELAY', 'LATE_AIRCRAFT_DELAY'], parse_dates=[0])
    print(df.describe())
    print(df.info())
    print(df.head())

    return df


print('Loading Data...')
df = load_data('831394006_T_ONTIME.csv')


