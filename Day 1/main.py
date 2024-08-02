import cv2

# 0 = Camera Channel
# VideoCapture(0) = Python Request into camera channel/device 0
cap = cv2.VideoCapture(0)

# Save frame into output.avi
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 10.0, (640, 480))

# isOpened mean, if VideoCapture getting channel of camera
while(cap.isOpened()):
    ret, frame = cap.read()

    if ret:
        # How to get height/width of frame
        height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
        print(height)
        width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
        print(width)

        # Insert frame into output.avi
        out.write(frame)

        # Change color of computer vision
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # outputing for input camera
        cv2.imshow('frame', gray)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# End handle
cap.release()
out.release()
cv2.destroyAllWindows()