#### Clean slate environment setup
Start by setting up a new spack instance (nothing is there yet)
```
git clone --depth 1 --recurse-submodules --shallow-submodules -b v0.18.1.4 https://github.com/C2SM/spack-c2sm.git
. spack-c2sm/setup-env.sh
python -m venv venv
source venv/bin/activate
pip list
```
-> we start empty, nothing in spack, nothing in python

#### User of the new package_b

Naive install process:
```
pip install -e package_b/
```

-> fails because not published package_a is a dependency.

-> if package_a was deployed somewhere (aka nexus), the next step would happen within the package_b install directly, we can emulate here:

```
pip install -e package_a
```

-> fails because geos is not present. And geos is not a python dependency, so pip can not resolve it. But your system needs it: here we spack


spack will download the dependencies we have specified in the package for our convenience:

#### Non python dependencices in spack
```
spack env create testenv package_a/install/spack.yaml
spack env activate --with-view testenv
spack install
```

#### Package A full install
(again because package_a is not published we do it manually)
```
pip install -e package_a
```
and we can run package a now (and it uses cartopy -> see plot)
```
python usage_a.py
```

#### Package B full install
```
pip install -e package_b
python usage_b.py
```

#### Open questions:
- how does package b know how to spack install package a dependencies without the yaml file if we only deploy on nexus?
- how do we deal with env variables?