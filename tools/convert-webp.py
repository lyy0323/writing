import os
from PIL import Image
import glob


def find_max_webp_index(directory):
    # 查找目录下所有的.webp文件
    webp_files = glob.glob(os.path.join(directory, '*.webp'))
    # 提取文件名中的数字，并找到最大的一个
    max_index = 0
    for webp_file in webp_files:
        file_name = os.path.basename(webp_file)
        # 提取文件名中的数字部分
        digits = ''.join(filter(str.isdigit, file_name))
        if digits.isdigit() and len(digits) == 4:
            max_index = max(max_index, int(digits))
    return max_index


def convert_images_to_webp(source_dir, resize=True):
    max_index = find_max_webp_index(source_dir)
    # 获取目录下所有的png和jpg图片
    images = glob.glob(os.path.join(source_dir, '*.png')) + glob.glob(os.path.join(source_dir, '*.jpg'))

    for idx, image_path in enumerate(images):
        try:
            # 打开图片
            with Image.open(image_path) as img:
                # 获取图片的宽高
                width, height = img.size

                # 计算缩放比例
                if resize:
                    max_dimension = max(width, height)
                    if max_dimension > 1280:
                        scale = 1280 / max_dimension
                        new_width = int(width * scale)
                        new_height = int(height * scale)
                        img = img.resize((new_width, new_height), Image.ANTIALIAS)

                # 生成新的文件名
                base_name = os.path.basename(image_path)
                file_name, file_ext = os.path.splitext(base_name)
                new_file_name = f"{max_index + idx + 1:04d}.webp"

                # 保存为webp格式
                new_file_path = os.path.join(source_dir, new_file_name)
                img.save(new_file_path, 'WEBP')

                # 删除原始文件
                os.remove(image_path)
                print(f"Converted and deleted: {image_path}")

        except Exception as e:
            print(f"Error converting {image_path}: {e}")


if __name__ == '__main__':
    # 指定目录
    source_directory = '../assets/imgs/design'
    convert_images_to_webp(source_directory, resize=True)
