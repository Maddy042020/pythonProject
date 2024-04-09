#Keep the url

class API_Constants(object):


#def base_url():
#return "https://restful-booker.herokuapp.com"
 @staticmethod
 def create_booking():
    return "https://restful-booker.herokuapp.com/booking"
 @staticmethod
 def url_create_token():
    return "https://restful-booker.herokuapp.com/auth"
 @staticmethod
 def url_put_patch_delete(self, booking_id):
    return "https://restful-booker.herokuapp.com/booking/" + str (self.booking_id)

