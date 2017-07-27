import hmac

password = "4441f63125284a43de6e113a7e39bd35"
while True:
    user_imput = str(input("Insert password: "))
    print user_input
    my_hash = hmac.new(user-input).hexdigest()
    if my_hash == password:
        print "točno"
        break


"""
import hashlib
import hmac

KEY = "secret"
MESSAGE = "Message"
result = hmac.new(KEY, MESSAGE, hashlib.sha256).hexdigest()
print result # aa747c502a898200f9e4fa21bac68136f886a0e27aec70ba06daf2e2a5cb5597
"""