import cv2
import numpy as np
from imutils import face_utils
from face_detection import Face_utilities
from signalprocessing import Signal_processing
import time



if __name__ == "__main__":

    option=int(input('VIDEO(press'1')_OR_REALTIME(press'0'): '))
    BUFFER_SIZE = int(input('USE_BUFFER_SIZE: '))
    if option == 1:
        path=str(input('PATH: '))
        cap = cv2.VideoCapture(path)
    else:
        cap = cv2.VideoCapture(option)

    #intial_module
    fu = Face_utilities()
    sp = Signal_processing()

    i = 0
    fps = 0  
    buffer_data = []
    bpm = 0
    bpms = []
    times = []
    start_time = time.perf_counter()

    while True:

        ret, frame = cap.read()
        frame = cv2.flip(frame, 1)

        bb_box = frame.copy()
        if frame is None:
            print("End of video")
            cv2.destroyAllWindows()
            break

        rects, shape, time_s = fu.no_age_gender_face_process(frame, start_time)
         
        if rects is None:
            cv2.putText(frame, "No face detected", (30, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
            cv2.imshow("frame", frame)
            if cv2.waitKey(1) & 0xFF == ord('q'):
                cv2.destroyAllWindows()
                break
            continue

        (x, y, w, h) = face_utils.rect_to_bb(rects[0])
        
        # creat bounding_box
        cv2.rectangle(bb_box, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.putText(bb_box, "Frame: {0:.2f}".format(i), (30, int(frame.shape[0] * 0.2)), cv2.FONT_HERSHEY_SIMPLEX, 1,
                    (255, 0, 0), 2)

        img = frame
        bbbox = img.copy()
        cv2.putText(bbbox, "frame: {}".format(i), (30, int(frame.shape[0] * 0.95) - 30), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (255, 0, 0), 2)
        #Find_ROI
        Roi1 = img[shape[70][1]:shape[23][1], shape[70][0]:shape[23][0]]
        #cv2.rectangle(bbbox, (shape[70][0], shape[70][1]), (shape[23][0], shape[23][1]), (0, 255, 0), 2)
        ROI2 = img[shape[29][1]:shape[33][1], shape[54][0]:shape[12][0]]
        #cv2.rectangle(bbbox, (shape[54][0], shape[29][1]), (shape[12][0], shape[33][1]), (0, 255, 0), 2)
        ROI3 = img[shape[29][1]:shape[33][1], shape[4][0]:shape[48][0]]
        #cv2.rectangle(bbbox, (shape[4][0], shape[29][1]), (shape[48][0], shape[33][1]), (0, 255, 0), 2)  
    
        #Find_pixel_AVG_of_ROI
        avg1 = np.mean(Roi1[:, :, 1])
        avg2 = np.mean(ROI2[:, :, 1])
        avg3 = np.mean(ROI3[:, :, 1])
        avg = [avg1, avg2, avg3]
        Raw_rppg = np.mean(avg)

        if rects is not None:
            times.append(time_s)
            
        buffer_data.append(Raw_rppg)

        L = len(buffer_data)

        if L > BUFFER_SIZE:
            buffer_data = buffer_data[-BUFFER_SIZE:]
            times = times[-BUFFER_SIZE:]
            L = BUFFER_SIZE

        if L == BUFFER_SIZE:
            diff = times[-1] - times[0]
            fps = float(L) / diff
            cv2.putText(bb_box, "Fs: {0:.2f}".format(fps), (int(frame.shape[1] * 0.68), int(frame.shape[0] *0.2)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 200, 0), 2)

            detrended_data = sp.signal_detrending(buffer_data)
            interpolated_data = sp.interpolation(detrended_data, times)
            normalize_data = sp.normalization(detrended_data)
            filtered_data = sp.butter_bandpass_filter(normalize_data, 0.7, 4, fps, order=5)

            psd, freqs_in_minute, resolution = sp.fft(filtered_data, fps)
            idxfreq = np.where((freqs_in_minute > 45) & (freqs_in_minute < 180))[0]
            interest_idx_sub = idxfreq[:-1].copy()
            freqs_of_interest = freqs_in_minute[interest_idx_sub]
            fft_of_interest = psd[interest_idx_sub]
            max_arg = np.argmax(fft_of_interest)

            bpm = freqs_of_interest[max_arg]
            bpms.append(bpm)
            cv2.putText(bb_box, "HR: {}".format(int(bpm)), (int(frame.shape[1] * 0.64), int(frame.shape[0] * 0.95)),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        #reccord_HR_timestamp
        #with open(r"C:\Users\User\Desktop\project report\realexp2.csv", mode="a+") as f:
        #f.write("{0:.2f} ".format(times[-1]) + ", {0:.2f} ".format(hr) + ", {0:.2f} ".format(bpm) + "\n")
        
        cv2.imshow("frame", bb_box)
        i = i + 1

        # waitKey to show the frame and break loop whenever 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cv2.destroyAllWindows()
            break

    cap.release()
    cv2.destroyAllWindows()


