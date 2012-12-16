senioritis
==========

Scrapes myedu to find out the easiest classes of a university by average GPA by
professor.

Motivated by a college senior who just wants his piece of paper and go work.

Installation
============

```
sudo pip install -r requirements.txt
rubygems install sass
git clone git@github.com:ngokevin/jingo-minify && python jingo-minify/setup.py install
sed -i 's/SASS_BIN = '.*'/SASS_BIN = $(watch sass)/' senioritis/settings/settings.py
```
