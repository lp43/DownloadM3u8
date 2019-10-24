import Util

print('Beginning file download with requests')

is_single_video = False
download_video_format = 'ts'

server_folder_path = \
    'https://xxxxxx.com/xxxx.m3u8/'
server_file_name = 'xxx.ts'  # ts僅有單一檔時才替換

local_folder_path = '/Users/xxx/dwhelper/2.1/'
local_file_name = 'merge.mp4'  # 不可以有.或其它特殊字元

for num in range(1, 2 if is_single_video is True else 500):
    if not is_single_video:
        # print('if not is_single_video')
        server_file_name = 'seg-' + str(num) + '-v1-a1.ts'
    status = Util.download(server_folder_path, server_file_name, local_folder_path)
    if status == 404:
        Util.delete_file(local_folder_path + server_file_name)
        break

Util.merge(video_format=download_video_format, input_folder_path=local_folder_path, output_file_name=local_file_name)

print('File download and merge success!!')
