import requests
import json
import csv

# 指定CSV文件名
csv_filename = 'data_2_9.csv'

with open(csv_filename, 'a', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        # 写入CSV文件的表头
        csv_writer.writerow(['Date', 'Group'])
for i in range(31):
     
    # 指定URL
    # url = 'https://www.services-rte.com/cms/open_data/v1/actual_generation_by_group?date=' + str(i) + '%2F3%2F2023&unit_eic_code=17W0000014455651'

    url = 'https://www.services-rte.com/cms/open_data/v1/actual_generation_by_group?date=' + str(i) + '%2F09%2F2023&unit_eic_code=17W000001445567Y'
    # 发送GET请求来获取数据
    response = requests.get(url)

    # 检查响应是否成功
    if response.status_code == 200:
        # 解析JSON数据
        data = response.json()

        # 提取日期和组数据
        values = data['values']

        

        with open(csv_filename, 'a', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)

            # 写入数据行
            for item in values:
                date = item['date']
                group = item['group']
                csv_writer.writerow([date, group])

        print(f"数据已保存到 {csv_filename}")
    else:
        print("请求失败，状态码：", response.status_code)


print("all is fini")