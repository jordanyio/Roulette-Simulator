import random
import csv
import pandas as pd
import matplotlib.pyplot as plt

while True:

    plt.figure(figsize=(10, 6))

    black_numbers = [2, 4, 6, 8, 10, 11, 13, 15, 17, 20, 22, 24, 26, 28, 29, 31, 33, 35]

    random_numbers = []
    color_list = []
    one_six_list = []
    money_list = []

    # Starting values and bet ( can bet on red or black, and a column 1-6 as-is... ) 
    # Modify the code to handle different bets below the draw  
    # EG: If num == 15: money *= 36 else money -= starting_bet || if num >= 1 and num <= 18: money *= 2 else money -= starting_bet 
    money = 5000
    starting_bet = 10
    sixToOne = starting_bet * 6
    var1 = 'black'        #random.choice(['red', 'black'])
    var2 = 'four'        # random.choice(['one', 'two', 'three', 'four', 'five', 'six'])

    with open('roulette.csv', mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['results', 'black/red', 'oneSix', 'money'])

        # Spin the wheel      
        for i in range(5000):
            num = random.randint(0, 36)
            random_numbers.append(num)

            # Realize the color/number
            if num == 0:
                color_list.append("green")
            elif num in black_numbers:
                color_list.append("black")
            else:
                color_list.append("red")

            # determine which column the ball landed in
            if num >= 1 and num <= 6:
                one_six_list.append("one")
            elif num >= 7 and num <= 12:
                one_six_list.append("two")
            elif num >= 13 and num <= 18:
                one_six_list.append("three")
            elif num >= 19 and num <= 24:
                one_six_list.append("four") 
            elif num >= 25 and num <= 30:
                one_six_list.append("five")
            elif num >= 31 and num <= 36:
                one_six_list.append("six")
            else:
                one_six_list.append("zero")

            # Calculate the change in money 
            if i > 0:
                prev_color = color_list[i-1]
                prev_one_six = one_six_list[i-1]
                if prev_color == var1:
                    money += starting_bet
                else:
                    money -= starting_bet

                if prev_one_six == var2:
                    money += sixToOne
                else:
                    money -= starting_bet

            # Add the current money value to the list
            money_list.append(money)

            # Write the row to the CSV file
            writer.writerow([random_numbers[i], color_list[i], one_six_list[i], money_list[i]])

        print("Random numbers, colors, oneSix categories, and money values written to CSV file")


    # Read the CSV file
    df = pd.read_csv('roulette.csv')
    df['MA13'] = df['money'].rolling(500).mean()

    #df.iloc[0, df.columns.get_loc('money')] = None
    #df['money'] = df['money'].shift(-1)
    # Plot the line chart
    plt.plot(df['money'])

    # Add axis labels and title
    plt.xlabel('Number of Spins')
    plt.ylabel('Money')
    plt.title('Roulette Simulation, bankroll:500, betPerSpin:2')
    plt.grid(True)
    plt.plot(df['MA13'])

    # Show the plot
    plt.show()
    # ^ deactivate the line above and activate the two lines below to rapidly simulate spins  
    #plt.draw()
    #plt.pause(2) # Display plot for 5 seconds
