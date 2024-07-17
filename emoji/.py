import os
import json

def generate_json_structure(base_url):
    result = {}
    
    for root, dirs, files in os.walk("."):
        if root == ".":
            for dir_name in dirs:
                dir_path = os.path.join(root, dir_name)
                result[dir_name] = {
                    "type": "image",
                    "container": []
                }
                
                for file_name in os.listdir(dir_path):
                    file_path = os.path.join(dir_path, file_name)
                    if os.path.isfile(file_path):
                        file_name_no_ext = os.path.splitext(file_name)[0]
                        result[dir_name]["container"].append({
                            "icon": f"<img src=\"{base_url}/{dir_name}/{file_name}\">",
                            "text": file_name_no_ext
                        })

    return result

base_url = "https://storage.enltc.pages.dev/emoji"
json_structure = generate_json_structure(base_url)

# 将json_structure格式化为JSON字符串
json_str = json.dumps(json_structure, ensure_ascii=False, indent=4)

# 将container中的内容改为单行
def single_line_container(json_str):
    import re
    pattern = re.compile(r'(\{\s*"icon":.*?"text":.*?\},?)\s*', re.DOTALL)
    return pattern.sub(lambda m: m.group(1).replace('\n', '').replace('  ', ''), json_str)

# 将改好的JSON字符串写入文件
formatted_json_str = single_line_container(json_str)

with open("emoji.json", "w", encoding="utf-8") as f:
    f.write(formatted_json_str)

print("JSON结构已成功写入emoji.json文件")