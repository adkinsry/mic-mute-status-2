from setuptools import setup, find_packages

setup(
    name='mic-mute-status',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A microphone mute status overlay application for Linux.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/mic-mute-status',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    entry_points={
        'console_scripts': [
            'mic-mute-status=mic_mute_status.mic_mute_status:main',
        ],
    },
    install_requires=[
        'PyGObject',
        'subprocess32',  # Add any other dependencies here
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: POSIX :: Linux',
    ],
    python_requires='>=3.6',
)