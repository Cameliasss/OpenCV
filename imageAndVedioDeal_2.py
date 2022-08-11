'''
    处理图像视频并以图像视频形式输出
    OpenCV构建计算机视觉
    流程：
        图像、视频输入--OpenCV项目处理--图像、视频输出
'''
import cv2
import numpy as np
from matplotlib import pyplot as plt
import argparse

'''
    读取图片
    使用argparse模块解析命令行参数
    详见CSDN
'''
# parser=argparse.ArgumentParser(description="Read image and vedio")
# parser.add_argument('file_path')
# parser.add_argument('path_img_output')
# args=parser.parse_args()
# img1=cv2.imread(args.file_path)
# # vars函数构造字典
# args=vars(parser.parse_args())
# img2=cv2.imread(args['file_path'])
# img_concat=np.concatenate((img1,img2),axis=1)
# '''
#     cv2.cvtColor(p1,p2) 是颜色空间转换函数，p1是需要转换的图片，p2是转换成何种格式。
# '''
# img_gray=cv2.cvtColor(img_concat,cv2.COLOR_BGR2GRAY)
# cv2.imshow('img1 and img2',img_concat)
# cv2.waitKey()
# cv2.destroyAllWindows()
# # 写出图片
# cv2.imwrite(args['path_img_output'],img_gray)
# cv2.waitKey()
# cv2.destroyAllWindows()


'''
    读取相机画面
'''
# parser1=argparse.ArgumentParser(description='camera capture')
# parser1.add_argument('camera_index',type=int)
# args1=parser1.parse_args()
#
# capture=cv2.VideoCapture(args1.camera_index)
# if capture.isOpened() is False:
#     print('Error! Camera is closed!')
# while capture.isOpened():
#     ret,frame=capture.read()
#     if ret is True:
#         cv2.imshow('camera capture',frame)
#         cv2.waitKey()
#         # cv2.destroyAllWindows()
#         gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imshow('gray frame',gray_frame)
#         # 按下q退出执行
#         if cv2.waitKey(1000) & 0xFF==ord('q'):
#             break
#     else:
#         break
# capture.release()
# cv2.destroyAllWindows()


'''
    访问获取画面的属性
    get函数
'''
# capture1=cv2.VideoCapture(0)
# height=capture1.get(cv2.CAP_PROP_FRAME_HEIGHT)
# width=capture1.get(cv2.CAP_PROP_FRAME_WIDTH)
# fps=capture1.get(cv2.CAP_PROP_FPS)
# print('相机获取帧的高度是：{}\n宽度是：{}\n每秒帧数：{}'.format(height,width,fps))


'''
    保存相机画面
'''
# capture=cv2.VideoCapture(0)
# if capture.isOpened() is False:
#     print('Error! Camera is closed!')
# frame_index=0
# while capture.isOpened():
#     ret,frame=capture.read()
#
#     if ret is True:
#         gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imshow('gray frame',gray_frame)
#         if cv2.waitKey(1000) & 0xFF==ord('c'):
#             frame_name='camera_capture{}.jpg'.format(frame_index)
#             gray_frame_name='camera_capture_gray{}.jpg'.format(frame_index)
#             cv2.imwrite(frame_name,frame)
#             cv2.imwrite(gray_frame_name,gray_frame)
#             frame_index+=1
#         if cv2.waitKey(1000)& 0xFF==ord('q'):
#             break
#     else:
#         break
# capture.release()
# cv2.destroyAllWindows()


'''
    读取视频画面
'''
# capture=cv2.VideoCapture('test.mp4')
# if capture.isOpened() is False:
#     print('Error! Camera is closed!')
# while capture.isOpened():
#     ret,frame=capture.read()
#     if ret is True:
#         gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         cv2.imshow('gray frame',gray_frame)
#         # 按下q退出执行
#         if cv2.waitKey(10) & 0xFF==ord('q'):
#             break
#     else:
#         break
# capture.release()
# cv2.destroyAllWindows()


'''
    计算帧率
'''
# import time
# capture=cv2.VideoCapture(0)
# if capture.isOpened() is False:
#     print('摄像头未开')
# while capture.isOpened():
#     ret,frame=capture.read()
#
#     if ret is True:
#         start_time=time.time()
#         cv2.imshow('frame now',frame)
#         if cv2.waitKey(20) & 0xFF==ord('q'):
#             break
#         end_time = time.time()
#         process_time=end_time-start_time
#         print('FPS={}'.format(1.0/process_time))
#     else:
#         break
# capture.release()
# cv2.destroyAllWindows()


'''
    写入视频文件
    视频文件压缩示例
'''
# parser=argparse.ArgumentParser()
# parser.add_argument('out_path')
# args=parser.parse_args()
#
# capture=cv2.VideoCapture(0)
# height=capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
# width=capture.get(cv2.CAP_PROP_FRAME_WIDTH)
# fps=capture.get(cv2.CAP_PROP_FPS)
#
# fourcc=cv2.VideoWriter_fourcc(*'XVID')
# out_gray=cv2.VideoWriter(args.out_path,fourcc,int(fps),(int(width),int(height)),False)
#
# if capture.isOpened() is False:
#     print('摄像头关闭')
# while capture.isOpened():
#     ret,frame=capture.read()
#     if ret:
#         gray_frame=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
#         out_gray.write(gray_frame)
#         cv2.imshow('gray frame',gray_frame)
#
#         if cv2.waitKey(20) & 0xFF==ord('q'):
#             break
#     else:
#         break
# capture.release()
# out_gray.release()
# cv2.destroyAllWindows()

'''
    倒放视频并保存
'''
# def decode_fourcc(fourcc):
#     fourcc_int=int(fourcc)
#     result=""
#     for i in range(4):
#         result+=chr(fourcc_int>>8*i&0xFF)
#     return result
#
# parser=argparse.ArgumentParser()
# parser.add_argument('out_path')
# args=parser.parse_args()
#
# capture=cv2.VideoCapture('test.mp4')
# width=capture.get(cv2.CAP_PROP_FRAME_WIDTH)
# height=capture.get(cv2.CAP_PROP_FRAME_HEIGHT)
# fps=capture.get(cv2.CAP_PROP_FPS)
# decode=decode_fourcc(capture.get(cv2.CAP_PROP_FOURCC))
#
# fourcc=cv2.VideoWriter_fourcc(*decode)
# out=cv2.VideoWriter(args.out_path,fourcc,int(fps),(int(width),int(height)),True)
#
# if capture.isOpened() is False:
#     print('摄像头关闭')
# frame_index=capture.get(cv2.CAP_PROP_FRAME_COUNT)-1
#
# while capture.isOpened() and frame_index>=0:
#     capture.set(cv2.CAP_PROP_POS_FRAMES,frame_index)
#     ret,frame=capture.read()
#     if ret:
#         cv2.imshow('original frame',frame)
#         out.write(frame)
#         frame_index-=1
#         if cv2.waitKey(1) & 0xFF==ord('q'):
#             break
#     else:
#         break
#
# capture.release()
# out.release()
# cv2.destroyAllWindows









