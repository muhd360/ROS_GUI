# ROS_GUI
This is an onboarding of how to setup for a gui which you can use to integrate an user interface in your robotics project
![Screenshot from 2024-02-16 07-30-59](https://github.com/muhd360/ROS_GUI/assets/125988314/7b59e3fb-d594-4340-8800-676e61aef1ca)

![Screenshot from 2024-02-16 07-27-01](https://github.com/muhd360/ROS_GUI/assets/125988314/d46601da-7388-4867-b5fb-e60ffbd8b95c)
![Screenshot from 2024-02-16 07-35-10](https://github.com/muhd360/ROS_GUI/assets/125988314/397a1517-e64a-4a27-8ba8-9891f46c166c)
![Screenshot from 2024-02-16 07-32-43](https://github.com/muhd360/ROS_GUI/assets/125988314/6e60d3e6-1fd7-478e-9013-7fa17f46dbc9)
img.png 
![img](https://github.com/muhd360/ROS_GUI/assets/125988314/709f1963-5ef1-4f65-adca-41940b12bde5)
The following are the components of the gui:-
1)you can access the terminal Directly from the gui
2)anurag.py will run on your onboard computer we have used esp32 to send the data.It is necessary to format the data accordingly we established multiple subscribers to extract and indiviually send the data on multiple ros publishers.
3)ensure that data is being published on multiple rostopics you can check by running rostopic_list in your terminal
4)now, you have to run the ros gui files they are as follows 1:-This is your main page here you can access all the subfiles.2:-there are 2 science graphs which receive data from the ros-publisher onboard the buttons are not connected to the publisher they show or disappear the graphs this needs to be fixed 
5)ensure that the rate of publishing is set the rate is in ms so set it accordingly try to create a seprate ui file which you can do from xyz.py import mainwindow connect your pyqt ui to this directly such that changes in this file dont affect the main.
6)there are also gps coordinates that we have received using neo6m gps just simply flash the arduino with no code make the rx and tx connections also gnd and vcc.Now you can use pyserial or rosserial inorder to send data ensure that u parse the strings correctly for this gps_pub.py is a good example for the same ensure that you write two seprate subscribers for lat and long.
7)The last file is the cam feed we had used ip cam so the feed was uploaded directly to a website url try to keep streaming protocol rstp for the same
8)use your own python enviornment-this is a good video for the same(https://www.youtube.com/watch?v=8uxd9RBQvmQ)
the pyqt5 tutorials are a mustwatch for gui setup.
the same thing can be acheived using qt designer in c++(https://www.youtube.com/watch?v=Cg1DaNFnZyY)refer for the same ALL THE BEST AND GODSPEED

