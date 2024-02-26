import serial
import rospy
from std_msgs.msg import Float64

def parse_gpgll(gpgll_data):
    print(f"Raw NMEA Sentence: {gpgll_data}")
    fields = gpgll_data.split(',')
    if len(fields) >= 6 and fields[0] == '$GPGLL' and fields[1] and fields[3]:
        latitude = float(fields[1]) / 100
        longitude = float(fields[3]) / 100
        return latitude, longitude

    return None

def main():
    rospy.init_node('gps_publisher')
    latitude_pub = rospy.Publisher('latitude', Float64, queue_size=10)
    longitude_pub = rospy.Publisher('longitude', Float64, queue_size=10)
    ser = serial.Serial('/dev/ttyACM0', 9600)

    try:
        while not rospy.is_shutdown():
            # Read a line from the serial port
            line = ser.readline().decode('utf-8', errors='replace').strip()
            if line.startswith('$GPGLL'):
                result = parse_gpgll(line)
                if result:
                    latitude_pub.publish(result[0])
                    longitude_pub.publish(result[1])

    except KeyboardInterrupt:
        ser.close()

if __name__ == "__main__":
    main()
