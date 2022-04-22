import setuptools
from jupyter_packaging import create_cmdclass
from setuptools import setup
from {{cookiecutter.package_name}} import __version__


VERSION = __version__


def get_data_files():
    """Get the data files for the package."""
    data_files = [
        ("external_data/etc/jupyter/jupyter_server_config.d", "etc/jupyter/jupyter_server_config.d/", "*.json"),
    ]

    return data_files


cmdclass = create_cmdclass(data_files_spec=get_data_files())

setup_args = dict(
    author="{{cookiecutter.author_name}}",
    author_email='{{cookiecutter.author_email}}',
    name="{{cookiecutter.package_name}}",
    version=VERSION,
    description="{{cookiecutter.project_short_description}}",
    python_requires=">=3.6",
    packages=setuptools.find_packages(),
    install_requires=[
        "jupyter_server",
        "jinja2",
    ],
    extras_require={
        "test": ["pytest"],
    },
    include_package_data=True,
    cmdclass=cmdclass,
)

if __name__ == "__main__":
    setup(**setup_args)
