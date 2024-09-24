# Doxly

```sh
( cd src; python -m doxly -i ~/tmp/build/dokit-gcc-6.6.3-debug/doc/xml/ -t docusaurs -o out [-h] )
# or
pipx run --no-cache --spec . doxly -i ~/tmp/build/dokit-gcc-6.6.3-debug/doc/xml/ -t docusaurus -o out [-h]
```

```sh
python -m unittest discover -v
# or
coverage run -m unittest discover && coverage report
coverage html
```
