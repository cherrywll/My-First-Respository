# My-First-Respositorydef f1():
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
