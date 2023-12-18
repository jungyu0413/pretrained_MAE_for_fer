import os
import shutil
import glob

paths = ['/workspace/dataset/Casia-Webface/casia_webface',
     #   '/workspace/dataset/CelebA_aligned',
        '/workspace/dataset/IMDB_crop']
save_path = '/workspace/dataset/netease/train'
error_path = []
for idx, path in enumerate(paths):
    path_name = path.split('/')[-1]
    all_path = os.listdir(path)
    for pidx, each_jpg in enumerate(all_path):
        try:
            shutil.copytree(os.path.join(path, each_jpg), os.path.join(save_path, f"{path_name}_"+each_jpg))
            print((pidx/len(all_path))*100)
        except:
            error_path.append(each_jpg)
            
print(error_path)