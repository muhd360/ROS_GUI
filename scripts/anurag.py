import serial
import rospy
from std_msgs.msg import Float64

# Define the COM port and baudrate for your Arduino
arduino_port = 'COMX'  # Change this to your Arduino's COM port
baudrate = 9600

# Open the serial connection
ser = serial.Serial(arduino_port, baudrate, timeout=1)

# Initialize ROS node
rospy.init_node('arduino_data_publisher', anonymous=True)

# Define ROS publishers for five distinct topics
dht_temp_pub = rospy.Publisher('dhtt', Float64, queue_size=10)
dht_hum_pub = rospy.Publisher('dhth', Float64, queue_size=10)
mqtt_1_pub= rospy.Publisher('mq1', Float64, queue_size=10)
mqtt_2_pub= rospy.Publisher('mq2', Float64, queue_size=10)
dht2_temp_pub = rospy.Publisher('dht2t', Float64, queue_size=10)
dht2_humidity_pub = rospy.Publisher('dht2h', Float64, queue_size=10)

# Function to process and publish data to ROS topics
def process_and_publish(topic_data):
    # Separate topic and data using "/"
    parts = topic_data.split('/')
    
    if len(parts) == 2:
        # Extracted topic and data
        topic, data = parts
        data.strip()
        # Convert data to float64
        try:
            data_float64 = float(data)
            
            # Publish to ROS topics
            if topic == 'dhtt':
                dht_temp_pub.publish(data_float64)
            elif topic == 'dhth':
                dht_hum_pub.publish(data_float64)
            elif topic == 'mq1':
                mqtt_1_pub.publish(data_float64)
            elif topic == 'mq2':
                mqtt_2_pub.publish(data_float64)
            elif topic == 'dht2t':
                dht2_temp_pub.publish(data_float64)
            elif topic == 'dht2h':
                dht2_humidity_pub.publish(data_float64)
 
        except ValueError:
            print("Invalid data format:", data)

# Read and process data indefinitely
try:
    while not rospy.is_shutdown():
        # Read a line from ArduinoMake sure to replace the 'COMX' with the actual COM port of your Arduino and 
        line = ser.readline().decode('utf-8').strip()
        
        # Process and publish data to ROS topics
        process_and_publish(line)

except KeyboardInterrupt:
    # Close the serial connection on keyboard interrupt
    ser.close()
    print("Serial connection closed.")
