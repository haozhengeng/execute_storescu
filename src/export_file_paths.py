import os

def get_patient_folders(root_folder, output_file):
    """
    获取指定根文件夹下所有文件夹的路径，并将结果保存到本地文本文件中
    :param root_folder: 根文件夹路径
    :param output_file: 输出文本文件的路径
    :return: 包含文件夹路径的列表
    """
    patient_folders = []
    try:
        for item in os.listdir(root_folder):
            item_path = os.path.join(root_folder, item)
            if os.path.isdir(item_path):
                patient_folders.append(item_path)
        
        # 将文件夹路径写入文本文件
        with open(output_file, 'w', encoding='utf-8') as f:
            for folder in patient_folders:
                f.write(folder + '\n')
    except FileNotFoundError:
        print(f"指定的根文件夹 {root_folder} 未找到。")
    return patient_folders

if __name__ == "__main__":
    # 指定路径
    root_folder = '/media/tx-deepocean/Data/DICOMS/ct_nodule'
    output_file = '/home/tx-deepocean/Desktop/patient_folders.txt'
    get_patient_folders(root_folder, output_file)