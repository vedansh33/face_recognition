from facenet_pytorch import MTCNN

import venv  # import all the files of the folder so that we can make object from those classes
import os
import torch
from torchvision import models
import torch.nn as nn

import torchvision
from facenet_pytorch import MTCNN
import cv2
import numpy as np
import torch
from PIL import Image
from torchvision import transforms

####################  INITIATE CLASSIFIER  #########################
# Need to give the same modification to the same classifier
model=torchvision.models.mobilenet_v2(pretrained=True)
classifier = nn.Sequential(nn.Linear(1000,256),nn.ReLU(),nn.Dropout(0.25),nn.Linear(256,2),nn.Sigmoid())
model.fc = classifier

model.load_state_dict(torch.load("E:/face recognizer/model_Inc.pth",map_location=torch.device('cpu')))

trans = transforms.Compose([transforms.ToPILImage(),
                            transforms.Resize((64, 64)),  # Same transformations as on training data
                            transforms.ToTensor(),
                            transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
                                         ])
device = torch.device("cuda:0" if torch.cuda.is_available() else "cpu")
print(f"Running on device {device}")

labels = ["Not Vedansh", "Vedansh"]
labelColor = [(10, 255, 0), (10, 0, 255)]

cap = cv2.VideoCapture(0)

# MTCNN for detecting the presence of faces
mtcnn = MTCNN(keep_all=True, device=device)

#model.to(device)
model.eval()

while True:
    ret, frame = cap.read()

    if ret == False:
        pass

    img_ = frame.copy()
    boxes, probs, landmarks = mtcnn.detect(img_, landmarks=True)  # We saved box coordinates in boxes and left the landmarks
    try:
        for i in range(len(boxes)):
            x1, y1, x2, y2 = boxes[i]
            x1, y1 = max(x1,0), max(y1, 0)
            frame = cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 255), 2)
            for ld in landmarks:
                cv2.circle(frame, tuple(ld[0]), 2, (0, 0, 255), -1)
                cv2.circle(frame, tuple(ld[1]), 2, (0, 0, 255), -1)
                cv2.circle(frame, tuple(ld[2]), 2, (0, 0, 255), -1)
                cv2.circle(frame, tuple(ld[3]), 2, (0, 0, 255), -1)
                cv2.circle(frame, tuple(ld[4]), 2, (0, 0, 255), -1)
            face = img_[int(y1-30):int(y2+30), int(x1-30):int(x2+30)]

            in_img = trans(face)

            in_img = in_img.unsqueeze(0)
            #in_img = in_img.to(device)

            out = model(in_img)
            # pr = out.detach().cpu().numpy()
            # if out == 1:
            #     print("yes")
            # else:
            #     print("no")
            prob = torch.exp(out)
            a = list(prob.squeeze())
            predicted = a.index(max(a))
            textSize = cv2.getTextSize(labels[predicted], cv2.FONT_HERSHEY_COMPLEX, 0.7, 2)[0]
            textX = x1 + (x2-x1)//2-textSize[0]//2
            cv2.putText(frame, labels[predicted], (int(textX), y1), cv2.FONT_HERSHEY_COMPLEX, 0.7, labelColor[predicted], 2)
    except (TypeError, ValueError) as e:
        pass

    cv2.imshow("Face Recognizer", frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        cap.release()
        cv2.destroyAllWindows()