from setuptools import setup

package_name = 'ros2_pkg'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    entry_points={
        'console_scripts': [
            'number_publisher = ros2_pkg.publisher:main',
            'number_subscriber = ros2_pkg.subscriber:main',
        ],
    },
)
