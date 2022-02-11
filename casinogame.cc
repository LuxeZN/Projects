#include <iostream>
#include <iomanip>
#include <cstdlib>
#include <string>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{

    //Variable Declaration
    double user_balance, user_bet;
    int user_guess, winning_number;
    char play_again;

    cout << "Welcome to the Casino Game" << endl;

        do
        {
            cout << "Enter how much money you would like to deposit $";
            cin >> user_balance;
            if (user_balance < 0)
            {
                cout << "Invalid amount, please try again" << endl;
            }
        } while (user_balance < 0);

        cout << "Your balance is: $" << user_balance << endl;

    do
    {
        //Loop to define bet amount

        do
        {
            cout << "Enter amount you would like to bet: $";
            cin >> user_bet;
            if ((user_bet < 0) || (user_bet > user_balance))
            {
                cout << "Invalid bet amount, please try again" << endl;
            }
        } while ((user_bet < 0) || (user_bet > user_balance));

        cout << "Your bet amount is $" << user_bet << endl;

        //Loop to define number guessed

        do
        {

            cout << "Enter the number you would like to bet on (0-9): ";
            cin >> user_guess;
            if ((user_guess < 0) || (user_guess > 9))
            {
                cout << "Invalid guess, please try again" << endl;
            }

        } while ((user_guess < 0) || (user_guess > 9));

        //Generates the winning number with random function

        winning_number = rand() % 10;

        //Statements to decide if user is a winner/loser and updating balance based on win or loss

        if (user_guess == winning_number)
        {
            user_balance += (user_bet * 10);
            cout << "Congratulations, you won!" << endl;
            cout << "Your new balance total is: $" << user_balance << endl;
        }
        else
        {
            user_balance -= user_bet;
            cout << "Sorry, you lost." << endl;
            cout << "Your new balance total is: $" << user_balance << endl;
        }

        cout << "Would you like to play again? (y/n) ";
        cin >> play_again;

    } while ((play_again == 'y') && (user_balance > 0));

    cout << "You decided not to play again, or you need to deposit more money!" << endl;

}