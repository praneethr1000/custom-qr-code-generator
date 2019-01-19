import pyqrcode
sample_code = pyqrcode.create('This is for qr code generation',
                           error='L'
)#error=l,m,q,h
sample_code.png('adv.png',
             scale=6,
             module_color=[255, 150, 30],
             background=[0, 0, 0])
sample_code.show()
