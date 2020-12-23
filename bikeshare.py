import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

months = ['All','January', 'February', 'March', 'April', 'May', 'June']

def get_filters():
    """asking the user of what city, month , day he want the filter the data by"""

    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    """asking the user to Enter city he want to explore"""
    city = input('what city you want to explor\n 1: chicago \n 2: new york city \n 3: washington\n pleas type the city name shown\n').lower()

    while city not in CITY_DATA.keys():
        print('\n >>>pleas enter valid city name<<<\n')
        city = input('what city you want to explor\n 1: chicago \n 2: new york city \n 3:washington\n pleas type the city name as shown\n').lower()

    print(city)

        # TO DO: get user input for month (all, january, february, ... , june)



    month = input('what month, you can type all for all months data\n please type the month name as shown\n 1: January\n 2: February\n 3: March \n 4: .\n 5: . \n or All for ALL months\n').title()
    while month not in months:
        print('\n >>> you have not enter valid month <<< \n')
        month = input(' you can type All for ALL months data\n please type the month name as shown\n 1: January\n 2: February\n 3: March \n 4: .\n 5: . \n or ALL for all months\n').title()


        # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = ['All','Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday','Sunday']
    day = input( 'if you like to filter data by day pleas type the day name \n 1.Monday \n 2.Tueseday\n 4. .\n 5. . \n OR ALL for all days\n').title()
    while day not in days:
        print('\n >>> invalid day Name <<< \n')
        day = input( 'pleas type the day name \n 1.for Monday \n 2.for tuseday\n 4. .\n 5. . \n OR ALL for all days\n').title()

    print(f'you chose: {city}, filtered by {month} month/months , and {day} as day filter')
    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['Month'] = df['Start Time'].dt.month_name()
    df['Day'] = df['Start Time'].dt.day_name()

    if month != 'All':
        df=df[df['Month'] == month]

    if day != 'All':
        df=df[df['Day'] == day]
    return df


def time_stats(df, city, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()


    # TO DO: display the most common month

    if month == 'All':
         top_month = df['Month'].mode()[0]
         print(f'{top_month}  is the most common month in  {city}')

    # TO DO: display the most common day of week
    if day == 'All':
        top_day = df['Day'].mode()[0]
        print(f'the most common day of the week is: {top_day}')



    # TO DO: display the most common start hour
    df['Hour'] = df['Start Time'].dt.hour
    common_start_hour = df['Hour'].mode()[0]

    print('The Most Common Start Hour is: ',common_start_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    top_strt_station = df['Start Station'].mode()[0]
    print(f'\n most commonly used start station is: {top_strt_station} ')

    # TO DO: display most commonly used end station
    top_end_station = df['End Station'].mode()[0]
    print(f'\n most commonly used end station is: {top_end_station} ')
    print('the number we use end station is: ',(df['End Station'].values ==top_end_station).sum())


    # TO DO: display most frequent combination of start station and end station trip
    df['route'] = 'from ' + df['Start Station'] + ' to ' + df['End Station']
    top_route = df['route'].mode()[0]
    print(f'\n most frequent combination of start station and end station trip\n \n {top_route}')
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    total_travel_time = df['Trip Duration'].sum()
    print(f'\n total travel time is {total_travel_time} seconds \n')


    # TO DO: display mean travel time
    trip_mean = df['Trip Duration'].mean()
    print(f'\n mean travel time: {trip_mean} seconds \n')


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    users_types = df.groupby('User Type').size()
    print(f'\n users types are as fallow: \n {users_types}')


    # TO DO: Display counts of gender
    try:
        gender_count = df['Gender'].value_counts()
        print(f'\n counts of customers gender \n {gender_count}')
    except:
        print("this city don't have gender information")


    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        earliest_BD = int(df['Birth Year'].min())
        print(f'\n our oldest coustomer birth year is: {earliest_BD}')
        recent_BD = int(df['Birth Year'].max())
        print(f'\n our youngest coustomer birth year is: {recent_BD}')
        common_BD = int(df['Birth Year'].mode()[0])
        print(f'\n most common birth year is: {common_BD}')

    except:
        print('\n no birth day data avilible\n')




    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw(df):

    """ask if user want to see roaw data"""
        #take user response
    response = input('\n would you want to see the raw data? Y/N (Y for yes, N for no) \n')
    if response.upper() == 'Y':
        #counter to increment each time user chose Y to display next 10 lines of raw data
        counter = 0

        while True:
            print(df.iloc[counter: counter+10])
            counter += 10
                #see if user want to see more raw data ..
            repeat = input('\n want to contue ?? Y/N \n').upper()
            if repeat != 'Y':
                break



def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df, city, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
