import torch
from matplotlib import pyplot as plt
import numpy as np
import cv2
from time import time


model = torch.hub.load('.', 'custom', path='best_5s.pt', force_reload=True,source='local')

cap = cv2.VideoCapture(2)
while cap.isOpened():
    ret, frame = cap.read()
    
    # Make detections 
    results = model(frame)
    
    cv2.imshow('YOLO', np.squeeze(results.render()))
    
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()