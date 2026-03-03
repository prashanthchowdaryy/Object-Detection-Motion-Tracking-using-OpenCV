# ----------> IMPORT LIBRARIES
import cv2
import mediapipe as mp

# ----------> MEDIAPIPE SETUP
mp_objectron = mp.solutions.objectron
mp_drawing = mp.solutions.drawing_utils

# ----------> VIDEO SOURCE
cap = cv2.VideoCapture(r"C:\Users\Prashanth\Desktop\Naresh_it\AI\DeepLearning\mediapipe_project\shoe.mp4")

# ----------> OBJECTRON MODEL
objectron = mp_objectron.Objectron(
    static_image_mode=False,
    max_num_objects=2,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5,
    model_name='Shoe'   # Supported: 'Shoe', 'Chair', 'Cup', 'Camera', 'Laptop'
)

# ----------> WINDOW
cv2.namedWindow("MediaPipe Objectron", cv2.WINDOW_NORMAL)

print("Press Q to quit")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Video ended or cannot read frame.")
        break

    # Resize first for stability
    frame = cv2.resize(frame, (960, 540))

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    rgb_frame.flags.writeable = False

    # Process frame
    results = objectron.process(rgb_frame)

    rgb_frame.flags.writeable = True

    # Draw detections
    if results.detected_objects:
        for detected_object in results.detected_objects:
            mp_drawing.draw_landmarks(
                frame,
                detected_object.landmarks_2d,
                mp_objectron.BOX_CONNECTIONS
            )

            mp_drawing.draw_axis(
                frame,
                detected_object.rotation,
                detected_object.translation
            )

    cv2.imshow("MediaPipe Objectron", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()