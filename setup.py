from setuptools import setup

setup(
    name='urdf_to_dh',
    version='0.0.1',
    description='A example Python package',
    url='https://github.com/onekk/urdf_to_dh',
    author='andy',
    author_email='andy.mcevoy@sslmda.com',
    license='MIT',
    packages=['urdf_to_dh'],
    install_requires=['setuptools',
                      'anytree',
                      'numpy',
                      'pandas',
                      'tabulate'
                      ],

    classifiers=[
        'Development Status :: 1 - Planning',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.11',
    ],
)
