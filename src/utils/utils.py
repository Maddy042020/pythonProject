# Common headers
class Util (object):
  @staticmethod
  def common_headers_json():
    headers = {
        "Content-Type": "application/json"
    }
    return headers
  @staticmethod
  def common_headers_xml():
    headers = {
        "Content-Type": "application/xml"
    }
    return headers
  @staticmethod
  def common_header_put_delete_byauth():
    headers = {
        "Content-Type": "application/xml",
        "Authorization": "Basic YWRtaW46cGFzc3dvcmQxMjM=",
    }
    return headers

  def common_header_put_delete_bycookie(self,token):
    headers = {
        "Content-Type": "application/xml",
        "Cookie": "token="+str(token),
    }
    return headers
def read_csv_file(self):
   pass

def read_env_file(self):
  pass
