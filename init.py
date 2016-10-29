# -*- coding = utf-8 -*-
#As a normal person, I use coding: utf-8



from qiniu import Auth, put_file, etag, urlsafe_base64_encode
import qiniu.config
import ConfigParser
import string, os, sys

reload(sys)
sys.setdefaultencoding('utf8')

cf = ConfigParser.ConfigParser()

cf.read("configuration.conf")
#return all section
secs = cf.sections()
print 'sections: ', secs

#get the keys from the configuration file
access_key = cf.get("key","access_key")
secret_key = cf.get("key","secret_key")
#get the bucket name from the file
bucket_name = cf.get("bucket","bucket_name")

#build the object to verify right
q = Auth(access_key, secret_key)




print "Please drag the picture you want to upload:"

#要上传文件的本地路径

for path in sys.argv[1:]:
    localfile = path
    key = path.split(".")[0]
    # 生成上传 Token，可以指定过期时间等
    token = q.upload_token(bucket_name, key, 3600)
    ret, info = put_file(token, key, localfile)
    print(str(info))
    assert ret['key'] == key
    assert ret['hash'] == etag(localfile)


