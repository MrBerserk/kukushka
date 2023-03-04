import setuptools

with open('readme.md') as file:
    read_me_desc = file.read()

setuptools.setup(
    name='kukushka',
    version='0.1',
    author='Dimasik',
    author_email='mr.berserk228@mail.ru',
    description='Project_Kukushka',
    long_description=read_me_desc,
    long_description_content_type='text/markdown',
    url='https://github.com/MrBerserk/kukushka',
    packages=['kukushka'],
    #install_requires=['logging'],
    python_requires='>=3.6',
)