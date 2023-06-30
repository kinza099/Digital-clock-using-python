# Digital-clock-using-python
This program displays a clock with the current time. Rather than render numeric Characters directly, the sevseg module,"seven Segment Display Module",generates the drawings for each digit.

Let me explain it's code

Import the necessary libraries sys, time, and sevseg. sys is a module that provides access to some variables used or maintained by the interpreter and functions that interact with the interpreter. time is a module that provides various time-related functions. sevseg is a custom module or library that provides functions for generating seven-segment display patterns.
Then  starts a try-except block to handle potential exceptions that may occur during the execution of the program. Inside the block, an infinite loop (while True) is initiated to continuously update and display the digital clock.

Inside the loop:

print('\n' * 60) is used to clear the console output by printing multiple newline characters.
current_time is set to the current local time using time.localtime().
The hour, minutes, and seconds are extracted from current_time and converted to strings for display purposes. The % 12 operation is performed on the hour value to display it in a 12-hour format instead of 24-hour format.
If the hour is '0', it is replaced with '12' to correctly display midnight (12 AM).
These values are stored in hour, minutes, and seconds variables, respectively.

Then sevseg library is used to obtain the seven-segment display patterns for each digit of the hour, minutes, and seconds. The getSevSegStr() function from the sevseg module is called, passing in the digit value and the desired width (2 in this case) as arguments. The return value is a string representation of the seven-segment display patterns for the digit.

These strings are then split into individual lines using the splitlines() method and assigned to variables htop_row, hmiddle_row, hbuttom_row, mtop_row, mmiddle_row, mbuttom_row, stop_row, smiddle_row, sbuttom_row for each digit's display pattern.
AFter that the seven-segment display patterns for the digits of the hour, minutes, and seconds are printed on the console using print() statements. The display patterns are arranged in a formatted manner to mimic a digital clock layout




