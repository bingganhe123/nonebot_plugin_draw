
from setuptools import setup, find_packages

setup(
    name = "nonebot_plugin_draw",
    version = "0.1.0",
    description = "draw lots",
    license = "MIT Licence",

    url = "https://github.com/bingganhe123/nonebot_plugin_draw",
    author = "bingganhe123",
    author_email = "3143799170@qq.com",

    packages = find_packages(),
    include_package_data = True,
    python_requires='>=3.9, <4',
    zip_safe = False,
    install_requires = [
        'nonebot2>=2.0.0b1']
)