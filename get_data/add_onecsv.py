import pandas as pd
import glob
import os

# 获取当前工作目录
current_directory = os.getcwd()
print("current_directory",current_directory)
# 设置要合并的CSV文件的文件夹路径
folder_path = current_directory

# 使用glob库获取文件夹中所有以.csv结尾的文件
file_list = glob.glob(f'{folder_path}/*.csv')


print("file_list",file_list)
# 创建一个空的DataFrame来存储合并后的数据
combined_data = pd.DataFrame()

# 循环读取每个CSV文件并将其合并到combined_data中
for file in file_list:
    print(file)
    df = pd.read_csv(file)
    combined_data = pd.concat([combined_data, df], ignore_index=True)

# 将合并后的数据保存为一个新的CSV文件
combined_data.to_csv('combined.csv', index=False)

# 打印合并后的数据
print(combined_data)
