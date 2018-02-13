#!/usr/bin/env python
#coding: utf-8 
import pymssql
import xlwt
import datetime
import xlrd
import xlwt
import time
import pandas as pd
import numpy as np
import scipy.stats as stats
from matplotlib import pyplot

# catering_sale = 'd:/test.xlsx' #餐饮数据，含有其他属性
# data = pd.read_excel(catering_sale,'result-1',index_col = u'日期') #读取数据，指定“日期”列为索引列
# print(data)
# d1=data.corr() #相关系数矩阵，即给出了任意两款菜式之间的相关系数
# # print(d1)
# # print("\n")
# d1.to_excel('d:/result.xlsx',sheet_name='sum',header=True,index=True)
# # d2=data.corr()[u'O2O占比'] #只显示“百合酱蒸凤爪”与其他菜式的相关系数
# # print(d2)
# # print('\n')#打印换行单引号双引号都行，*3表示打印3个空行
# # d3=data[u'O2O占比'].corr(data[u'人效']) #计算“百合酱蒸凤爪”与“翡翠蒸香茜饺”的相关系数
# # print(d3)
# #水果占比和大货占比有正相关性？
def f1():
	data_s = 25.1
	data_e = 35.9
	sample_list = [22.113,22.550,25.463,29.844,40.253,31.030,26.464,32.880,33.960,36.120,33.952,36.022,36.183,31.227,31.960,28.495,35.051,30.375,34.173,37.952,34.759,29.670,32.774,30.187,27.223,30.061,28.536,30.281,23.642,25.520,28.790]
	#19.86284553333333&30.96
	#sample_list = [22.550,25.463,29.844,31.030,26.464,32.880,33.960,36.120,33.952,36.022,36.183,31.227,31.960,28.495,35.051,30.375,34.173,37.952,34.759,29.670,32.774,30.187,27.223,30.061,28.536,30.281,23.642,25.520,28.790]
	test_list = [i/100 for i in range(2510,4000,1)]
	mean_ = np.mean(sample_list)
	median_ = np.median(sample_list)
	mode_ = stats.mode(sample_list)
	ptp_ = np.ptp(sample_list)
	var_ = np.var(sample_list)
	std_ = np.std(sample_list)
	#变异系数
	cv = std_/mean_
	#print(cv)
	#z-分数= (sample_list[0] - mean_)/std_　
	#通常来说，z-分数的绝对值大于3将视为异常。
	for i in sample_list:
		z_ = (i-mean_)/std_
		if abs(z_) >= 2:
			print(i)
			print(z_)
	#print(var_)
	#print(std_)
	return -1
	#15.401652428571428 & 30.94
	#print(temp_list)
	var_list = []
	for i in test_list:
		var_ = 0
		for j in sample_list:
			var_ += (i-j)*(i-j)
		var_ = var_/(len(sample_list)-1)
		var_list.append({"var_":var_,"test_v":i})
	min = 100
	min_index = 0
	for i in var_list:
		# print(i["var_"])
		# print(i["test_v"])
		# break
		if i["var_"] < min :
			min = i["var_"]
			min_index = i["test_v"] 
	print(min) 
	print(min_index)
#f1()
def f2():
	from numpy import array
	from numpy.random import normal, randint
	#使用List来创造一组数据
	data = [1, 2, 3,3,4,4,4]
	print(stats.mode(data).mode)
	return -1 
	#使用ndarray来创造一组数据
	data = array([1, 2, 3])
	print(data)
	#创造一组服从正态分布的定量数据
	data = normal(0, 10, size=10)
	print(data)
	#创造一组服从均匀分布的定性数据
	data = randint(0, 10, size=10)
	print(data)
#f2()
def f3():
	# sample_list = [22.113,22.550,25.463,29.844,40.253,31.030,26.464,32.880,33.960,36.120,33.952,36.022,36.183,31.227,31.960,28.495,35.051,30.375,34.173,37.952,34.759,29.670,32.774,30.187,27.223,30.061,28.536,30.281,23.642,25.520,28.790]
	sample_list = [20.693,24.91385768,26.3318649,27.79731744,28.09243697,27.04375497,24.45437616,32.35374928,27.86934023,27.68441065,26.081142,27.1611479,26.84087363,27.60592044,29.17692806,27.40770252,24.94520548,29.06202723,25.76773296,29.3253493,31.5565032,27.30453258,25.60095579,27.36899563,24.13309776,29.81290602,27.67776017,31.3220339,25.95721393,26.05582694,27.05389222]
	mean_ = np.mean(sample_list)
	median_ = np.median(sample_list)
	mode_ = stats.mode(sample_list)
	ptp_ = np.ptp(sample_list)
	var_ = np.var(sample_list)
	std_ = np.std(sample_list)
	#变异系数
	cv = std_/mean_
	#print(cv)
	#z-分数= (sample_list[0] - mean_)/std_　
	#通常来说，z-分数的绝对值大于3将视为异常。
	for i in sample_list:
		z_ = (i-mean_)/std_
		if abs(z_) >= 2:
			print(i)
			print(z_)
