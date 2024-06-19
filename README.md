# Intelli-Eye
A criminal facial recognition system that utilize Viola-Jones face detection and LBPH algorithm for facial algorithm to extract facial features

1. The application will require some sample photos of user front face where it can be done by running the Enrol.py file.
2. To run the application , kindly initiate main.py
3. Next kindly create a criminal detail via the icon of 'Criminal Details'. Inside you will input all the relevant information and upload the pictures from step 1.
4. To train the application, click on 'Train AI' so that it can study and analyse the facial features of the photos.
5. To observe the system functionality, kindly click on 'Real-time monitoring' where the application will turn on the computer camera and search for faces. Upon identification of the criminal, it will show importart information such as the Criminal Identification (CID), name and offense. Additionally, a push notification will occur via the application to alert the application user.
6. Upon detection, it will putput into an excel file, 'CriminalLog.xlsx' where it will record information such as the name, offense, time, date and the coordinate via GeoCode library in Python.
