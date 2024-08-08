import os
import tos


ak = 'AKLTODQwNDcyNWQ0NzQ1NDI2NDk4MGEyNzVjMTIwNGJjNjA'
sk = 'Wm1JeFpUYzNaRGhoTWpRNU5EVXlOemt6WTJFek1UUXpZakZsWW1NMk1qQQ=='
endpoint = "tos-cn-shanghai.volces.com"
region = "cn-shanghai"
bucket_name = "gwm-adc-qa"
# 本地解析后文件夹的路径，文件夹名称为bag包名称
try:
    client = tos.TosClientV2(ak, sk, endpoint, region)
    #pre 是桶中的前缀，不带文件夹名称
    pre = 'test/'
    convert_bagfile_name = 'YR-convert-bagname'
    prefix = pre + convert_bagfile_name + '/'

    def upload_dir(root_dir, prefix):
        list = os.listdir(root_dir)
        for i in list:
            path = os.path.join(root_dir, i)
            object_key = os.path.join(prefix, i)
            if os.path.isdir(path):
                upload_dir(path,prefix + i + '/')

            if os.path.isfile(path):
                client.put_object_from_file(bucket_name, object_key , path)
                print(path)
                print(prefix)


    upload_dir(file_dir, prefix)

except tos.exceptions.TosClientError as e:
    # 操作失败，捕获客户端异常，一般情况为非法请求参数或网络异常
    print('fail with client error, message:{}, cause: {}'.format(e.message, e.cause))
except tos.exceptions.TosServerError as e:
    # 操作失败，捕获服务端异常，可从返回信息中获取详细错误信息
    print('fail with server error, code: {}'.format(e.code))
    # request id 可定位具体问题，强烈建议日志中保存
    print('error with request id: {}'.format(e.request_id))
    print('error with message: {}'.format(e.message))
    print('error with http code: {}'.format(e.status_code))
    print('error with ec: {}'.format(e.ec))
    print('error with request url: {}'.format(e.request_url))
except Exception as e:
    print('fail with unknown error: {}'.format(e))
