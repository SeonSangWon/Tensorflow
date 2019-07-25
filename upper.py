import cv2
import sys

#이미지 경로받아오기
path = sys.argv[1]
src = cv2.imread(path , cv2.IMREAD_COLOR)
copy_file = src.copy()

#이미지 줄이기
dst = cv2.resize(src, dsize=(750,664), interpolation=cv2.INTER_AREA)	

#이미지 자르기
#가로 : 550 세로 : 620
image = dst.copy()
image = dst[30:650, 100:650]


#상의 이미지 추출
#가로 : 550 세로 : 325
upper = image.copy()
upper = image[0:325, 0:600]


#하의 이미지 추출
#가로 : 550 세로 : 295
lower = image.copy()
lower = image[325:620, 0:600]


#cv2.imshow("dst", dst)
#cv2.imshow("image", image)

#상의 하의 출력
#cv2.imshow("upper", upper)
#cv2.imshow("lower", lower)

#원래있던 경로의 이미지에 상의를 덮어씌움
cv2.imwrite(path, upper)
#cv2.imwrite("lower.jpg", lower)

#원본 이미지 복사  
origin_path = sys.argv[1]
copy_path = origin_path[:-4] + "-1.jpg"
print(copy_path)
cv2.imwrite(copy_path, copy_file)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
