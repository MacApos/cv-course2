import numpy as np
import shutil
import os

execution_path = os.getcwd()
base_path = os.path.join(execution_path, 'image-dataset')
raw_no_of_files = {}
cls_1 = 'horse'
cls_2 = 'lion'
train_ratio = 0.7
valid_ratio = 0.2
classes = [cls_1, cls_2]

# for dir in os.listdir(base_path):
#     path = os.path.join(base_path, dir)
#     for idx, name in enumerate(os.listdir(path)):
#         extension = name.split('.')[-1]
#         new_name = f'img_{idx + 1}.{extension}'
#         src = os.path.join(path, name)
#         dst = os.path.join(path, new_name)
#         if not os.path.exists(os.path.join(path, new_name)):
#             os.rename(src=src, dst=dst)

for dir in classes:
    raw_no_of_files[dir] = len(os.listdir(os.path.join(base_path, dir)))

data_dir = r'F:\PycharmProjects\cv-course2\06_classification\image'

if not os.path.exists(data_dir):
    os.makedirs(data_dir)

train_dir = os.path.join(data_dir, 'train')
valid_dir = os.path.join(data_dir, 'valid')
test_dir = os.path.join(data_dir, 'test')

train_cls_1_dir = os.path.join(train_dir, cls_1)
valid_cls_1_dir = os.path.join(valid_dir, cls_1)
test_cls_1_dir = os.path.join(test_dir, cls_1)

train_cls_2_dir = os.path.join(train_dir, cls_2)
valid_cls_2_dir = os.path.join(valid_dir, cls_2)
test_cls_2_dir = os.path.join(test_dir, cls_2)

for dir in (train_dir, valid_dir, test_dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

for dir in (train_cls_1_dir, valid_cls_1_dir, test_cls_1_dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

for dir in (train_cls_2_dir, valid_cls_2_dir, test_cls_2_dir):
    if not os.path.exists(dir):
        os.makedirs(dir)

cls_1_names = os.listdir(os.path.join(base_path, cls_1))

cls_2_names = os.listdir(os.path.join(base_path, cls_2))

cls_1_names = [name for name in cls_1_names if name.split('.')[-1].lower() in ['jpg', 'png', 'jpeg']]
cls_2_names = [name for name in cls_2_names if name.split('.')[-1].lower() in ['jpg', 'png', 'jpeg']]


np.random.shuffle(cls_1_names)
np.random.shuffle(cls_2_names)

size = min(len(cls_1_names), len(cls_2_names))

train_size = int(train_ratio*size)
valid_size = train_size + int(valid_ratio*size)

for idx, name in enumerate(cls_1_names[:train_size]):
    if len(os.listdir(train_cls_1_dir)) < train_size:
        src = os.path.join(base_path, cls_1, name)
        dst = os.path.join(train_cls_1_dir, name)
        shutil.copyfile(src, dst)

for idx, name in enumerate(cls_1_names[train_size:valid_size]):
    if len(os.listdir(valid_cls_1_dir)) < valid_size-train_size:
        src = os.path.join(base_path, cls_1, name)
        dst = os.path.join(valid_cls_1_dir, name)
        shutil.copyfile(src, dst)

for idx, name in enumerate(cls_1_names[valid_size:]):
    if len(os.listdir(test_cls_1_dir)) < len(cls_1_names)-valid_size:
        src = os.path.join(base_path, cls_1, name)
        dst = os.path.join(test_cls_1_dir, name)
        shutil.copyfile(src, dst)

for idx, name in enumerate(cls_2_names[:train_size]):
    if len(os.listdir(train_cls_2_dir)) < train_size:
        src = os.path.join(base_path, cls_2, name)
        dst = os.path.join(train_cls_2_dir, name)
        shutil.copyfile(src, dst)

for idx, name in enumerate(cls_2_names[train_size:valid_size]):
    if len(os.listdir(valid_cls_2_dir)) < valid_size-train_size:
        src = os.path.join(base_path, cls_2, name)
        dst = os.path.join(valid_cls_2_dir, name)
        shutil.copyfile(src, dst)

for idx, name in enumerate(cls_2_names[valid_size:]):
    if len(os.listdir(test_cls_2_dir)) < len(cls_2_names)-valid_size:
        src = os.path.join(base_path, cls_2, name)
        dst = os.path.join(test_cls_2_dir, name)
        shutil.copyfile(src, dst)


print(f'Liczba obrazów w klasie {cls_1} w zbiorze treningowym: {len(os.listdir(train_cls_1_dir))}')
print(f'Liczba obrazów w klasie {cls_1} w zbiorze walidacyjnym: {len(os.listdir(valid_cls_1_dir))}')
print(f'Liczba obrazów w klasie {cls_1} w zbiorze testowym: {len(os.listdir(test_cls_1_dir))}')
print(f'Liczba obrazów w klasie {cls_2} w zbiorze treningowym: {len(os.listdir(train_cls_2_dir))}')
print(f'Liczba obrazów w klasie {cls_2} w zbiorze walidacyjnym: {len(os.listdir(valid_cls_2_dir))}')
print(f'Liczba obrazów w klasie {cls_2} w zbiorze testowym: {len(os.listdir(test_cls_2_dir))}')