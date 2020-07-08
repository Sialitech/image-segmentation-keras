import os

# Empty for no info, INFO for wood event, area and sensor distance. Debug for FPS
DEBUG = "INFO"
LOG_PATH = "/share/mainlog.txt"
# Select the working daytime of the modelo 
INIT_HOUR = 6
INIT_MIN = 0
LAST_HOUR = 22
LAST_MIN = 0
########################COMUNICATIONS##########################################
path = os.path.dirname(os.path.realpath(__file__))
KEY = "1dnE5ELo0AP-LTxrL-Qs5ceUPXxLe7GHouCFj-in4gNI"
SCOPE = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive',
         'https://www.googleapis.com/auth/spreadsheets']
CREDENTIALS = path + '/credentials.json'  # Google spreadsheet credentials
WORKSHEET_POS = 0  # page number of the spreadsheet
HOST = '192.111.111.111'  # RPi IP 
SENSOR_PORT = 4000
CAMERA_PORT = 4500
MOTOR_PORT = 6000

EMAIL_ADDRESS = "pythonsender12@gmail.com"
EMAIL_PASSWORD = "njwvdwkvffhsrelg"
###############################################################################


###############################################################################
VIDEO = ""  # "/home/varona/test.mp4"  # Inferenced video. If empty, uses raspi camera
HHD_PATH = ""  # "/home/varona/"  # "/media/varona/Jaled"  # save camvideo here
DETECTION_PATH = "/share"
VIDEO_LEN = 600  # we don't want save 16 hours videos. Video leght in secods 
DISPLAY = False  # If true, imshow of camera and inference
SCALE = 2  # video tunning frame size display
TRESHOLD_AREA = {"x_min": 100, "x_max": 250, "y_min": 150, "y_max": 800}
CLASS_COLORS = [(0, 0, 0), (255, 255, 255), (0, 0, 0), (0, 0, 0)]
FILTER = True  # enable opencv contour filtering to remove small blobs
FILTER_SIZE = 15
FILTER_TIME = 4
MIN_AREA = 5000
MIN_LENGTH = 400
CHECKPOINTS_PATH = "../volume_simple/"  # model weigths path
###############################################################################


###############################################################################
PIX_RELATION = 425/490  # 127/1273  # Pixel size vs real mm size mm/pix
WOOD_HEIGHT = 38  # mm
# Interpolation fix the relation between sensor distance measurement and saw
# distance, or motor real position between good pixel location. We take
# data for multiple points and use a rule of three.
INTERPOLATE = True
REAL_SENSOR_POINTS = [80, 100, 120, 140, 160, 180, 200]
SENSOR_POINTS = [33.1, 30.9, 29.1, 26.9, 25.6, 23.2, 21.9]
REAL_MOTOR_POINTS = [0, 65, 130, 195]
MOTOR_POINTS = [320, 420, 520, 620]
###############################################################################
