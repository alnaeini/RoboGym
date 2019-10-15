from setuptools import setup

setup(
    name='Roby',
    version='1.0.5',
    description='RoboGym Required Packages',
    url='https://github.com/beyretb/AnimalAI-Olympics',
    author='Ali Hassanzadeh',
    author_email='datascience.ai.ali@gmail.com',

    classifiers=[
        'Intended Audience :: Developers',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python :: 3.6'
    ],

    packages=['RoboGym.envs', 'RoboGym.envs.gym', 'RoboGym.communicator_objects'],  # Required
    zip_safe=False,

    install_requires=[
        'Pillow>=4.2.1,<=5.4.1',
        'numpy>=1.13.3,<=1.14.5',
        'protobuf>=3.6,<3.7',
        'grpcio>=1.11.0,<1.12.0',
        'pyyaml>=5.1',
        'jsonpickle>=1.2',
        'gym'],
    python_requires=">=3.5,<3.8",
)