#f3()
#绘制箱形图
def f4():
	#创建箱形图
	#第一个参数为待绘制的定量数据
	#第二个参数为数据的文字说明
	df = pd.DataFrame()
	df["chengdu"] = [21.52034001,21.79019384,24.21732283,30.03171247,33.74211503,28.55923638,27.65825015,32.86470337,34.40272727,32.9387234,29.99272397,35.43910406,31.73243802,31.24047878,34.01241685,28.36865539,34.66860677,32.7688,26.70026933,27.66125494,24.11177474,23.53588907,31.43685756,29.79516423,31.09316038,34.60472805,31.95021645,34.11454102,30.18158568,34.77140335,31.07177814]
	df["qingdao"] = [15.89413835,13.68831169,19.65893869,20.31304348,20.99297677,16.28358209,12.39954853,24.81745609,24.21774633,23.93769799,20.261345,20.53729604,22.90031348,19.81587725,25.48322543,27.41579315,22.81654436,27.61574383,23.38324176,24.81985294,24.53971708,22.12964054,23.18892734,27.63699422,27.75397797,25.5522615,25.81109023,30.00713194,25.15123457,21.59790819,23.35667107]
	df["gexin"] = [26.43822222,28.96696945,31.18315617,30.97891691,38.82246513,30.60131291,24.46830844,39.71,45.22900365,33.67012987,38.44627532,44.73065693,35.98311524,26.8352799,34.79114602,34.39168911,43.17241379,39.9145745,36.65229977,39.96078431,32.87836186,27.71779572,26.59759319,38.42451155,31.75377468,35.0057929,12.54670185,27.75143678,38.71980676,37.0539643,29.8210084]
	df["chongqing"] = [13.4072406,13.54184277,18.06353791,17.90348525,26.4362851,18.90145673,18.3777336,26.06279863,21.98290598,22.30298273,22.78079009,34.21870504,32.44526084,28.27134725,29.38906752,25.44164038,25.78008552,28.2057735,29.27498177,22.50034364,19.02270663,19.31950845,21.67036626,23.75037258,23.20394737,25.25717064,24.98432175,21.71218616,17.42857143,17.24444444,19.93432369]
	#sample_list.sort()
	#print(sample_list)
	pyplot.boxplot(x=df.values, labels=df.columns)
	pyplot.title('sample_list')
	pyplot.show()
#f4()
def xiaocang():
	df = pd.DataFrame()
	df["shenyang"] = [19.92378991,20.83590209,21.45539033,24.80618557,24.68726592,21.70696721,20.03118908,40.8117284,29.4785324,30.16374269,27.76547842,32.03806228,28.92933204,30.04795205,29.06413302,25.23390895,27.03414634,29.77646188,29.6417694,32.83591837,26.89753773,27.0550113,25.25771812,43.76851852,45.3839838,34.45656309,36.19130435,32.38005391,25.76874562,27.61875946,36.6900149]
	df["fuzhou"] = [22.07413011,24.40799449,26.31743869,24.41049798,30.13067151,29.79459459,27.99559795,30.37627812,28.1247191,30.65859564,27.63344788,28.06382979,22.47103756,22.68720379,26.91033807,23.95550957,28.33881279,28.13559322,23.32695756,29.79497289,32.58329062,26.34346847,21.21699406,24.77887198,22.18015171,25.05386064,22.75037258,21.45003183,19.26235212,17.38855422,19.78757669]
	df["jinan"] = [20.69306931,24.91385768,26.3318649,27.79731744,28.09243697,27.04375497,24.45437616,32.35374928,27.86934023,27.68441065,26.081142,27.1611479,26.84087363,27.60592044,29.17692806,27.40770252,24.94520548,29.06202723,25.76773296,29.3253493,31.5565032,27.30453258,25.60095579,27.36899563,24.13309776,29.81290602,27.67776017,31.3220339,25.95721393,26.05582694,27.05389222]
	df["wuxian"] = [18.09878844,23.65551601,21.54422208,25.81736334,35.07685009,24.59774011,20.93253012,27.93609361,24.28371442,23.20494104,24.33699161,25.73291536,20.55404531,17.55749832,21.93634841,22.69747899,31.37279454,27.32783505,28.54803789,32.64411367,27.96465969,25.78309859,26.75254965,26.77008696,33.32310315,26.33208356,14.23538831,27.25259067,28.64576458,24.00381194,24.39644219]
	df["xian"] = [14.61831153,18.70952381,23.08450704,16.88,21.21291866,13.49579832,20.89486553,34.17349857,24.88082902,27.50389321,22.39637599,27.94131455,20.64948454,24.03950617,31.06378132,23.63409091,27.52920354,23.03908484,25.7983368,32.92307692,24.77878104,25.24300112,35.97849462,30.55519268,22.8207024,30.65610143,31.50766456,29.02294455,21.7045204,25.33403141,28.94577007]
	#sample_list.sort()
	#print(sample_list)
	pyplot.boxplot(x=df.values, labels=df.columns)
	pyplot.title('sample_list')
	pyplot.show()
