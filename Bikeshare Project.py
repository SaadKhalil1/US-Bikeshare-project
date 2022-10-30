import time
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
    # get user input for city (chicago, new york city, washington).
    while True :
        try:
            city = input('enter city : ').lower()
            if city in ['chicago','new york city','washington'] :
                break
            else : 
                print('invalid city')
        except : 
            print('try again')
            
    # get user input for month (all, january, february, ... , june)
    while True :
        try:
            month = input('enter month : ').lower()
            if month in ['all','january', 'february', 'march', 'april', 'may', 'june'] :
                  break
            else : 
                print('invalid month')
        except : 
            print('try again')

    # get user input for day of week (all, monday, tuesday, ... sunday)
            
    while True :
        try:
            day = input('enter day : ').lower()
            if day in ['all','sunday', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday' ] :
                break
            else : 
                print('invalid day')
        except : 
            print('try again')

 

    print('-'*40)
    return city, month, day

def load_data(city, month, day):
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]
    return df




def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    df['Start Time'] =pd.to_datetime(df['Start Time'])
    # display the most common month
    most_common_month = df['month'].mode()[0]
    print('most common month : ',most_common_month)

    # display the most common day of week
    df['day']=df['Start Time'].dt.day_name()
    most_common_day=df['day'].mode()[0]
    print('most common day of week : ',most_common_day)

    # display the most common start hour
    df['hour']=df['Start Time'].dt.hour
    most_common_hour = df['hour'].mode()[0]
    print('most common start hour : ',most_common_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()
    
    # display most commonly used start station
    most_common_STstation=df['Start Station'].mode()[0]
    print('most commonly used start station : ',most_common_STstation)

    # display most commonly used end station
    most_common_ENDstation=df['End Station'].mode()[0]
    print('most commonly used end station : ',most_common_ENDstation)

    # display most frequent combination of start station and end station trip
    Start_station=df['Start Station']
    End_station=df['End Station']
    most_frequent_combination=pd.concat([Start_station,End_station])
     
    print('most frequent combination of start station and end station trip : ',most_frequent_combination.mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_travel_time=df['Trip Duration'].sum()
    print('total travel time : ',total_travel_time,'minutes')

    # display mean travel time
    mean_travel_time=df['Trip Duration'].mean()
    print('mean travel time : ',mean_travel_time,'minutes')

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print('counts of user types : \n',user_types)

    # Display counts of gender
    
    try :
        gender = df['Gender'].value_counts()
        print('counts of gender : \n',gender)

    # Display earliest, most recent, and most common year of birth
        Earliest_year =df['Birth Year'].min()
        most_recent_year =df['Birth Year'].max()
        most_common_year= df['Birth Year'].mode()[0]
        print('Earliest year of birth : ',Earliest_year)
        print('Most recent year of birth : ' , most_recent_year)
        print('Most common year of birth',most_common_year)
    except :    
        print('no available data')
        
        
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
            
def display_data(df):
    view_data = input('\nWould you like to view 5 rows of individual trip data? Enter yes or no\n') 
    start_loc = 0
    
    while view_data == 'yes':
        print(df.iloc[start_loc:start_loc+5])
        start_loc += 5
        view_data = input("Do you wish to continue?: ").lower()


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()






