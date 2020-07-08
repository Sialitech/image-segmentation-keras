import cv2
import socket
import time
import numpy as np
import json
from .keras_segmentation.predict import model_from_checkpoint_path, predict


class Unet:
    def __init__(self, socket, weights_path, colors, sender_socket):
        self.model = model_from_checkpoint_path(weights_path)
        self.socket = socket
        self.class_colors = list(colors)
        self.sender_socket = sender_socket
        self.inference()

    def inference(self):
        while True:
            frame_read = self.socket.recv()
            npimg = np.frombuffer(frame_read, dtype=np.uint8)
            frame = cv2.imdecode(npimg, 1)
            start_time = time.time()
            prediction = predict(model=self.model, inp=frame, colors=self.class_colors)
            fps = 1/(time.time() - start_time)
            print("FPS: {}".format(fps))
            res = json.dumps(prediction.tolist())
            self.sender_socket.send_string(res)
