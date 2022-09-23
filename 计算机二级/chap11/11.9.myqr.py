from MyQR import myqr
words=['a' ]
import os
version, level, qr_name = myqr.run(
	words,
    version=1,
    level='H',
    picture=None,
    colorized=False,
    contrast=1.0,
    brightness=1.0,
    save_name='test.jpg',
    save_dir=os.getcwd()
	)
