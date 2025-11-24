========================================================================
PROJECT: AI VIRTUAL MOUSE (HAND GESTURE CONTROL)
========================================================================

1. OVERVIEW
------------------------------------------------------------------------
The AI Virtual Mouse is a Human-Computer Interaction (HCI) project that 
enables users to control their system cursor using hand gestures. By 
processing video input from a webcam, the system tracks the user's index 
finger to move the mouse and detects a "pinch" gesture (Index + Thumb) 
to simulate a mouse click. This eliminates the need for physical hardware 
mouse devices.

2. FEATURES
------------------------------------------------------------------------
- Real-Time Tracking: Uses MediaPipe to track hand landmarks with low latency.
- Cursor Control: Maps the Index Finger tip coordinates to the screen size.
- Gesture Clicking: Simulates a left-click when the Index Finger and Thumb 
  come close together (Pinch gesture).
- Motion Smoothing: Implements a smoothing algorithm to prevent cursor 
  jitter and ensure fluid movement.
- Visual Feedback: Draws the hand skeleton and landmarks on the video feed.

3. PROJECT STRUCTURE
------------------------------------------------------------------------
AI_Virtual_Mouse/

 mouse.py            
 README.txt         
 REPORT.txt   

4. CODE LOGIC REVIEW
------------------------------------------------------------------------
The code operates in a continuous while-loop:

A. Initialization:
   - Sets up MediaPipe Hands with a confidence threshold of 0.5.
   - Captures Screen Width/Height using PyAutoGUI.

B. Pre-processing:
   - Flips the frame horizontally (Mirror Effect) for intuitive control.
   - Converts the image from BGR to RGB for MediaPipe processing.
   - Sets the image to "Not Writeable" to optimize performance.

C. Hand Tracking & Movement:
   - Detects Landmark 8 (Index Tip) and Landmark 4 (Thumb Tip).
   - Maps the Index Finger's webcam coordinates to the Monitor's resolution.
   - Applies a 'Smoothing Factor' (value: 2) to average out shaky movements.
   - Moves the actual OS cursor using `pyautogui.moveTo()`.

D. Click Action:
   - Calculates the distance between the Index Tip and Thumb Tip.
   - If distance < 0.05, `pyautogui.click()` is triggered.

5. ERROR HANDLING
------------------------------------------------------------------------
- Empty Frame Detection: The code checks `if not success:` after reading 
  from the camera. If the frame is empty, it prints a warning and skips 
  the iteration instead of crashing.
- Resource Management: Ensures `video_capture.release()` and 
  `cv2.destroyAllWindows()` are called upon exiting to free up the camera 
  for other apps.

6. EXAMPLE OUTPUT
------------------------------------------------------------------------
Console Output:
   > Press 'q' to quit the video stream.

Visual Output:
   - A window titled "Hand Detection and Air Mouse" appears.
   - Green lines connect the hand joints. 
   - Red dots appear on fingertips and knuckles.
   - As you move your hand, the mouse cursor on your desktop moves.
   - When you pinch, a click is registered.

========================================================================
END OF DOCUMENT
========================================================================