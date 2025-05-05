# emotion detection,emotion recognition,emotion processing,emotion capturing,emotion streaming,emotion editing,emotion image editing,emotion video editing,emotion image processing,emotion video processing,emotion image capturing,emotion video capturing Load the video
import cv2
from deepface import DeepFace
import threading

def analyze_frame(frame):
    result = DeepFace.analyze(frame, actions=['emotion', 'age', 'gender'], enforce_detection=False)
    return result[0]

video = cv2.VideoCapture(0)
try:
    while True:
        ret, frame = video.read()
        if not ret:
            break

        # Use threading to analyze the frame in a separate thread
        analysis_thread = threading.Thread(target=analyze_frame, args=(frame,))
        analysis_thread.start()
        analysis_thread.join()

        # Analyze the frame for emotions, age, and gender
        result = analyze_frame(frame)
        
        # Access the results
        emotion = result['dominant_emotion']
        age = result['age']
        gender = result['gender']
        
        # Display the results on the frame
        cv2.putText(frame, f'Emotion: {emotion}', (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, f'Age: {age}', (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        cv2.putText(frame, f'Gender: {gender}', (50, 150), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        
        # Show the frame
        cv2.imshow('Emotion, Age, and Gender Detection', frame)

        # Break the loop on 'q' key press
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
finally:
    # Release the video capture object and close all OpenCV windows
    video.release()
    cv2.destroyAllWindows()
    
