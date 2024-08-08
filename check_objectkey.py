# 导入适用于 TOS 的 SDK
import tos
import glog
# 创建 TOS 客户端对象

access_key='AKLTODQwNDcyNWQ0NzQ1NDI2NDk4MGEyNzVjMTIwNGJjNjA'
secret_key='Wm1JeFpUYzNaRGhoTWpRNU5EVXlOemt6WTJFek1UUXpZakZsWW1NMk1qQQ=='
endpoint='tos-cn-shanghai.volces.com'
region = 'cn-shanghai'
client = tos.TosClientV2(access_key, secret_key, endpoint, region)
# 指定要检查的对象名称和存储桶名称
object_name = 'ADC30L/data/trigger/4363CDEDA4E4DB1FDBA43239E5C541563B817B0420C8F2563569C724A00358A5/20240402/YR_M83_6_1712048567696210091/logs/YR-M83-6_20240402_082214/logs/canbus/canbus.log.INFO.123129.20240402.084113.491373'
bucket_name = 'gwm-adc-qa'

#check_object_key(access_key, secret_key, endpoint, region, object_name, bucket_name)

if not check_object_key(access_key, secret_key, endpoint, region, object_name, bucket_name):
    # 发送kafka错误消息
    return True





def check_object_key(ak,sk,endpoint,region,object_name,bucket_name):
    try:
        # try:
        # 使用 HeadObject 方法发送 HEAD 请求
        response = client.head_object(bucket=bucket_name, key=object_name)
        print("对象存在")
        return True
    except tos.exceptions.TosClientError as e:
        # 操作失败，捕获客户端异常，一般情况为非法请求参数或网络异常
        glog.info('fail with client error, message:{}, cause: {}'.format(e.message, e.cause))
        return False
    except tos.exceptions.TosServerError as e:
        # 操作失败，捕获服务端异常，可从返回信息中获取详细错误信息
        glog.info('fail with server error, code: {}'.format(e.code))
        # request id 可定位具体问题，强烈建议日志中保存
        glog.info('error with request id: {}'.format(e.request_id))
        glog.info('error with message: {}'.format(e.message))
        glog.info('error with http code: {}'.format(e.status_code))
        glog.info('error with ec: {}'.format(e.ec))
        glog.info('error with request url: {}'.format(e.request_url))
        return False
    except Exception as e:
        glog.info('fail with unknown error: {}'.format(e))
        return False
    
