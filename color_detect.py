import cv2 as cv
import pandas as pd

img_path = r'G:/py program/color detection/colorpic.jpg'
img = cv.imread(img_path)
clicked = False
r = g = b = x_pos = y_pos = 0

index = ["color", "color_name", "hex", "R", "G", "B"]
csv = pd.read_csv('G:/py program/color detection/colors.csv', names=index, header=None)

def get_color_name(R, G, B):
    minimum = 10000
    for i in range(len(csv)):
        d = abs(R - int(csv.loc[i, "R"]))
        if d <= minimum:
            minimum = d
            cname = csv.loc[i, "color_name"]
    return cname

def draw_function(event, x, y, flags, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        global b, g, r, x_pos, y_pos, clicked
        clicked = True
        x_pos = x
        y_pos = y
        b, g, r = img[y, x]
        b, g, r = int(b), int(g), int(r)

cv.namedWindow('image')
cv.setMouseCallback('image', draw_function)

#video = cv.VideoCapture(0)
while True:
    #isTrue, img = video.read()
    cv.imshow("image", img)
    if clicked:
        cv.rectangle(img, (20, 20), (750, 60), (b, g, r), -1)
        text = get_color_name(r, g, b) + ' R=' + str(r)+ 'G=' + str(g) + 'B=' + str(b)
        cv.putText(img, text, (50, 50), 2, 0.8, (255, 255, 255), 2, cv.LINE_AA)

        if r + g + b >= 600:
            cv.putText(img, text, (50, 50), 2, 0.8, (0, 0, 0), 2, cv.LINE_AA)
        clicked = False

    if cv.waitKey(20) & 0xff == ord('q'):
        break

#video.release()
cv.destroyAllWindows()