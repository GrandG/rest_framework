.PHONY: install migrate run sphinx test

# 激活项目所用的虚拟环境后, 并 cd 到项目所在根目录

django = python "./manage.py"

deploy:
	$(django) makemigrations --settings=djangodvs.settings.production
	$(django) migrate --settings=djangodvs.settings.production
	echo "migrate done"

	$(django) collectstatic --settings=djangodvs.settings.production
	echo "collectstatic done"

install:
	python -m pip install -r "./requirements.txt"
	echo "pip install -r requirements.txt"

# nmake migrate app="project" m="0002_xxx"
migrate:
	$(django) makemigrations
	$(django) migrate $(a) $(m)
	echo "migrate done"

production: deploy
	echo "ONLY FOR TEST! Do not run in production environment."
	$(django) runserver --settings=djangodvs.settings.production --insecure

run:
	$(django) runserver

# nmake showmigrations app="project"
showmigrations:
	$(django) showmigrations $(a)

sphinx:
	sphinx-build -b html "./docs/source" "./docs/build"
	start docs/build/index.html
	echo "sphinx-build done"

test:
	$(django) test djangodvs.tests
	echo "test done"
