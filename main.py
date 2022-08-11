'''
    图像读取和像素操作
'''
import cv2
from matplotlib import pyplot as plt
import numpy as np
'''
    读取彩色图像信息并显示图片
'''
# 读取图片信息
img_OpenCV=cv2.imread('3.jpg')
# 获取图片BGR通道并重组
b,g,r=cv2.split(img_OpenCV)
# print(img_OpenCV,np.shape(img_OpenCV))
# print(b,np.shape(b))
img_matplotlib=cv2.merge([r,g,b])
print('图片信息读取成功')
# 绘制图片
figure=plt.figure(figsize=(12,8))
plt.subplot(121)
plt.imshow(img_OpenCV)
plt.subplot(122)
plt.imshow(img_matplotlib)
plt.show()
# 按通道显示图片
cv2.imshow('bgr image',img_OpenCV)
'''
    cv2.imshow函数：
        自适应窗口大小
        第一个参数是窗口名称
    waitKey函数：
        键盘绑定函数
        时间单位是毫秒
        指定时间间隔按下键盘任意键继续执行程序
    destroyAllWindows函数：
        删除窗口
'''
cv2.imshow('rgb image',img_matplotlib)
cv2.waitKey()
cv2.destroyAllWindows()
# 拼接图片
img_concat=np.concatenate((img_OpenCV,img_matplotlib),axis=1)
cv2.imshow('bgr image and rgb image',img_concat)
cv2.waitKey(0)
cv2.destroyAllWindows()
# 优化cv2.split()函数，前两个参数表示行列
B=img_OpenCV[:,:,0]
G=img_OpenCV[:,:,1]
R=img_OpenCV[:,:,2]
# 优化BGR转化为RGB
img_matplotlib=img_OpenCV[:,:,::-1]


'''
    访问操作像素
'''
# 获取图片信息
img_shape=img_OpenCV.shape
print('像素信息是{}'.format(img_shape))
img_size=img_OpenCV.size
print('图片大小是{}'.format(img_size))
img_elements_type=img_OpenCV.dtype
print('像素类型是{}'.format(img_elements_type))
# 访问某个像素值
(xb,xg,xr)=img_OpenCV[6,40]
xb=img_OpenCV[6,40,0]
# 修改像素值
img_OpenCV[6,40]=(0,0,255)
print('[6,40]像素的通道为{}'.format((xb,xg,xr)))
# 获取图片区域，可看作另一张图片
top_left_corner=img_OpenCV[0:250,0:250]
cv2.imshow('top left corner',top_left_corner)
cv2.waitKey()
cv2.destroyAllWindows()



'''
    灰度访问图像，没有通道
'''
gray_img=cv2.imread('3.jpg',cv2.IMREAD_GRAYSCALE)
img_shape=gray_img.shape
print('灰度图像的像素信息：{}'.format(img_shape))
cv2.imshow('gray img',gray_img)
cv2.waitKey()
cv2.destroyAllWindows()
# 修改像素信息
top_left_corner_gray=gray_img[0:250,0:250]
top_left_corner_gray=np.zeros((250,250))
gray_img[0:250,0:250]=top_left_corner_gray
cv2.imshow('gray img',gray_img)
cv2.waitKey()
cv2.destroyAllWindows()


