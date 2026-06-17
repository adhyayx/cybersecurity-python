import cv2
from cvzone.HandTrackingModule import HandDetector
import pyautogui
import time

detector = HandDetector(maxHands=1, detectionCon=0.7)
cap = cv2.VideoCapture(0)

last_action_time = 0
prev_y = None  # Pichli position track karne ke liye

print("Chal raha hai! Q dabao band karne ke liye.")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Webcam nahi mila!")
        break

    frame = cv2.flip(frame, 1)
    hands, frame = detector.findHands(frame)
    finger_count = 0
    action_text = ""

    if hands:
        hand = hands[0]
        fingers = detector.fingersUp(hand)
        finger_count = sum(fingers)

        # Haath ki center position
        cx, cy = hand['center']

        current_time = time.time()

        # --- SCROLL (1 ungli + haath move karo) ---
        if finger_count == 1:
            if prev_y is not None:
                diff = cy - prev_y  # Kitna move hua

                if diff < -8:  # Haath upar gaya
                    pyautogui.scroll(3)
                    action_text = "Scroll UP"
                    print("Scroll UP")

                elif diff > 8:  # Haath neeche gaya
                    pyautogui.scroll(-3)
                    action_text = "Scroll DOWN"
                    print("Scroll DOWN")

            prev_y = cy  # Position save karo

        else:
            prev_y = None  # Reset karo jab 1 ungli na ho

        # --- BAAKI GESTURES ---
        if current_time - last_action_time > 1.5:

            if finger_count == 2:
                pyautogui.press('left')
                action_text = "BACK"
                print("2 Ungliyan - BACK")
                last_action_time = current_time

            elif finger_count == 5:
                pyautogui.press('space')
                action_text = "PLAY/PAUSE"
                print("5 Ungliyan - PLAY/PAUSE")
                last_action_time = current_time

            elif finger_count == 0:
                pyautogui.press('volumemute')
                action_text = "MUTE"
                print("Mutthi - MUTE")
                last_action_time = current_time

            elif finger_count == 3:
                pyautogui.press('right')
                action_text = "NEXT"
                print("3 Ungliyan - NEXT")
                last_action_time = current_time

    # Screen pe info dikhao
    cv2.putText(frame, f"Ungliyan: {finger_count}", (10, 50),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 255, 0), 2)
    cv2.putText(frame, f"Action: {action_text}", (10, 90),
                cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 200, 255), 2)

    cv2.imshow("Gesture Controller", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()