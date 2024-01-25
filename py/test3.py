import os
import json
# 输入文件夹路径
input_folder = '全市/'

# 输出文件夹路径
output_folder = '县级市'

def get_file(input_folder):
    for filename in os.listdir(input_folder):
        file="全市/"+filename
        with open(file, encoding="utf-8") as f:
            data = json.load(f)
            childrenNum=data["features"][0]["properties"]["childrenNum"]
            if childrenNum==0:
                k = open('县级市/'+filename, 'a', encoding='utf-8')
                k.write(str(data))
                k.close()