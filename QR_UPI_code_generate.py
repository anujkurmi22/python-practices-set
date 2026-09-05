# import sys, subprocess
# subprocess.check_call([sys.executable, "-m", "pip","install","Pillow","qrcode[pil]"])

import qrcode

upi_id = input("enter your upi id = ")
amount =int(input("enter amount for genenrate qr code : "))

#upi://pay?pa=UPI_ID&pn=NAME&am=Amount&cu=CURRENCY&tn=MESSAGE

#Defining the pyment url based on the upi id and the payment app
#you can modify  these URLs based on the payment app you went to support 

phonepe_url = f'upi://pay?pa={upi_id}&pn=Anujsingh&am={amount}&cu=INR'
paytm_url = f'upi://pay?pa{upi_id}&pn=Anujsingh&am={amount} &cu=INR'
google_pay_url = f'upi://pay?pa{upi_id}&pn=Anujsingh&am={amount}& cu= INR'

# #create QR code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

# save the qr code to image file (optional)
phonepe_qr.save('phonepe_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')
print('sahi qr baan gya hai ')

#disply