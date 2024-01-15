import cv2
import numpy as np
import time

# Define the video capture device
cap = cv2.VideoCapture(0)

# Define the face and eye classifiers
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

# Define the EAR threshold
ear_threshold = 0.25

# Define the timer variables
start_time = 0
end_time = 0
alarm_on = False

while True:
    # Capture the video frame
    ret, frame = cap.read()

    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the grayscale frame
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x,y,w,h) in faces:
        # Draw a rectangle around the face
        cv2.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), 2)

        # Crop the face region
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = frame[y:y+h, x:x+w]

        # Detect eyes in the face region
        eyes = eye_cascade.detectMultiScale(roi_gray)

        for (ex,ey,ew,eh) in eyes:
            # Draw a rectangle around the eye
            cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

            # Calculate the eye aspect ratio (EAR)
            left_eye = roi_gray[ey:ey+eh, ex:ex+int(ew/2)]
            right_eye = roi_gray[ey:ey+eh, ex+int(ew/2):ex+ew]
            left_ear = get_ear(left_eye)
            right_ear = get_ear(right_eye)
            ear = (left_ear + right_ear) / 2

            # Check if the EAR falls below the threshold
            if ear < ear_threshold:
                # Start the timer if not already started
                if not alarm_on:
                    start_time = time.time()
                    alarm_on = True
                
                # Calculate the elapsed time since the alarm started
                elapsed_time = time.time() - start_time

                # Check if the elapsed time is greater than the threshold
                if elapsed_time > 2: # Change the threshold as per requirement
                    # Play an alarm sound or flash a warning message
                    print("Driver is drowsy!")
            else:
                # Reset the timer if the EAR is above the threshold
                alarm_on = False

    # Display the resulting frame
    cv2.imshow('frame',frame)

    # Stop the program if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture device and close all windows
cap.release()
cv2.destroyAllWindows()

def get_ear(eye):
    # Calculate the eye aspect ratio (EAR)
    vert1 = np.linalg.norm(eye[1] - eye[5])
    vert2 = np.linalg.norm(eye[2] - eye[4])
    horiz = np.linalg.norm(eye[0] - eye[3])
    ear = (vert1 + vert2) / (2.0 * horiz)
   
