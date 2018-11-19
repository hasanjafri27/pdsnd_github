import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york': 'new_york_city.csv',
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
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = ''
    while city.lower() != ['chicago', 'new york', 'washington']:
        city = input("Would you like to see data for Chicago, New York, or Washington?\n")
        if city.lower() == 'chicago':
            city = city.lower()
            break
        elif city.lower() == 'new york':
            city = city.lower()
            break
        elif city.lower() == 'washington':
            city = city.lower()
            break
        else:
            print('Sorry, I do not understand your input. Please input either Chicago, New York, or Washington.')

    filter_choice = ''
    while filter_choice.lower() != ['month', 'day', 'none']:
        filter_choice = input("Would you like to filter the data by month, day, or not at all? Type 'none' for no time filter.\n")
        if filter_choice.lower() == 'month':
            filter_choice = filter_choice.lower()
            break
        elif filter_choice.lower() == 'day':
            filter_choice = filter_choice.lower()
            break
        elif filter_choice.lower() == 'none':
            filter_choice = filter_choice.lower()
            break
        else:
            print('Sorry, I do not understand your input. Please input either month, day or none.')


    # filter by month if applicable
    if filter_choice == 'month':
        day = 'all'
        # get user input for month (all, january, february, ... , june)
        month = ''
        while month.lower != ['january', 'february', 'march', 'april', 'may', 'june']:
            month = input("Which month - January, February, March, April, May, or June?\n")
            if month.lower() == 'all':
                month = month.lower()
                break
            elif month.lower() == 'january':
                month = month.lower()
                break
            elif month.lower() == 'february':
                month = month.lower()
                break
            elif month.lower() == 'march':
                month = month.lower()
                break
            elif month.lower() == 'april':
                month = month.lower()
                break
            elif month.lower() == 'may':
                month = month.lower()
                break
            elif month.lower() == 'june':
                month = month.lower()
                break
            else:
                print('Sorry, I do not understand your input. Please input either January, February, March, April, May, or June.')


    # filter by day of week if applicable
    elif filter_choice == 'day':
        month = 'all'
        # get user input for day of week (all, monday, tuesday, ... sunday)
        day = ''
        while day.lower != ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            day = input("Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday?\n")
            if day.lower() == 'all':
                day = day.lower()
                break
            elif day.lower() == 'monday':
                day = day.lower()
                break
            elif day.lower() == 'tuesday':
                day = day.lower()
                break
            elif day.lower() == 'wednesday':
                day = day.lower()
                break
            elif day.lower() == 'thursday':
                day = day.lower()
                break
            elif day.lower() == 'friday':
                day = day.lower()
                break
            elif day.lower() == 'saturday':
                day = day.lower()
                break
            elif day.lower() == 'sunday':
                day = day.lower()
                break
            else:
                print('Sorry, I do not understand your input. Please input either Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday.')

    elif filter_choice == 'none':
        month = 'all'
        day = 'all'

    print('-'*40)
    return city, month, day, filter_choice


def load_data(city, month, day, filter_choice):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['Start Time'].dt.month == month]


    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['Start Time'].dt.weekday_name == day.title()]


    # filter by day of week if applicable
    if (day == 'all') & (month == 'all'):
        # filter by day of week to create the new dataframes
        df = pd.read_csv(CITY_DATA[city])


    return df


def time_stats(df, filter_choice):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    
    # display the most common month
    # extract month from the Start Time column to create a month column
    if (filter_choice == 'none'):
        df['month'] = df['Start Time'].dt.month
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        common_month = months[df['month'].mode()[0] - 1]
        print("Most common month : ",common_month)
    
    # display the most common day of week
    # extract day of week from the Start Time column to create a day_of_week column
    if (filter_choice == 'none') or (filter_choice == 'month'):
        df['day_of_week'] = df['Start Time'].dt.weekday_name
        common_dow = df['day_of_week'].mode()[0]
        print("Most common day of week : ",common_dow)
    
    # display the most common start hour
    # extract hour from the Start Time column to create an hour column
    df['hour'] = df['Start Time'].dt.hour
    common_hour = df['hour'].mode()[0]
    print("Most common start hour : ",common_hour,"hundred hours")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    common_startstation = df['Start Station'].mode()[0]
    print("Most commonly used start station : ",common_startstation)

    # display most commonly used end station
    common_endstation = df['End Station'].mode()[0]
    print("most commonly used end station : ",common_endstation)

    # display most frequent combination of start station and end station trip
    # Creating 'Trip Combination' column.
    df['Trip Combination'] = df['Start Station'].str.cat(df['End Station'], sep=' to ')
    frequent_combination = df['Trip Combination'].mode().to_string(index = False)
    print("most frequent combination of start station and end station trip : ",frequent_combination)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_traveltime = df['Trip Duration'].sum()
    print("Total travel time : ",total_traveltime,"seconds")
    # display mean travel time
    mean_traveltime = df['Trip Duration'].mean()
    print("Mean travel time : ",mean_traveltime,"seconds")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Count of user types :\n",user_types)

    if (city == 'chicago') or (city == 'new york'):
        # Display counts of gender
        gender_types = df['Gender'].value_counts()
        print("Count of gender types :\n",gender_types)
        # Display earliest, most recent, and most common year of birth
        earliest_yob = int(df['Birth Year'].min())
        print("Earliest year of birth : ",earliest_yob)
        mostrecent_yob = int(df['Birth Year'].max())
        print("Most recent year of birth : ",mostrecent_yob)
        mostcommon_yob = int(df['Birth Year'].mode()[0])
        print("Most common year of birth : ",mostcommon_yob)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def view_data(df):

    def is_valid(display):
        if display.lower() in ['yes', 'no']:
            return True
        else:
            return False
    head = 0
    tail = 5
    valid_input = False
    while valid_input == False:
        display = input('\nWould you like to view individual trip data? '
                        'Type \'yes\' or \'no\'.\n')
        valid_input = is_valid(display)
        if valid_input == True:
            break
        else:
            print("Sorry, I do not understand your input. Please type 'yes' or 'no'.")
    if display.lower() == 'yes':
        print(df[df.columns[0:-1]].iloc[head:tail])
        display_more = ''
        while display_more.lower() != 'no':
            valid_input_2 = False
            while valid_input_2 == False:
                display_more = input('\nWould you like to view more individual trip data? Type \'yes\' or \'no\'.\n')
                valid_input_2 = is_valid(display_more)
                if valid_input_2 == True:
                    break
                else:
                    print("Sorry, I do not understand your input. Please type 'yes' or 'no'.")
            if display_more.lower() == 'yes':
                head += 5
                tail += 5
                print(df[df.columns[0:-1]].iloc[head:tail])
            elif display_more.lower() == 'no':
                break


def main():
    while True:
        city, month, day, filter_choice = get_filters()
        df = load_data(city, month, day, filter_choice)

        time_stats(df, filter_choice)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        view_data(df)

        restart = ''
        while restart.lower() != ['yes', 'no']:
            restart = input('\nWould you like to restart? Enter yes or no.\n')
            if restart.lower() == 'yes':
                break
            elif restart.lower() == 'no':
                exit()
            else:
                print("Sorry, I do not understand your input. Please type 'yes' or 'no'.")


if __name__ == "__main__":
	main()
