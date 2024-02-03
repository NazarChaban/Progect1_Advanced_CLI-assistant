from setuptools import setup, find_namespace_packages

setup(
    name='console_assistant',
    version='1.0',
    description='console_assistant',
    url='https://github.com/Vivern0/Progect1_Advanced_CLI-assistant.git',
    author='P.A.N.D.A.M',
    license='MIT',
    packages=find_namespace_packages(),
    install_requires=['prettytable', 'prompt_toolkit'],
    entry_points={'console_scripts': ['assistant = src.main:main']}
)