xiaocang()
#济南仓测试
def sandiantu():
	#第一个参数为点的横坐标
	#第二个参数为点的纵坐标
	sample_list = [20.69306931,24.91385768,26.3318649,27.79731744,28.09243697,27.04375497,24.45437616,32.35374928,27.86934023,27.68441065,26.081142,27.1611479,26.84087363,27.60592044,29.17692806,27.40770252,24.94520548,29.06202723,25.76773296,29.3253493,31.5565032,27.30453258,25.60095579,27.36899563,24.13309776,29.81290602,27.67776017,31.3220339,25.95721393,26.05582694,27.05389222]
	mean_ = np.mean(sample_list)
	median_ = np.median(sample_list)
	mode_ = stats.mode(sample_list)
	ptp_ = np.ptp(sample_list)
	var_ = np.var(sample_list)
	std_ = np.std(sample_list)
	#变异系数
	cv_ = std_/mean_
	#print(cv_)
	#z-分数= (sample_list[0] - mean_)/std_　
	#通常来说，z-分数的绝对值大于3将视为异常。
	for i in sample_list:
		z_ = (i-mean_)/std_
		# if abs(z_) >= 2:
		# 	print(i)
		# 	print(z_)
	#print("mean=" +str(mean_) + ";median_=" + str(median_) + ";ptp = " + str(ptp_) + ";var="+str(var_) + ";std=" + str(std_) + ";cv= "+str(cv_))
	#pyplot.scatter([i for i in range(1,32)],sample_list)
	#pyplot.xlabel('date')
	#pyplot.ylabel('renxiao')
	#pyplot.title('sample_list:scatter')
	#pyplot.show()
	#用来正常显示中文标签
	pyplot.rcParams['font.sans-serif'] = ['SimHei'] 
	t = pyplot.boxplot(sample_list, labels=["测试"])
	#获取异常值
	#print(t)
	#print("异常值：" + str(t["fliers"][0].get_ydata()))
	pyplot.title('sample_list:boxplot')
	#上下界限
	for i in t["caps"]:
		pass
		#print(i.get_ydata())
	#Q1,Q3
	for i in t["boxes"]:
		pass
		#print(i.get_ydata())
	#中位线
	for i in t["medians"]:
		print(i.get_ydata())
	pyplot.show()
	#print(sample_list)
#sandiantu()
#济南仓测试
#resultEntity(warehouse,str(fliers_),str(jixian),str(Q1Q3),str(median)str(mean_),str(ptp_),str(var_),str(std_),str(cv_))
class resultEntity:
	warehouse = ""
	yichangzhi = ""
	jiexian = ""
	Q1Q3 = ""
	median = ""
	mean = ""
	ptp = ""
	var = ""
	std = ""
	cv = ""
	def __init__(self,warehouse_,yichangzhi_,jiexian_,Q1Q3_,median_,mean_,ptp_,var_,std_,cv_):
		self.warehouse = warehouse_
		self.yichangzhi = yichangzhi_
		self.jiexian = jiexian_
		self.Q1Q3 = Q1Q3_
		self.median = median_
		self.mean = mean_
		self.ptp = ptp_
		self.var = var_
		self.std = std_
		self.cv = cv_

