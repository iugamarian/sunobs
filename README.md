# sunobs


## Sun Observation System

This is the source code of [sunobs](http://sunobs.hackerspace.gr) web application
for sun observations.


## license
This software is licensed under the [GNU AFFERO GENERAL PUBLIC LICENSE](https://www.gnu.org/licenses/agpl-3.0.html).
For more information, read the file [COPYING](COPYING).


## contribute

Four easy steps:

### 1. Fork the repository on your account and clone it locally.

`git clone git@github.com:your_github_username/sunobs.git`

Pro Tip: For every feature/bug you develop create a different branch

### 2. Install python dependencies

On Fedora:

`yum install python-virtualenv python-pip`

On Debian:

`aptitude install python-virtualenv python-pip`

### 3. Build you virtualenv

```
virtualenv --no-site-packages env
source env/bin/activate
pip install -r requirements.txt
```

### 4. Run the damn thing

`cp local_settings.py-example local_settings.py`

Check if everything seems ok in this file, or fill any blank.

Initialization:

```
./manage.py syncdb
./manage.py migrate
./manage.py runserver
```

Run:

`http://localhost:8000`
