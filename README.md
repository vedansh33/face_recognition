# Face recognizer 
Using deep learning to recognize my face.
For a person to recognize your face is too normal but 
for a computer to do that it is a pretty difficult task .
So for that purpose I used computer vison .
Face recognition is a computer vison technology that helps to locate visulaize hauman faces in 
the digital image .
Face recognition is a problem of identifying amd verifying people in photo/video/real time 
by thier face.Deep learning methods are able to leverage very large datasets of faces and 
learn rich and compact representations of faces, allowing modern models to first perform as-well and later to outperform the face recognition capabilities of humans
<BR>In this, I have used PyTorch for computer vision and also used MobileNet V2 pre trained model to train my model according to my dataset.
 <BR>
  # Dataset Used
- My dataset was divided into training set and validation set
- Training set had 2 labels - "vedansh" and "not_vedansh"
- "vedansh" folder had around 200 images of my face and "not_aryan" folder had around 100 images of random faces
- Similarly in validation set "vedansh" consist of 90 images and "not_vedansh" consists of around 90 images.
<BR>
 # Procedure:
  ##bounding_box.py
  - this file is used for making bounding box and making landmarks around the faces in the datasets .
  - For training purposes Goggle collab is being uesd as it gives me advantage of increased RAM and GPU.
  - After that, I have used "MobileNet V2" to train my model according to my customized dataset.
  
  At last we will save the model so that we can use it to recognize face in real-time. 
  "Face Recognition.ipynb" is the notebook for this work.
  - I have used "OpenCV" library for accessing my webcame and "MTCNN" for detecting faces and landmarks. After that, use the frame and saved model to check if the if the person in front of camera is "vedansh" or "Not_vedansh". "face_recognizer_app.py" notebook has code for it.
  
  
  
