import requests
import os
import re


def download(domain_path, file_path, output_folder_path):
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    r = requests.get(domain_path + file_path)

    with open(output_folder_path + file_path, 'wb') as f:
        f.write(r.content)

    # Retrieve HTTP meta-data
    print('downloading: ' + file_path)
    print(r.status_code)
    # print(r.headers['content-type'])
    # print(r.encoding)
    return r.status_code


def atoi(text):
    return int(text) if text.isdigit() else text


def natural_keys(text):
    """
    自然排序法
    alist.sort(key=natural_keys) sorts in human order
    http://nedbatchelder.com/blog/200712/human_sorting.html
    (See Toothy's implementation in the comments)
    """
    return [atoi(c) for c in re.split('(\d+)', text)]


def list_file(parent_path, file_format):
    files = []
    # r=root, d=directories, f = files
    for r, d, f in os.walk(parent_path):
        for file in sorted(f, key=natural_keys):
            if '.' + file_format in file:
                files.append(os.path.join(file))
    # for f in files:
    #     print(f)
    return files


def write_txt(out_file_name, content):
    print(out_file_name)
    out_file = open(out_file_name, "w")
    out_file.write(content)
    out_file.close()


def write_file_list_to_txt(parent_path, file_format, txt_path):
    files = list_file(parent_path=parent_path, file_format=file_format)
    files_txt = ''
    for f in files[:-1]:
        files_txt += 'file \'' + f + '\'\n'
    files_txt += 'file \'' + files[-1] + '\''
    # print(files_txt)
    write_txt(out_file_name=txt_path, content=files_txt)

    # 以上程式與以下直接下cmd的效果相同
    # os.chdir(parent_path)
    # cmd1 = 'for i in `ls *.ts | sort -V`; do echo "file $i"; done >> mylist.txt'
    # os.system(cmd1)


def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    else:
        print("Can not delete the file as it doesn't exists: "+file_path)


def ffmpeg_merge(input_folder_path, output_file_name):
    """使用ffmpeg做影片合併"""
    os.chdir(input_folder_path)  # 換目錄
    # cmd範例：'ffmpeg -f concat -i mylist.txt -c copy -bsf:a aac_adtstoasc video.mp4'
    cmd2 = 'ffmpeg -f concat -i mylist.txt -c copy -bsf:a aac_adtstoasc ' + output_file_name
    os.system(cmd2)


def merge(video_format, input_folder_path, output_file_name):
    # https://superuser.com/questions/692990/use-ffmpeg-copy-codec-to-combine-ts-files-into-a-single-mp4
    write_file_list_to_txt(input_folder_path, video_format, input_folder_path + 'mylist.txt')
    ffmpeg_merge(input_folder_path=input_folder_path, output_file_name=output_file_name)
