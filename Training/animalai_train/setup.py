from setuptools import setup

setup(
    name='RoboGym',
    version='1.0.0',
    description='Robo Gym training tools',
    url='https://github.com/ahassanzadeh/RoboGym.git',
    author='Ali Hasasnzadeh',
    author_email='datascience.ali.ai@gmail.com',

    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6'
    ],

    packages=['robogym_train.trainers', 'robogym_train.trainers.bc', 'robogym_train.trainers.ppo'],  # Required
    zip_safe=False,

    install_requires=[
        'animalai>=1.0.5',
        'dopamine-rl',
        'tensorflow==1.14',
        'matplotlib',
        'Pillow>=4.2.1,<=5.4.1',
        'numpy>=1.13.3,<=1.14.5',
        'protobuf>=3.6,<3.7',
        'grpcio>=1.11.0,<1.12.0',
        'pyyaml>=5.1',
        'atari-py',
        'jsonpickle>=1.2',
        'docopt',
        'pypiwin32==223;platform_system=="Windows"'],
    python_requires=">=3.5,<3.8",
)
