from distutils.core import setup  
setup(name='python-dash',  
      version='0.0.1',  
      description='Dashboad system base on python tornado django',  
      author='tony.zhang',  
      author_email='tony09@foxmail.com',  
      url='https://github.com/tony-zh/python-dash',  
      packages=['python-dash'],  
      package_dir={'python-dash':'pydash'},
      package_data={'python-dash':['*.*','pydash/*']}
)  
