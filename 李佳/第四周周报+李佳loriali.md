### 下周计划
学习platEMO使用（班主任的小任务）   
继续机器学习   
python练习   
### 本周

实现流程    
1 计算预测点到已知类别属性的数据集中的每个点的距离   
2 距离按递增排序   
3 选取与预测点最近的K个点   
4 确定前K个点所属类别的出现概率    
5 返回概论最高的类别作为当前预测分类    

一、此处当有文本文件大量xxx    
二、处理数据为向量    
#准备数据：将图像转换为数据向量    
def img2vector(filename):    
    '''   
    将图像转换为向量   
    :param filename: 文件目录名   
    :return: 向量数组   
    '''    
    #创建向量    
    returnVect = zeros((1,1024))    
    #打开数据文件，读取每行内容    
    fr = open(filename)    
    for i in range(32):    
        #循环读取每一行    
        lineStr = fr.readline()   
        for j in range(32):   
            #将每行前32字符转成int存入向量    
            returnVect[0,32*i+j] = int(lineStr[j])   
    return returnVect     


测试函数    
testVector = img2vector("digits/testDigits/0_13.txt")    
    print(testVector[0,0:31])    
    print(testVector[0, 32:63])    

三、测试算法    
#手写数字识别系统测试代码    
def handwritingClassTest():      
    #样本数据的类标签列表     
    hwLabels = []     
    #样本数据文件列表     
    trainingFileList = os.listdir("digits/trainingDigits")      
    #得到文件行数      
    m = len(trainingFileList)      
    #初始化样本数据矩阵     
    trainingMat = zeros((m,1024))     
    #依次读取所有样本数据到数据矩阵     
    for i in range(m):    
        #提取文件名中的数字      
        fileNameStr = trainingFileList[i]     
        #去掉.txt       
        fileStr = fileNameStr.split('.')[0]      
        #获取第一个字符，即它是哪一个数字            
        classNumStr = int(fileStr.split('_')[0])       
        #保存标签                        
        hwLabels.append(classNumStr)           
        #将样本数据存入矩阵                                                        
        trainingMat[i,:] = img2vector('digits/trainingDigits/%s' %(fileNameStr))            
    #读取测试数据                                      
    testFileList = os.listdir('digits/testDigits')             
    #初始化错误率                  
    errorCount = 0.0                
    mTest = len(testFileList)                          
    errfile = []                 
    #循环测试每个测试数据文件            
    for i in range(mTest):               
        fileNameStr = testFileList[i]               
        fileStr = fileNameStr.split('.')[0]              
        classNumStr = int(fileStr.split('_')[0])              
        #提取数据向量             
        vectorUnderTest = img2vector('digits/testDigits/%s' %(fileNameStr))        
        #对数据文件进行分类           
        classifierResult = classify0(vectorUnderTest,trainingMat,hwLabels ,3)    #传值k=3            
        #输出k-近邻算法分类结果和真实的分类        
        print('the classifier came back with: %d,the real answer is：%d' %(classifierResult,classNumStr))         
        #判断k-近邻算法是否准确               
        if(classifierResult != classNumStr):          
            errorCount +=1.0                 
            errfile.append(fileNameStr)               
    print('\n the total number of errors is: %d' %(errorCount))          #错误的总数          
    print('错误的是:%s ;' %[i for i in errfile])                                       
    print('\n the total error rate is: %f' %(errorCount/float(mTest)))   #总错误率        


#不将这个目录下的文件载入矩阵中，而是使用classify0()函数测试该目录下的每个文件。         
#测试handwritingClassTest()函数:          
                  
    #开始时间                    
    start = time.perf_counter()             
    #测试handwritingClassTest()的输出结果             
    handwritingClassTest()          
    end = time.perf_counter()               
    print("运行耗时：%ds" %(end-start))             
             
#更改K值验算准确率得出最优k           
    
