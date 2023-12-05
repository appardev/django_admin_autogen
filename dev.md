## How to upload to PyPI

Installation

```shell
pip install twine
```

After you update the project, 

```shell
python setup.py sdist bdist_wheel
twine upload dist/* -u __token__ -p <pypi_api_token>
```