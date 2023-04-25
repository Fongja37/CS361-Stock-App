Author: Jayden Fong
Date: 2/24/23


Stock Price Reporter:
This program reports the current price of a desired stock using Yahoo Finance API. Users can enter a company symbol for the stock they want to check, such as AAPL for Apple Inc., and the program will return the current price in USD.


Getting Started:
To use this program, follow these steps:

Enter the company symbol for the stock you want to check in the "Company Symbol" text field.
Click the "Show" button to get the current stock price.
The reported price will be displayed in the "Stock Result (USD)" field.
Click "Clear" to erase all content within the text field.
Note: This program may not be able to get the stock price if the stock is not publicly traded or if the Yahoo Finance API is unavailable. If an error occurs, an error message will be printed.


Usage:
To use this program, you will need to install the yahoo_fin module and the tkinter module. You can install them using pip:

pip install yahoo_fin
pip install tkinter


Customization:
Users can modify the colors of the program's widgets to their liking by changing the values of the fg (foreground) and bg (background) parameters in the respective widget's constructor.

For example, to change the color of the "Stock Result (USD)" label to red, modify the following line:
Label(master, text="Stock Result (USD):", justify=LEFT).grid(row=2, sticky=W, padx=5, pady=5)

Similarly, users can modify the colors of other widgets such as buttons, labels, and text fields by changing the respective parameters.
Users can find a list of available color names and their corresponding hexadecimal codes on websites such as https://htmlcolorcodes.com/color-names/.

Note: Changing the colors of widgets is purely a cosmetic change and does not affect the functionality of the program.