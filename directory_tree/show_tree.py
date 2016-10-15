"""
show dir tree
date: 16/10/15
"""

import os


DIR_LIST = []


def collect_dir_info(dir_list, base_path='.'):
    """收集文件夹信息"""
    current_dir = base_path
    if os.path.isfile(path=current_dir):
        dir_list.append(current_dir)
        return

    dir_list.append(current_dir)

    for m_dir in os.listdir(path=current_dir):
        b_path = os.path.join(current_dir, m_dir)
        collect_dir_info(dir_list, b_path)


def print_tree(dir_list):
    """打印目录树"""
    space_base = "   "
    root = dir_list[0]
    print(root)

    for node in dir_list[1:]:
        root_distance = node.replace(root, "").count("/")
        print(space_base * (root_distance - 1) + "└── " + os.path.split(node)[1])


if __name__ == '__main__':

    import sys
    base_path = sys.argv[1]
    if base_path:
        collect_dir_info(DIR_LIST, base_path=base_path)
    else:
        collect_dir_info(DIR_LIST)

    print_tree(DIR_LIST)

