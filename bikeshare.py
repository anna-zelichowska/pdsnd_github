import time
import datetime
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Ask User for City input

    city = input("For which city (Chicago, New York City, Washington) would you like to display the data? ").lower()

    while city not in ["chicago", "new york city", "washington"]:
        print("Oooops! There is no data to display for your input")
        city = input("For which city (Chicago, New York City, Washington) would you like to display the data? ").lower()

    # Ask User for Month input

    month = input("For which month would you like to display the data (all, January, February, March, April, May, June)? ").lower()

    while month not in ["january", "february", "march", "april", "may", "june", "all"]:
        print("Oooops! There is no data to display for your input")
        month = input("For which month would you like to display the data (all, January, February, March, April, May, June)? ").lower()

    # Ask User for Day input
    day = input("For which day of the week would you like to display the data (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)? ").lower()

    while month not in ["january", "february", "march", "april", "may", "june", "all"]:
        print("Oooops! There is no data to display for your input")
        day = input("For which day of the week would you like to display the data (all, Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday)? ").lower()

    print('-'*40)
    return city, month, day


# Loads the data based on the filters set in get_filters()

def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """

    # Load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # Convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Extract month and day of week from Start Time to new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name

    # Filter by month if applicable
    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # Filter by day of week if applicable
    if day != 'all':

        # Filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df

def display_raw_data(df):
    """
    Displays 5 rows of the loaded data upon User's request.

    Args:
        df - Pandas Data Frame for the selected city, month and day

    Returns:
        None
    """
    row = 0
    raw_data = input("Would you like to display the raw data? Enter yes or no: ").lower()

    while raw_data not in ['yes', 'no']:
        raw_data = input("Invalid input!\nWould you like to display the raw data? Enter yes or no: ").lower()

    # Display first 5 rows if User selected yes
    if raw_data == "yes":
        print(df.head())

    # Display the next 5 rows if User selected yes
    while raw_data == 'yes':
        raw_data = input("Would you like to display the next 5 rows of data? Enter yes or no: ").lower()
        row += 5
        if raw_data == 'yes':
            print(df[row:row+5])
        elif raw_data != 'yes':
            break

def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.

    Args:
        df - Pandas Data Frame for the selected city, month and day

    Returns:
        None
    """

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # Displays the most popular month
    popular_month = df['month'].mode()[0]
    print('The most common month: ', popular_month)

    # Displays the most popular day of week
    popular_day_of_week = df['day_of_week'].mode()[0]
    print('The most common day of week: ', popular_day_of_week)

    # Extracts the hour from Start Time to a new column
    df['hour'] = df['Start Time'].dt.hour

    # Displays the most popular hour
    popular_hour = df['hour'].mode()[0]
    print('The most common hour: ', popular_hour)

    # Time used for calculations
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """
    Displays statistics on the most popular stations and trip.

    Args:
        df - Pandas Data Frame for the selected city, month and day

    Returns:
        None
    """

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # Displays the most popular Start Station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most common start station: ', popular_start_station)

    # Displays the most popular End Station
    popular_end_station = df['End Station'].mode()[0]
    print('The most common hour: ', popular_end_station)

    # Displays the most popular combo of Start and End Station
    df['Start_End'] = 'From ' + df['Start Station'].map(str) + ' to ' + df['End Station'].map(str)
    popular_trip = df['Start_End'].mode()[0]
    print("The most popular trip: ", popular_trip)

    # Time used for calculations
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.

    Args:
        df - Pandas Data Frame for the selected city, month and day

    Returns:
        None
    """

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # Displays total travel time in [days, hours:minutes:seconds] format
    total_travel_time = df['Trip Duration'].sum()

    print("Total travel time: ", str(datetime.timedelta(seconds=int(total_travel_time))))

    # Displays average travel time in [days, hours:minutes:seconds] format
    mean_travel_time = df['Trip Duration'].mean()
    print("Average travel time: ", str(datetime.timedelta(seconds=int(mean_travel_time))))

    # Time used for calculations
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """
    Displays statistics on bikeshare users.

    Args:
        df - Pandas Data Frame for the selected city, month and day

    Returns:
        None
    """

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Counts Users by the Type
    type_count = df['User Type'].value_counts()
    print("User type count:\n", type_count)

    # Counts Users by Gender if Gender column available
    try:
        gender_count = df['Gender'].value_counts()
        print("\nUser gender count:\n", gender_count)
    except KeyError:
        print("\nUser gender data not available!")

    # Displays earliest birth year, most recent birth year and most frequent birth year if Birth Year column available
    try:
        earliest_year = df['Birth Year'].min()
        print("\nEarliest User birth year: ", int(earliest_year))

        most_recent_year = df['Birth Year'].max()
        print("\nMost recent User birth year: ", int(most_recent_year))

        most_common_year = df['Birth Year'].mode()[0]
        print("\nMost common User birth year: ", int(most_common_year))

    except KeyError:
        print("\nUser birth year data not available!")

    # Time used for calculations
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

# Runs all previous functions
def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        display_raw_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
