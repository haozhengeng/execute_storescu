import subprocess
import time

def execute_storescu_commands(file_path):
    try:
        # 打开包含 DICOM 图像路径的文本文件
        with open(file_path, 'r') as file:
            # 逐行读取文件
            for line in file:
                # 去除行尾的换行符
                dicom_path = line.strip()
                if dicom_path:
                    # 构建 storescu 命令
                    command = f"storescu -aet TXPACSBJ -aec TXPACS +sd +r -d -xv 127.0.0.1 11111 {dicom_path}"
                    try:
                        # 执行命令
                        subprocess.run(command, shell=True, check=True,  stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
                        print(f"成功执行命令: {command}")
                    except subprocess.CalledProcessError as e:
                        print(f"执行命令 {command} 时出错: {e}")
                    # 等待 30 秒
                    time.sleep(30)
    except FileNotFoundError:
        print(f"未找到文件: {file_path}")

if __name__ == "__main__":
    # 替换为包含 DICOM 图像路径的文本文件的实际路径
    text_file_path = "/home/tx-deepocean/Desktop/patient_folders.txt"
    execute_storescu_commands(text_file_path)