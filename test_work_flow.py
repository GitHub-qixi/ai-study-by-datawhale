import os
import platform
import time

def search_file_system(name: str, is_dir: bool = False) -> list:
    """
    在整个计算机系统中查找指定的文件或文件夹。
    
    Args:
        name (str): 要查找的文件名或文件夹名（支持大小写不敏感）。
        is_dir (bool): 如果为 True，则只查找文件夹；如果为 False，则只查找文件。
        
    Returns:
        list: 包含所有匹配项绝对路径的列表。
    """
    results = []
    name_lower = name.lower()
    
    # 获取系统根目录/盘符
    if platform.system() == "Windows":
        # Windows 下获取所有盘符 (如 C:\, D:\)
        drives = [f"{d}:\\" for d in "ABCDEFGHIJKLMNOPQRSTUVWXYZ" if os.path.exists(f"{d}:\\")]
    else:
        # Linux/Mac 下从根目录开始
        drives = ["/"]

    print(f"开始在 {len(drives)} 个驱动器/根目录下搜索: '{name}' ...")

    for drive in drives:
        _recursive_search(drive, name_lower, is_dir, results)
        
    return results

def _recursive_search(current_path: str, target_name_lower: str, is_dir: bool, results: list):
    """
    递归遍历目录进行搜索。
    
    Args:
        current_path (str): 当前遍历的路径。
        target_name_lower (str): 目标名称的小写形式。
        is_dir (bool): 是否只查找目录。
        results (list): 用于存储结果路径的列表。
    """
    try:
        with os.scandir(current_path) as entries:
            for entry in entries:
                try:
                    # 检查名称是否匹配（大小写不敏感）
                    if entry.name.lower() == target_name_lower:
                        if is_dir and entry.is_dir():
                            results.append(entry.path)
                        elif not is_dir and entry.is_file():
                            results.append(entry.path)
                    
                    # 如果是目录，则继续递归深入
                    if entry.is_dir():
                        _recursive_search(entry.path, target_name_lower, is_dir, results)
                except (PermissionError, OSError):
                    # 跳过没有权限访问或出错的目录
                    continue
    except (PermissionError, OSError):
        pass

if __name__ == "__main__":
    # 测试用例
    search_name = input("请输入要查找的文件或文件夹名: ")
    is_directory = input("是文件夹吗? (y/n): ").lower() == 'y'
    
    start_time = time.time()
    found_paths = search_file_system(search_name, is_directory)
    end_time = time.time()
    
    if found_paths:
        print(f"\n找到 {len(found_paths)} 个结果 (耗时: {end_time - start_time:.2f}秒):")
        for path in found_paths:
            print(f"- {path}")
    else:
        print(f"\n未找到名为 '{search_name}' 的{'文件夹' if is_directory else '文件'}。")
