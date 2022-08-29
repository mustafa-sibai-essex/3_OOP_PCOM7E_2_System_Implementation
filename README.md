Overview:
This project contains my system implmentation of my previously design UML diagrams. This driverless car project uses no libraries or dependecy. The entire application can inteacted with by using the terminal.

Usage:
Run the app.py script to start the application. Then, read the terminal and press the appropriate number on the keyboard to go to a system or start a function.

Order of execution and systems:
This application starts by first diagnosing the entire vehicle systems to ensure all systems function correctly. Once that is done, the infotainment system begins its execution. The entire vehicle can be controlled directly from the infotainment system. 

This application contains many systems that will aid the user in using the driverless car. Some of these systems are

Diagnostics system:
    Scans and ensures all hardware in the vehicle is operational.

Telecommunication:
    Allow the user to connect to the Satellite, GPS, Internet, and Cloud Server. This module also contains the SMS and Email manager, which allow the user to send, receive and manage SMSes and Emails from within the infotainment module. One important note to remember is that the user will not be able to send or receive any SMSes or Emails if they are not connected to the Satellite. Similarly, the user will not be able to send any GPS coordinates without being connected to the GPS satellite. In addition to everything mentioned previously, this module contains a phone and phone book systems that allow the user to call any contact in their contact list, add, delete, update and remove any contacts within the phone book. Keep in mind calls cannot be made if the vehicle is not connected to the Satellite.

Drivetrain:
    This module allows the user to control the vehicle engine, brakes, and steering from within the infotainment system.

Autopilot:
    This module is responsible for setting the vehicle in autonomous mode, which allows the vehicle to drive itself and capture with the help of the camera system multiple pictures, which are then analyzed in the Object Detection system to identify dangerous objects on the road and avoid them. The autopilot will not turn on if the engines are off.

Security:
    This module is responsible for vehicle security, like locking and unlocking all entrances, alerting the driver in case of a breakin, and recording the vehicle surroundings at all times.

Design patterns and data structures:
Many different data structures have been used in this project. 

To start off, the stack data structure has been used to allow the user to navigate seamlessly in the terminal from one system to another. Any time the user makes an input, a so-called Page is pushed to the stack. Each page contains the necessary information displayed to the user to interact with the system. Once the user press 0 to go back to the previous page, the stack is popped, and the previous page is rendered.

Another data structure used in this project on many occasions is the list. The list is used in many places, one of which is the phone book. The phone book contains a list of contacts that can be displayed on the terminal. The user is allowed to add, remove, and update contacts in the list. Additionally, the list data structure is used in both the SMS and Email manager classes. Each of these contains a list of SMSes and emails.

Finally, queues and dictionaries are used in the object detection system to help analyze images captured by vehicle cameras to identify objects on the road.
