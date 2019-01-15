import cv2
import face_recognition
import sys

known_names = []
known_faces_encoding = []
known_password = []
face_locations = []
face_encodings = []
face_names = []
l = False

def help():
    print("Write 'reg', if you want to sign up")
    print("Write 'id', if you want to enter to the system")
    print("Write 'exit', if you want to close the program")

def desc():
    print("")

def id():
    y = False
    process_this_frame = True
    name = ''
    pass_conter = 0
    w = False
    print("Stand opposite the camera.")
    print("When you will ready, press 'q'")
    while (y != True):
        video_capture = cv2.VideoCapture(0)
        while True:

            ret, frame = video_capture.read()

            cv2.imshow('Video', frame)

            small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)

            rgb_small_frame = small_frame[:, :, ::-1]

            if process_this_frame:
                face_locations = face_recognition.face_locations(rgb_small_frame)
                face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

                face_names = []
                for face_encoding in face_encodings:
                    matches = face_recognition.compare_faces(known_faces_encoding, face_encoding)
                    name = "Unknown"

                    if True in matches:
                        first_match_index = matches.index(True)
                        name = known_names[first_match_index]

                    face_names.append(name)

            process_this_frame = not process_this_frame

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        video_capture.release()
        cv2.destroyAllWindows()

        if (name != "Unknown"):
            print("Welcome, {}".format(name))
            print("Write your password.")
            while (w != True):
                etal_pass = known_password[known_names.index(name)]
                password = input()
                if (etal_pass == hash("k05m0navt" + password + str(name))):
                    w = True
                    y = True
                else:
                    pass_conter += 1
                    print("Wrong password.")
                    print("Do you want to repeat?")
                    ans = input()
                    if (pass_conter == 3):
                        sys.exit()
                    else:
                        if (ans == "yes"):
                            continue
                        else:
                            sys.exit()
        else:
            print("You need to register.")
            reg()
    print("Congratulate, you can pass!")



def reg():
    print("I need to add your face to data base. Stand opposite the camera.")
    print("When you will ready, press 'q'")

    img = cv2.VideoCapture(0)
    while True:
        ret, frame = img.read()

        cv2.imshow('Video', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    img.release()
    cv2.destroyAllWindows()

    face_encod = face_recognition.face_encodings(frame)[0]
    known_faces_encoding.append(face_encod)

    print("Please write your name:")
    name = input()
    known_names.append(name)

    print("Please write your password:")
    passw = input()
    h_pasw = "k05m0navt" + passw + name
    hash_passw = hash(h_pasw)
    known_password.append(hash_passw)

    print("You can try to enter.")

print("Hello!")
print("Write, what do you want to do:")
while(l != True):
    ans = input()
    if (ans == 'reg'):
        reg()
        id()
        l = True
    elif(ans == 'id'):
        id()
        l = True
    elif (ans == 'exit'):
        sys.exit()
    else:
        help()
