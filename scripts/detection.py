import numpy as np
import imutils
import cv2


def detect_person(hog, paths):
    for imagePath in paths:
        image = cv2.imread(imagePath)
        time_start = cv2.getTickCount()
        image = imutils.resize(image, width=min(650, image.shape[1]))
        # image = cv2.cvtColor(image, cv2.COLOR_BAYER_BG2GRAY)
        (rects, weights) = hog.detectMultiScale(image, winStride=(6, 6),
                                                padding=(10, 10), scale=1.05)

        rects = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
        for (xA, yA, xB, yB) in rects:
            cv2.rectangle(image, (xA, yA), (xB, yB), (0, 255, 0), 2)
        time_end = cv2.getTickCount()
        cv2.putText(image, f'Detection Took:'
                    f'{(time_end - time_start)/cv2.getTickFrequency()} ',
                    (40, 40), cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 0, 0), 2)
        cv2.putText(image, f'Total Persons : {len(rects)}',
                    (40, 10), cv2.FONT_HERSHEY_DUPLEX, 0.6, (255, 0, 0), 2)

        cv2.imshow("Detection Results", image)
        cv2.waitKey(0)
