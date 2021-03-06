# Exchange App 

## Contents

* [Introduction](#Introduction)
* [Design](#Design)
* [Risk Assessment](#Risk-Assessment)
* [Agile Development](#Agile-Development)
* [Testing](#Testing)

## Introduction
This project emulates the basics of an exchange, allowing users to create their user profile and purchase Bitcoin or 
Ethereum at a given rate, with 10 GBP given at account creation. Users can then allocate a portion of their GBP 
balance to either cryptocurreny and also sell their holdings. The price of the coins fluctuate. After the user is
finished with their account, they can delete it and make another one if they choose.

## Design
The following database was designed to provide the functionality required for the exchange to carry out the basic orders of buying and selling assets.

![ERD](https://github.com/GurjinderB/exchange-app/blob/main/figures/project1erd.png)

The future goal of this application would be to retrieve real-time data for each of the cryptocurrencies on offer and to provide a mechanism to transfer holdings to
other users.

## Risk Assessment

| Risk | Impact | Mitigation |
|------|--------|--------------------|
| Broken vesion gets deployed | High | Use a version control system such as github |
|Cross site request forgery | Low | Set a secret key |





## Agile Development
![Kanban board](https://github.com/GurjinderB/exchange-app/blob/main/figures/Kanbanbord.png)
## Testing

## Additional Features
Future releases could include:
* Including a date and time field in the transaction history so that users can track their transactions according to date and time too.
* Add the ability to transfer cryptocurrency balance to other users, which are added to a friends list for example.
* Display realtime data for the cryptocurrencies available to exchange users.
* Add password functionality for users.
* Create an admin account where more other cryptocurrencies can be added through form functionality.

## App
![Application Home](https://github.com/GurjinderB/exchange-app/blob/main/figures/home.png)

The price of Bitcoin and Ethereum changes based on the current price and a random number chosen from a normall distribution of mean 0 and standard deviation of 0.05.

![Create Account](https://github.com/GurjinderB/exchange-app/blob/main/figures/create-account.png)
![Trade](https://github.com/GurjinderB/exchange-app/blob/main/figures/trade.png)

The when navigating to the Buy/Sell tab, the price of Bitcoin and Ethereum is the same as the home page.
