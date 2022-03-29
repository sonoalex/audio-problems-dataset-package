from setuptools import setup, find_packages


setup(
    name='audio_problems_dataset',
    version='0.4',
    license='CC',
    author="Alex Albas",
    author_email='alex.albas01@estudiant.upf.edu',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='',
    keywords='audio-problems dataset',
    install_requires=[
          'gdown',
      ],

)