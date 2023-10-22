# 为了有矩阵
import numpy
# 使用S函数
import scipy.special
import matplotlib.pyplot
%matplotlib inline

# 一开始的时候先搭建框架
class neuralNetwork:
    # 定义输入层隐藏层输出层,还有学习率
    def __init__(self, inputnodes, hiddennodes, outputnodes, learningrate):
        # 定义每层的节点
        self.inodes = inputnodes
        self.hnodes = hiddennodes
        self.onodes = outputnodes
        # 链接权重矩阵
        # self.wih = (numpy.random.rand(self.hnodes,self.inodes)-0.5)
        # self.who = (numpy.random.rand(self.onodes,self.hnodes)-0.5)
        # 但是用正态分布可能更好吧,0.0是正态分布的中心
        self.wih = numpy.random.normal(0.0, pow(self.hnodes, -0.5), (self.hnodes, self.inodes))
        self.who = numpy.random.normal(0.0, pow(self.onodes, -0.5), (self.onodes, self.hnodes))
        # 学习率
        self.lr = learningrate

        # 定义一个S函数
        self.activation_function = lambda x: scipy.special.expit(x)
        pass

    # 用来训练
    def train(self, inputs_list, targets_list):
        inputs = numpy.array(inputs_list, ndmin=2).T
        targets = numpy.array(targets_list, ndmin=2).T

        hidden_inputs = numpy.dot(self.wih, inputs)
        hidden_outputs = self.activation_function(hidden_inputs)

        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)

        # 计算误差值，直接使用矩阵的减法
        output_errors = targets - final_outputs
        # 通过之前的表达式计算出隐藏层的误差值
        hidden_errors = numpy.dot(self.who.T, output_errors)

        # 更新权重
        self.who += self.lr * numpy.dot((output_errors * final_outputs * (1.0 - final_outputs)),
                                        numpy.transpose(hidden_outputs))
        self.wih += self.lr * numpy.dot((hidden_errors * hidden_outputs * (1.0 - hidden_outputs)),
                                        numpy.transpose(inputs))
        pass

    # 查询？？
    def query(self, inputs_list):
        # 把输入列表转换为矩阵
        inputs = numpy.array(inputs_list, ndmin=2).T  # .T转置,确保行列数相等
        # 将链接权重与输入矩阵点乘
        hidden_inputs = numpy.dot(self.wih, inputs)
        # 使用S函数，将信号传入到了隐藏层
        hidden_outputs = self.activation_function(hidden_inputs)
        # 隐藏层到输出层和之前的一样
        final_inputs = numpy.dot(self.who, hidden_outputs)
        final_outputs = self.activation_function(final_inputs)
        return final_outputs


# 定义每一层的节点数量
input_nodes = 784
hidden_nodes = 200
output_nodes = 10
# 学习率=0.3
learning_rate = 0.2
# 把这些数据传入neuralNetwork
n = neuralNetwork(input_nodes, hidden_nodes, output_nodes, learning_rate)

# 打开训练集

training_data_file = open("E:\mnist_dataset\mnist_train.csv", 'r')
training_data_list = training_data_file.readlines()
training_data_file.close()

# 分开多次训练可以节省时间
epochs = 7
for e in range(epochs):
    for record in training_data_list:
        # 注意这里应该遍历的是training_data_list，而不是training_data_file
        all_values = record.split(',')
        inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99 + 0.01)
        targets = numpy.zeros(output_nodes) + 0.01
        targets[int(all_values[0])] = 0.99
        # 使用train函数
        n.train(inputs, targets)
        pass
pass
# 检测，和训练差不多
test_data_file = open("E:\mnist_dataset\mnist_test.csv", 'r')
test_data_1ist = test_data_file.readlines()
test_data_file.close()
scorecard = []
for record in test_data_1ist:
    all_values = record.split(',')
    correct_label = int(all_values[0])
    # print(correct_label,'correct label')
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99 + 0.01)
    outputs = n.query(inputs)
    label = numpy.argmax(outputs)
    print(label, "network's answer")
    if (label == correct_label):
        scorecard.append(1)
    else:
        scorecard.append(0)
        pass
    pass
# 计算正确率
scorecard = []
for record in test_data_1ist:
    all_values = record.split(',')
    correct_label = int(all_values[0])
    print(correct_label, 'correct label')
    inputs = (numpy.asfarray(all_values[1:]) / 255.0 * 0.99 + 0.01)
    outputs = n.query(inputs)
    label = numpy.argmax(outputs)
    print(label, "network's answer")
    if (label == correct_label):
        scorecard.append(1)
    if (label != correct_label):
        scorecard.append(0)
        pass
    pass

scorecard_array = numpy.asarray(scorecard)
print('performance = ', scorecard_array.sum() / scorecard_array.size)
