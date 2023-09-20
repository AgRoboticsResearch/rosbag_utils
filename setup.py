from setuptools import setup

setup(
    name='rosbagpy',
    version='0.0.1',
    description='a pip-installable rosbag python utlity package',
    license='Apache-2.0 license',
    packages=['rosbagpy'],
    author='Zhenghao Fei',
    author_email='zfei@zju.edu.cn',
    keywords=['rosbagpy'],
    url='https://github.com/AgRoboticsResearch/rosbag_utils',
    install_requires=['scipy', 'pycryptodomex', 'rosbag', 'gnupg'],
)