#全局变量
def boxplot_(warehouse,sample_list,resultList):
	#用来正常显示中文标签
	pyplot.rcParams['font.sans-serif'] = ['SimHei'] 
	t = pyplot.boxplot(sample_list, labels=[warehouse])
	#获取异常值
	#print(t)
	fliers_ = t["fliers"][0].get_ydata()
	print("异常值：" + str(fliers_))
	pyplot.title('sample_list:boxplot')
	#上下界限
	print("上下界限：")
	jiexian = []
	for i in t["caps"]:
		#pass
		jiexian.append(i.get_ydata())
		print(i.get_ydata())
	#Q1,Q3
	print("Q1,Q3:")
	Q1Q3 = []
	for i in t["boxes"]:
		#pass
		Q1Q3.append(i.get_ydata())
		print(i.get_ydata())
	#中位线
	print("median:")
	median = []
	for i in t["medians"]:
		median.append(i.get_ydata())
		print(i.get_ydata())
	#pyplot.show()
	new_list = []
	for i in sample_list:
		if i in fliers_:
			continue
		new_list.append(i)

	mean_ = np.mean(sample_list)
	median_ = np.median(sample_list)
	mode_ = stats.mode(sample_list)
	ptp_ = np.ptp(sample_list)
	var_ = np.var(sample_list)
	std_ = np.std(sample_list)
	#变异系数
	cv_ = std_/mean_
	#print(cv_)
	#z-分数= (sample_list[0] - mean_)/std_　
	#通常来说，z-分数的绝对值大于3将视为异常。
	for i in sample_list:
		z_ = (i-mean_)/std_
		# if abs(z_) >= 2:
		# 	print(i)
		# 	print(z_)
	#print("mean=" +str(mean_) + ";median_=" + str(median_) + ";ptp = " + str(ptp_) + ";var="+str(var_) + ";std=" + str(std_) + ";cv= "+str(cv_))

	#输出
	resultList.append(resultEntity(warehouse,str(fliers_),str(jiexian),str(Q1Q3),str(median),str(mean_),str(ptp_),str(var_),str(std_),str(cv_)))
	if len(fliers_) < 1:
		if cv_ > 0.15:
			print("mean=" +str(mean_) + ";median_=" + str(median_) + ";ptp = " + str(ptp_) + ";var="+str(var_) + ";std=" + str(std_) + ";cv= "+str(cv_))

		print("THE END")
		return -1
	boxplot_(warehouse,new_list,resultList)
	print("end")
	return -1

def main():
	resultList = []
	catering_sale = 'd:/renxiao/renxiao_121.xlsx' #餐饮数据，含有其他属性
	data = pd.read_excel(catering_sale)
	dict_list = []
	for i,j in enumerate(data):
		if i == 0:
			continue
		dict_list.append({"warehouse":j,"values":data[j]})
	for i in dict_list:
		print(i["warehouse"])
		boxplot_(i["warehouse"],i["values"],resultList)
		#break
	#输出
	print("output")
	wb = xlwt.Workbook()
	ws = wb.add_sheet("result")

#resultEntity(warehouse,str(fliers_),str(jixian),str(Q1Q3),str(median)str(mean_),str(ptp_),str(var_),str(std_),str(cv_))
	colNames = ['warehouse','fliers_','jixian','Q1Q3','median','mean','ptp','var','std','cv']
	for index,col in enumerate(colNames):
		ws.write(0,index,col) 
	print(len(resultList))
	for k,i in enumerate(resultList):
		ws.write(k + 1,0,i.warehouse) 
		ws.write(k + 1,1,i.yichangzhi) 
		ws.write(k + 1,2,i.jiexian) 
		ws.write(k + 1,3,i.Q1Q3) 
		ws.write(k + 1,4,i.median) 
		ws.write(k + 1,5,i.mean) 
		ws.write(k + 1,6,i.ptp)  
		ws.write(k + 1,7,i.var) 
		ws.write(k + 1,8,i.std) 
		ws.write(k + 1,9,i.cv) 
	wb.save('result_121.xls')

	#sample_list = [20.69306931,24.91385768,26.3318649,27.79731744,28.09243697,27.04375497,24.45437616,32.35374928,27.86934023,27.68441065,26.081142,27.1611479,26.84087363,27.60592044,29.17692806,27.40770252,24.94520548,29.06202723,25.76773296,29.3253493,31.5565032,27.30453258,25.60095579,27.36899563,24.13309776,29.81290602,27.67776017,31.3220339,25.95721393,26.05582694,27.05389222]
	#boxplot_("",sample_list)
#main()
# a = resultEntity("warehouse","str(fliers_)","str(jiexian)","str(Q1Q3)","str(median)","str(mean_)","str(ptp_)","str(var_)","str(std_)","str(cv_)")
# t = []
# t.append(a)
# print(len(t))
from xlrd import open_workbook
from xlutils.copy import copy
# 打开文件
rb = open_workbook("d://1.xls")
# 复制
wb = copy(rb)
# 选取表单
# s = wb.get_sheet(0)
# # 写入数据
# s.write(0, 1, 'new data')
# 保存
wb.save('d://example.xls')