from setuptools import setup, find_packages

setup(
    name='nanodata2014',
    version='0.0.1dev',
    description='nanodata2014',
    author='Chia-Chi Chang, Jia-Wei Chen, Yin-Chen Liao, Willy Kuo',
    author_email='c3h3.tw@gmail.com, sk413025@gmail.com, qmalliao@gmail.com, waitingkuo0527@gmail.com',
    packages=find_packages(),
    package_data={'': ['*.coffee']},
    install_requires=["numpy",
                      "scipy",
                      "pandas",
                      "scikit-learn",
                      "pymongo"],
)
