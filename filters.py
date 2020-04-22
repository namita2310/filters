import cv2
import matplotlib.pyplot as plt
import numpy as np
nemo=cv2.imread("girl.jpg")
cv2.imshow("original",nemo)
#plt.show()
cv2.waitKey(100)
new=cv2.cvtColor(nemo, cv2.COLOR_BGR2RGB)
cv2.imshow("1",new)
status=cv2.imwrite("./filter/1.jpg",new)

cv2.waitKey(100)
gray_image = cv2.cvtColor(nemo, cv2.COLOR_BGR2GRAY) 
  
cv2.imshow('2', gray_image)
status=cv2.imwrite("./filter/2.jpg",new) 
cv2.waitKey(100)   
new=cv2.cvtColor(nemo,cv2.COLOR_XYZ2RGB)
#plt.imshow(nemo_1)
#plt.show()
cv2.imshow("3",new)
status=cv2.imwrite("./filter/3.jpg",new)
cv2.waitKey(100)
new=cv2.cvtColor(nemo,cv2.COLOR_BGR2BGRA)
cv2.imshow("4",new)
status=cv2.imwrite("./filter/4.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGR2HLS)
cv2.imshow("5",new)
status=cv2.imwrite("./filter/5.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGR2HLS_FULL)
cv2.imshow("6",new)
status=cv2.imwrite("./filter/6.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGR2HSV)
cv2.imshow("7",new)
status=cv2.imwrite("./filter/7.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGR2HSV_FULL)
cv2.imshow("8",new)
status=cv2.imwrite("./filter/8.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGR2LAB)
cv2.imshow("9",new)
status=cv2.imwrite("./filter/9.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGR2LUV)
cv2.imshow("10",new)
status=cv2.imwrite("./filter/10.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGR2Lab)
cv2.imshow("11",new)
status=cv2.imwrite("./filter/11.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGR2Luv)
cv2.imshow("12",new)
status=cv2.imwrite("./filter/12.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGR2RGBA)
cv2.imshow("13",new)
status=cv2.imwrite("./filter/13.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGR2XYZ)
cv2.imshow("14",new)
status=cv2.imwrite("./filter/14.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGR2YCR_CB)
cv2.imshow("15",new)
status=cv2.imwrite("./filter/15.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGR2YUV)
cv2.imshow("16",new)
status=cv2.imwrite("./filter/16.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGRA2BGR)
cv2.imshow("17",new)
status=cv2.imwrite("./filter/17.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGRA2GRAY)
cv2.imshow("18",new)
status=cv2.imwrite("./filter/18.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGRA2RGB)
cv2.imshow("19",new)
status=cv2.imwrite("./filter/19.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_BGRA2RGBA)
cv2.imshow("20",new)
status=cv2.imwrite("./filter/20.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_HLS2BGR)
cv2.imshow("21",new)
status=cv2.imwrite("./filter/21.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_HLS2BGR_FULL)
cv2.imshow("22",new)
status=cv2.imwrite("./filter/22.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_HLS2RGB)
cv2.imshow("23",new)
status=cv2.imwrite("./filter/23.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_HLS2RGB_FULL)
cv2.imshow("24",new)
status=cv2.imwrite("./filter/24.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_HSV2BGR)
cv2.imshow("25",new)
status=cv2.imwrite("./filter/25.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_HSV2BGR_FULL)
cv2.imshow("26",new)
status=cv2.imwrite("./filter/26.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_HSV2RGB)
cv2.imshow("27",new)
status=cv2.imwrite("./filter/27.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_HSV2RGB_FULL)
cv2.imshow("28",new)
status=cv2.imwrite("./filter/28.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LAB2BGR)
cv2.imshow("29",new)
status=cv2.imwrite("./filter/29.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LAB2LBGR)
cv2.imshow("30",new)
status=cv2.imwrite("./filter/30.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LAB2LRGB)
cv2.imshow("31",new)
status=cv2.imwrite("./filter/31.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LAB2RGB)
cv2.imshow("32",new)
status=cv2.imwrite("./filter/32.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LBGR2LAB)
cv2.imshow("33",new)
status=cv2.imwrite("./filter/33.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LBGR2LUV)
cv2.imshow("34",new)
status=cv2.imwrite("./filter/34.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LBGR2Lab)
cv2.imshow("35",new)
status=cv2.imwrite("./filter/35.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LBGR2Luv)
cv2.imshow("36",new)
status=cv2.imwrite("./filter/36.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LRGB2LAB)
cv2.imshow("37",new)
status=cv2.imwrite("./filter/37.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LRGB2LUV)
cv2.imshow("38",new)
status=cv2.imwrite("./filter/38.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LRGB2Lab)
cv2.imshow("39",new)
status=cv2.imwrite("./filter/39.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LRGB2Luv)
cv2.imshow("40",new)
status=cv2.imwrite("./filter/40.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LUV2BGR)
cv2.imshow("41",new)
status=cv2.imwrite("./filter/41.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LUV2LBGR)
cv2.imshow("42",new)
status=cv2.imwrite("./filter/42.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LUV2LRGB)
cv2.imshow("43",new)
status=cv2.imwrite("./filter/43.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_LUV2RGB)
cv2.imshow("44",new)
status=cv2.imwrite("./filter/44.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_Lab2BGR)
cv2.imshow("45",new)
status=cv2.imwrite("./filter/45.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_Lab2LBGR)
cv2.imshow("46",new)
status=cv2.imwrite("./filter/46.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_Lab2LRGB)
cv2.imshow("47",new)
status=cv2.imwrite("./filter/47.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_Lab2RGB)
cv2.imshow("48",new)
status=cv2.imwrite("./filter/48.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_Luv2BGR)
cv2.imshow("49",new)
status=cv2.imwrite("./filter/49.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_Luv2LBGR)
cv2.imshow("50",new)
status=cv2.imwrite("./filter/50.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_Luv2LRGB)
cv2.imshow("51",new)
status=cv2.imwrite("./filter/51.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_Luv2RGB)
cv2.imshow("52",new)
status=cv2.imwrite("./filter/52.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2BGR)
cv2.imshow("53",new)
status=cv2.imwrite("./filter/53.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2BGRA)
cv2.imshow("54",new)
status=cv2.imwrite("./filter/54.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2GRAY)
cv2.imshow("55",new)
status=cv2.imwrite("./filter/55.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2HLS)
cv2.imshow("56",new)
status=cv2.imwrite("./filter/56.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2HLS_FULL)
cv2.imshow("57",new)
status=cv2.imwrite("./filter/57.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2HSV)
cv2.imshow("58",new)
status=cv2.imwrite("./filter/58.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2HSV_FULL)
cv2.imshow("59",new)
status=cv2.imwrite("./filter/59.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2LAB)
cv2.imshow("60",new)
status=cv2.imwrite("./filter/60.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2LUV)
cv2.imshow("61",new)
status=cv2.imwrite("./filter/61.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2Lab)
cv2.imshow("62",new)
status=cv2.imwrite("./filter/62.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2Luv)
cv2.imshow("63",new)
status=cv2.imwrite("./filter/63.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2RGBA)
cv2.imshow("64",new)
status=cv2.imwrite("./filter/64.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2XYZ)
cv2.imshow("65",new)
status=cv2.imwrite("./filter/65.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2YCR_CB)
cv2.imshow("66",new)
status=cv2.imwrite("./filter/66.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2YCrCb)
cv2.imshow("67",new)
status=cv2.imwrite("./filter/67.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGB2YUV)
cv2.imshow("68",new)
status=cv2.imwrite("./filter/68.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGBA2BGR)
cv2.imshow("69",new)
status=cv2.imwrite("./filter/69.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_RGBA2GRAY)
cv2.imshow("70",new)
status=cv2.imwrite("./filter/70.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_XYZ2BGR)
cv2.imshow("71",new)
status=cv2.imwrite("./filter/71.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_XYZ2RGB)
cv2.imshow("72",new)
status=cv2.imwrite("./filter/72.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_YCR_CB2BGR)
cv2.imshow("73",new)
status=cv2.imwrite("./filter/73.jpg",new)
cv2.waitKey(200)

new=cv2.cvtColor(nemo,cv2.COLOR_YCR_CB2RGB)
cv2.imshow("74",new)
status=cv2.imwrite("./filter/74.jpg",new)
cv2.waitKey(100)

new=cv2.cvtColor(nemo,cv2.COLOR_YCrCb2BGR)
cv2.imshow("75",new)
status=cv2.imwrite("./filter/75.jpg",new)
cv2.waitKey(200)
new=cv2.cvtColor(nemo,cv2.COLOR_YCrCb2RGB)
cv2.imshow("76",new)
status=cv2.imwrite("./filter/76.jpg",new)
cv2.waitKey(200)
new=cv2.cvtColor(nemo,cv2.COLOR_YUV2BGR)
cv2.imshow("77",new)
status=cv2.imwrite("./filter/77.jpg",new)
cv2.waitKey(200)
new=cv2.cvtColor(nemo,cv2.COLOR_YUV2RGB)
cv2.imshow("78",new)
status=cv2.imwrite("./filter/78.jpg",new)
cv2.waitKey(100)

cv2.destroyAllWindows()


