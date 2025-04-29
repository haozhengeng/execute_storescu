# DICOM文件路径导出与发送工具

包含两个Python脚本：
1. `export_file_paths.py` - 导出指定目录下所有文件的绝对路径
2. `send_to_pacs.py` - 使用storescu发送DICOM文件到PACS节点

## 环境要求
- Python 3.6+
- 已安装DCMTK的storescu并添加到系统PATH

## 脚本1：文件路径导出器

### 功能特点
- 递归遍历子目录
- 支持所有文件类型
- 生成带时间戳的文本文件
- 简易进度显示

### 使用方法
```bash
python3 export_file_paths.py
```

## 脚本2：DICOM发送器

### 功能特点
- 多线程发送
- 成功/失败记录
- 可配置PACS参数
- 自动跳过非DICOM文件

### 使用方法
```bash
python3 send_to_pacs.py
```


### 重要说明
- 确保storescu已正确配置PACS连接参数
- 大数据集发送时可能需要调整系统文件句柄限制
- 生产环境使用前请先用小数据集测试
- 建议通过PACS存储确认功能验证发送结果