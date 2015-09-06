from setuptools import setup


# Dynamically calculate the version based on pyperclip.VERSION.
setup(
    name='Xclipboard',
    version='1.1',
    url='https://github.com/adyezik/Xclipboard',
    author='Calvin(Martin)adyezik',
    author_email='adyezik@gmail.com',
    description=('simple python3 clipboard module based on tkinter croos-platform'),
    license='MIT',
    py_modules=['Xclipboard']
    keywords="gui tkinter test module keyboard copy paste clear clear xclipboard control",
    classifiers=[
       ' Classifier: Development Status :: 5 - Production/Stable'
        'Classifier: Environment :: Win32 (MS Windows)'
        'Classifier: Environment :: X11 Applications'
       ' Classifier: Environment :: MacOS X'
        'Classifier: Intended Audience :: Developers'
       ' Classifier: Operating System :: OS Independent'
    ],
)
