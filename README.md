
# RFID Attendance System with LINE Notification

This Python script serves as an RFID attendance system integrated with LINE notification. It allows you to monitor attendance using RFID cards/tags and sends notification messages via LINE Notify. The script is designed to run on a Raspberry Pi.

## Prerequisites

-   Raspberry Pi
-   MFRC522 RFID Reader
-   Python 3.x
-   RPi.GPIO library
-   mfrc522 library
-   line_notify library

## Installation

1.  Connect the MFRC522 RFID Reader to your Raspberry Pi.
2.  Install the required libraries:
    
    Copy code
    
    `pip install RPi.GPIO
    pip install mfrc522
    pip install line_notify` 
    
3.  Replace `"Your Token"` with your LINE Notify token obtained from the LINE Notify website.

## Usage

1.  Run the script on your Raspberry Pi.
2.  Hold an RFID card/tag near the RFID reader.
3.  The script will read the card/tag and send a notification message to your LINE account with attendance details.

## Configuration

-   `start_work_time`: The start time of the workday.
-   `end_work_time`: The end time of the workday.

## Notification Messages

The script sends different notification messages based on the current time:

-   Early arrival message if the time is before the work start time.
-   On-time arrival message if the time is within the first few hours of work.
-   Late arrival message if the time is after the grace period.
-   On-time departure message if the time is within working hours.
-   Leaving message if the time is after work hours.

## Notes

-   Ensure proper wiring and setup of the RFID reader and Raspberry Pi GPIO pins.
-   Customize the notification messages or conditions based on your requirements.
-   Ensure that your Raspberry Pi has internet connectivity to send LINE notifications.

## License

This project is licensed under the MIT License - see the LICENSE file for details.
