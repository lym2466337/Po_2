import os, yaml
# 默认获取根目录的方式： os.path.dirname(os.path.abspath(__file__)),将该方法放在根目录上，则可以无论项目在哪里打开，都能获取到项目的根目录
import root_path


# 调用该方法最终会返回一个 字典类型的 yml数据
def get_data(filename):
    file_path = root_path.path + os.sep + "Data" + os.sep + filename + ".yml"

    with open(file_path, "r") as f:
        return yaml.load(f)

    #第二种：
    # with open("./Data/"+file_name+".yml","r") as f:
    #     return yaml.load(f)