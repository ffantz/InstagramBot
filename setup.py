# import setup function from
# python distribution utilities
from distutils.core import setup

# Calling the setup function
setup(
      name = 'InstagramBot',
      version = '1.0.0',
      py_modules = ['secrets','InstagramBot','selenium','time'],
      author ='Fantz',
      author_email = 'flavioluzio22@gmail.com',
      url = 'https://instagram.com/ffantz',
      description = 'A simple bot to check who you follow on Instagram that doesn\'t follow you back',
      keywords='users instagram not following',
)