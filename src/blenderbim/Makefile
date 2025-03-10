# BlenderBIM Add-on - OpenBIM Blender Add-on
# Copyright (C) 2020, 2021 Dion Moult <dion@thinkmoult.com>
#
# This file is part of BlenderBIM Add-on.
#
# BlenderBIM Add-on is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# BlenderBIM Add-on is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with BlenderBIM Add-on.  If not, see <http://www.gnu.org/licenses/>.

VERSION:=`date '+%y%m%d'`
PYVERSION:=py37

ifeq ($(PYVERSION), py37)
PYLIBDIR:=python3.7
PYNUMBER:=37
endif
ifeq ($(PYVERSION), py39)
PYLIBDIR:=python3.9
PYNUMBER:=39
endif

ifeq ($(PLATFORM), linux)
ifeq ($(PYVERSION), py37)
HPPFCL_URL:=https://anaconda.org/conda-forge/hpp-fcl/1.7.5/download/linux-64/hpp-fcl-1.7.5-py37h5f1835d_0.tar.bz2
EIGENPY_URL:=https://anaconda.org/conda-forge/eigenpy/2.6.5/download/linux-64/eigenpy-2.6.5-py37h95e2c48_0.tar.bz2
BOOST_URL:=https://anaconda.org/conda-forge/boost/1.74.0/download/linux-64/boost-1.74.0-py37h0379df6_3.tar.bz2
LXML_URL:=https://files.pythonhosted.org/packages/30/c0/d0526314971fc661b083ab135747dc68446a3022686da8c16d25fcf6ef07/lxml-4.6.3-cp37-cp37m-manylinux2014_x86_64.whl
endif
ifeq ($(PYVERSION), py39)
HPPFCL_URL:=https://anaconda.org/conda-forge/hpp-fcl/1.7.5/download/linux-64/hpp-fcl-1.7.5-py39hbcdfc36_0.tar.bz2
EIGENPY_URL:=https://anaconda.org/conda-forge/eigenpy/2.6.5/download/linux-64/eigenpy-2.6.5-py39h5aed9d1_0.tar.bz2
BOOST_URL:=https://anaconda.org/conda-forge/boost/1.74.0/download/linux-64/boost-1.74.0-py39h5472131_3.tar.bz2
LXML_URL:=https://files.pythonhosted.org/packages/19/d9/a69c6aff5673554df48120565a14a50eaa41d29ae03b02faa0b023666318/lxml-4.6.3-cp39-cp39-manylinux2014_x86_64.whl
endif
ASSIMP_URL:=https://anaconda.org/conda-forge/assimp/5.0.1/download/linux-64/assimp-5.0.1-hedfc422_6.tar.bz2
OCTOMAP_URL:=https://anaconda.org/conda-forge/octomap/1.9.7/download/linux-64/octomap-1.9.7-h4bd325d_0.tar.bz2
ZLIB_URL:=https://anaconda.org/conda-forge/zlib/1.2.11/download/linux-64/zlib-1.2.11-h516909a_1010.tar.bz2
endif

ifeq ($(PLATFORM), macos)
ifeq ($(PYVERSION), py37)
HPPFCL_URL:=https://anaconda.org/conda-forge/hpp-fcl/1.7.5/download/osx-64/hpp-fcl-1.7.5-py37h2d7f23a_0.tar.bz2
EIGENPY_URL:=https://anaconda.org/conda-forge/eigenpy/2.6.5/download/osx-64/eigenpy-2.6.5-py37h0695097_0.tar.bz2
BOOST_URL:=https://anaconda.org/conda-forge/boost/1.74.0/download/osx-64/boost-1.74.0-py37hd79e0ac_3.tar.bz2
LXML_URL:=https://files.pythonhosted.org/packages/1e/3e/f0abc15d5dac50939bccc589aae336d5ead4c72e7ad1039a2e0f3630ea92/lxml-4.6.3-cp37-cp37m-macosx_10_9_x86_64.whl
endif
ifeq ($(PYVERSION), py39)
HPPFCL_URL:=https://anaconda.org/conda-forge/hpp-fcl/1.7.5/download/osx-64/hpp-fcl-1.7.5-py39h1e32b98_0.tar.bz2
EIGENPY_URL:=https://anaconda.org/conda-forge/eigenpy/2.6.5/download/osx-64/eigenpy-2.6.5-py39h5405915_0.tar.bz2
BOOST_URL:=https://anaconda.org/conda-forge/boost/1.74.0/download/osx-64/boost-1.74.0-py39ha641261_3.tar.bz2
LXML_URL:=https://files.pythonhosted.org/packages/b8/74/a71f7ad72e8db54ce899efab84507b801660750cbbfa6a39e6717557d36a/lxml-4.6.3-cp39-cp39-macosx_10_9_x86_64.whl
endif
ASSIMP_URL:=https://anaconda.org/conda-forge/assimp/5.0.1/download/osx-64/assimp-5.0.1-h1224e73_6.tar.bz2
OCTOMAP_URL:=https://anaconda.org/conda-forge/octomap/1.9.7/download/osx-64/octomap-1.9.7-h940c156_0.tar.bz2
ZLIB_URL:=https://anaconda.org/conda-forge/zlib/1.2.11/download/osx-64/zlib-1.2.11-h7795811_1010.tar.bz2
endif

ifeq ($(PLATFORM), win)
ifeq ($(PYVERSION), py37)
HPPFCL_URL:=https://anaconda.org/conda-forge/hpp-fcl/1.7.5/download/win-64/hpp-fcl-1.7.5-py37h839d6b1_0.tar.bz2
EIGENPY_URL:=https://anaconda.org/conda-forge/eigenpy/2.6.5/download/win-64/eigenpy-2.6.5-py37h2c32e34_0.tar.bz2
BOOST_URL:=https://anaconda.org/conda-forge/boost/1.74.0/download/win-64/boost-1.74.0-py37h3b38789_3.tar.bz2
LXML_URL:=https://files.pythonhosted.org/packages/9e/5e/171ee9d40a600f565fe691ec5bf7596247ec62cfb2edc00c91afe8ea837b/lxml-4.6.3-cp37-cp37m-win_amd64.whl
endif
ifeq ($(PYVERSION), py39)
HPPFCL_URL:=https://anaconda.org/conda-forge/hpp-fcl/1.7.5/download/win-64/hpp-fcl-1.7.5-py39h2e7c763_0.tar.bz2
EIGENPY_URL:=https://anaconda.org/conda-forge/eigenpy/2.6.5/download/win-64/eigenpy-2.6.5-py39h3ce40e6_0.tar.bz2
BOOST_URL:=https://anaconda.org/conda-forge/boost/1.74.0/download/win-64/boost-1.74.0-py39hefe7e4c_3.tar.bz2
LXML_URL:=https://files.pythonhosted.org/packages/72/d4/426ecb8849c47c3e370c87aa0ac05d85768df917ffea27fcd6686a5e6495/lxml-4.6.3-cp39-cp39-win_amd64.whl
endif
ASSIMP_URL:=https://anaconda.org/conda-forge/assimp/5.0.1/download/win-64/assimp-5.0.1-hc2aa0de_6.tar.bz2
OCTOMAP_URL:=https://anaconda.org/conda-forge/octomap/1.9.7/download/win-64/octomap-1.9.7-h5362a0b_0.tar.bz2
ZLIB_URL:=https://anaconda.org/conda-forge/zlib/1.2.11/download/win-64/zlib-1.2.11-h62dcd97_1010.tar.bz2
endif

.PHONY: dist
dist:
ifndef PLATFORM
	$(error PLATFORM is not set)
endif
	rm -rf dist
	mkdir -p dist/working
	mkdir -p dist/blenderbim
	cp -r blenderbim/* dist/blenderbim/

	# Provides IfcOpenShell Python functionality
	cd dist/working && wget https://s3.amazonaws.com/ifcopenshell-builds/ifcblender-python-$(PYNUMBER)-v0.7.0-4c40fc1-$(PLATFORM)64.zip
	cd dist/working && unzip ifcblender*
	cp -r dist/working/io_import_scene_ifc/ifcopenshell dist/blenderbim/libs/site/packages/

	# See bug #812
	cd dist/working && wget https://raw.githubusercontent.com/IfcOpenShell/IfcOpenShell/v0.7.0/src/blenderbim/occ_utils.py
	cd dist/working && mv occ_utils.py ../blenderbim/libs/site/packages/ifcopenshell/geom/occ_utils.py
	rm -rf dist/working

	# Provides dependencies that are part of IfcOpenShell
	mkdir dist/working
	cd dist/working && wget https://github.com/IfcOpenShell/IfcOpenShell/archive/v0.7.0.zip
	cd dist/working && unzip v0.7.0.zip
	# IfcOpenBot sometimes lags behind, so we hotfix the Python utilities
	cp -r dist/working/IfcOpenShell-0.7.0/src/ifcopenshell-python/ifcopenshell/util/* dist/blenderbim/libs/site/packages/ifcopenshell/util/
	cp -r dist/working/IfcOpenShell-0.7.0/src/ifcopenshell-python/ifcopenshell/api/* dist/blenderbim/libs/site/packages/ifcopenshell/api/
	cp dist/working/IfcOpenShell-0.7.0/src/ifcopenshell-python/ifcopenshell/entity_instance.py dist/blenderbim/libs/site/packages/ifcopenshell/
	cp dist/working/IfcOpenShell-0.7.0/src/ifcopenshell-python/ifcopenshell/file.py dist/blenderbim/libs/site/packages/ifcopenshell/
	# Provides bcf functionality
	cp -r dist/working/IfcOpenShell-0.7.0/src/bcf/src/bcf dist/blenderbim/libs/site/packages/
	# Provides IFCClash functionality
	cp -r dist/working/IfcOpenShell-0.7.0/src/ifcclash/ifcclash dist/blenderbim/libs/site/packages/
	# Provides BIMTester functionality
	cd dist/working && python -m venv env
	cd dist/working && . env/bin/activate && pip install pybabel
	cd dist/working && . env/bin/activate && pip install babel
	cd dist/working && . env/bin/activate && ./env/bin/pybabel compile -d ./IfcOpenShell-0.7.0/src/ifcbimtester/bimtester/locale/
	cp -r dist/working/IfcOpenShell-0.7.0/src/ifcbimtester/bimtester dist/blenderbim/libs/site/packages/
	# Provides IFCCOBie functionality
	cp -r dist/working/IfcOpenShell-0.7.0/src/ifccobie/* dist/blenderbim/libs/site/packages/
	# Provides IFCDiff functionality
	cp -r dist/working/IfcOpenShell-0.7.0/src/ifcdiff/* dist/blenderbim/libs/site/packages/
	# Provides IFCCSV functionality
	cp -r dist/working/IfcOpenShell-0.7.0/src/ifccsv/* dist/blenderbim/libs/site/packages/
	# Provides IFCPatch functionality
	cp -r dist/working/IfcOpenShell-0.7.0/src/ifcpatch/ifcpatch dist/blenderbim/libs/site/packages/
	# Provides IFC4D functionality
	cp -r dist/working/IfcOpenShell-0.7.0/src/ifc4d/ifc4d dist/blenderbim/libs/site/packages/
	# Provides IFC5D functionality
	cp -r dist/working/IfcOpenShell-0.7.0/src/ifc5d/ifc5d dist/blenderbim/libs/site/packages/
	# Provides IFCCityJSON functionality
	cp -r dist/working/IfcOpenShell-0.7.0/src/ifccityjson dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Provides Mustache templating in construction documentation
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/d6/fd/eb8c212053addd941cc90baac307c00ac246ac3fce7166b86434c6eae963/pystache-0.5.4.tar.gz
	cd dist/working && tar -xzvf pystache*
	cd dist/working/pystache-0.5.4/ && python setup.py build && cp -r build/lib/pystache ../../blenderbim/libs/site/packages/
	rm -rf dist/working

	# Provides SVG export in construction documentation
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/79/e8/7eb2ba188eda14a4b47e33b51f3b4978985f4116655c699bcd18c79279b5/svgwrite-1.3.1.zip
	cd dist/working && unzip svgwrite*
	cp -r dist/working/svgwrite-1.3.1/svgwrite dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Provides fuzzy date parsing for construction sequencing
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/be/ed/5bbc91f03fa4c839c4c7360375da77f9659af5f7086b7a7bdda65771c8e0/python-dateutil-2.8.1.tar.gz
	cd dist/working && tar -xzvf python-dateutil*
	cp -r dist/working/python-dateutil-2.8.1/dateutil dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Provides duration parsing for construction sequencing
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/b1/80/fb8c13a4cd38eb5021dc3741a9e588e4d1de88d895c1910c6fc8a08b7a70/isodate-0.6.0.tar.gz
	cd dist/working && tar -xzvf isodate*
	cp -r dist/working/isodate-0.6.0/src/isodate dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Provides networkx graph analysis for project dependency calculations
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/b0/21/adfbf6168631e28577e4af9eb9f26d75fe72b2bb1d33762a5f2c425e6c2a/networkx-2.5.1.tar.gz
	cd dist/working && tar -xzvf networkx*
	cp -r dist/working/networkx-2.5.1/networkx dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by networkx
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/4f/51/15a4f6b8154d292e130e5e566c730d8ec6c9802563d58760666f1818ba58/decorator-5.0.9.tar.gz
	cd dist/working && tar -xzvf decorator*
	cp -r dist/working/decorator-5.0.9/src/decorator.py dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Provides jsgantt-improved supports for web-based construction sequencing gantt charts
	mkdir dist/working
	cd dist/working && wget https://raw.githubusercontent.com/jsGanttImproved/jsgantt-improved/master/dist/jsgantt.js
	cd dist/working && wget https://raw.githubusercontent.com/jsGanttImproved/jsgantt-improved/master/dist/jsgantt.css
	cp dist/working/jsgantt* dist/blenderbim/bim/data/gantt/
	rm -rf dist/working

	# Required by IFCDiff
	mkdir dist/working
	cd dist/working && wget https://github.com/Moult/deepdiff/archive/master.zip
	cd dist/working && unzip master.zip
	cp -r dist/working/deepdiff-master/deepdiff dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by deepdiff
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/00/55/ce2cbc6d64034b30cad81a29ba61bdba456f190f5e83c09831304bf68d6b/jsonpickle-1.2.tar.gz
	cd dist/working && tar -xzvf jsonpickle*
	cp -r dist/working/jsonpickle-1.2/jsonpickle dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by deepdiff
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/a3/b7/d4d69641cbe707a45c23b190f2d717466ba5accc4c70b5f7a8a450387895/ordered-set-3.1.1.tar.gz
	cd dist/working && tar -xzvf ordered-set*
	cp -r dist/working/ordered-set-3.1.1/ordered_set.py dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by lark
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/00/32/8076fa13e832bb4dcff379f18f228e5a53412be0631808b9ca2610c0f566/pyparsing-2.4.5.tar.gz
	cd dist/working && tar -xzvf pyparsing*
	cp -r dist/working/pyparsing-2.4.5/pyparsing.py dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by bcf
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/bb/41/ad9ce53bb978b68af8ae415293cafc89b165b8ad55a593725299dca76729/xmlschema-1.1.1.tar.gz
	cd dist/working && tar -xzvf xmlschema*
	cp -r dist/working/xmlschema-1.1.1/xmlschema dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by bcf
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/12/f9/f9960222d5274944b01391749e55e4dcdf28d8f0c108b64ac931ceff6fdb/elementpath-1.4.3.tar.gz
	cd dist/working && tar -xzvf elementpath*
	cp -r dist/working/elementpath-1.4.3/elementpath dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by bcf
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/21/9f/b251f7f8a76dec1d6651be194dfba8fb8d7781d10ab3987190de8391d08e/six-1.14.0.tar.gz
	cd dist/working && tar -xzvf six*
	cp -r dist/working/six-1.14.0/six.py dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by IFCCSV and ifcopenshell.util.selector
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/18/4d/8d522136c37d9e1ea74062b41b8d5e1318ebf45063ae46ce72ed60af223b/lark-parser-0.8.5.tar.gz
	cd dist/working && tar -xzvf lark-parser*
	cp -r dist/working/lark-parser-0.8.5/lark dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by IFC4D
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/b0/bb/9c4dddd3ca173cb56241cfb2eddfae24690dc676d357ac4cab17d0a36d9d/PyP6Xer-1.13.0.tar.gz
	cd dist/working && tar -xzvf PyP6Xer*
	cp -r dist/working/PyP6Xer-1.13.0/xerparser dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by xerparser and IFC4D
	# TODO: remove this dependency. It's only used to show a progress bar.
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/9f/7b/76c4e5ef1a1b528fcaada4133f972e77d33c252831676cf414119ca6093d/tqdm-4.50.0.tar.gz
	cd dist/working && tar -xzvf tqdm*
	cp -r dist/working/tqdm-4.50.0/tqdm dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by IFCCityJSON
	mkdir dist/working
	cd dist/working && python -m venv env
	cd dist/working && mkdir site-packages
	cd dist/working && . env/bin/activate && pip install cjio --target=./site-packages
	cd dist/working/site-packages/ && rm -r *dist-info*
	cp -r dist/working/site-packages/* dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by IFCClash
	mkdir dist/working
	cd dist/working && wget $(HPPFCL_URL)
	cd dist/working && tar -xf hpp-fcl*
ifeq ($(PLATFORM), linux)
	cp -r dist/working/lib/$(PYLIBDIR)/site-packages/hppfcl dist/blenderbim/libs/site/packages/
	cp -r dist/working/lib/*.so* dist/blenderbim/libs/
endif
ifeq ($(PLATFORM), macos)
	cp -r dist/working/lib/$(PYLIBDIR)/site-packages/hppfcl dist/blenderbim/libs/site/packages/
	cp -r dist/working/lib/*.dylib dist/blenderbim/libs/
endif
ifeq ($(PLATFORM), win)
	cp -r dist/working/Lib/site-packages/hppfcl dist/blenderbim/libs/site/packages/
	cp -r dist/working/Library/bin/*.dll dist/blenderbim/libs/site/packages/hppfcl/
endif
	rm -rf dist/working

	# Required by hpp-fcl
	mkdir dist/working
	cd dist/working && wget $(ASSIMP_URL)
	cd dist/working && tar -xf assimp*
ifeq ($(PLATFORM), linux)
	cp -r dist/working/lib/*.so* dist/blenderbim/libs/
endif
ifeq ($(PLATFORM), macos)
	cp -r dist/working/lib/*.dylib dist/blenderbim/libs/
endif
ifeq ($(PLATFORM), win)
	cp -r dist/working/Library/bin/*.dll dist/blenderbim/libs/site/packages/hppfcl/
endif
	rm -rf dist/working

	# Required by hpp-fcl
	mkdir dist/working
	cd dist/working && wget $(EIGENPY_URL)
	cd dist/working && tar -xf eigenpy*
ifeq ($(PLATFORM), linux)
	cp -r dist/working/lib/*.so* dist/blenderbim/libs/
endif
ifeq ($(PLATFORM), macos)
	cp -r dist/working/lib/*.dylib dist/blenderbim/libs/
endif
ifeq ($(PLATFORM), win)
	cp -r dist/working/Library/bin/*.dll dist/blenderbim/libs/site/packages/hppfcl/
endif
	rm -rf dist/working

	# Required by hpp-fcl
	mkdir dist/working
	cd dist/working && wget $(OCTOMAP_URL)
	cd dist/working && tar -xf octomap*
ifeq ($(PLATFORM), linux)
	cp -r dist/working/lib/*.so* dist/blenderbim/libs/
endif
ifeq ($(PLATFORM), macos)
	cp -r dist/working/lib/*.dylib dist/blenderbim/libs/
endif
ifeq ($(PLATFORM), win)
	# Uh, do nothing, apparently? No DLLs are shipped.
endif
	rm -rf dist/working

	# Required by hpp-fcl
	mkdir dist/working
	cd dist/working && wget $(BOOST_URL)
	cd dist/working && tar -xf boost*
ifeq ($(PLATFORM), linux)
	cp -r dist/working/lib/*.so* dist/blenderbim/libs/
endif
ifeq ($(PLATFORM), macos)
	cp -r dist/working/lib/*.dylib dist/blenderbim/libs/
endif
ifeq ($(PLATFORM), win)
	cp -r dist/working/Library/bin/*.dll dist/blenderbim/libs/site/packages/hppfcl/
endif
	rm -rf dist/working

	# Required by hpp-fcl
	mkdir dist/working
	cd dist/working && wget $(ZLIB_URL)
	cd dist/working && tar -xf zlib*
ifeq ($(PLATFORM), linux)
	cp -r dist/working/lib/*.so* dist/blenderbim/libs/
endif
ifeq ($(PLATFORM), macos)
	cp -r dist/working/lib/*.dylib dist/blenderbim/libs/
endif
ifeq ($(PLATFORM), win)
	cp -r dist/working/Library/bin/*.dll dist/blenderbim/libs/site/packages/hppfcl/
endif
	rm -rf dist/working

	# Required by BIMTester
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/c8/4b/d0a8c23b6c8985e5544ea96d27105a273ea22051317f850c2cdbf2029fe4/behave-1.2.6.tar.gz
	cd dist/working && tar -xzvf behave*
	cd dist/working/behave-1.2.6/ && cp -r behave ../../blenderbim/libs/site/packages/
	# See bug #1294
	cd dist/working/ && wget https://raw.githubusercontent.com/IfcOpenShell/IfcOpenShell/v0.7.0/src/ifcbimtester/patch/model_core.patch
	cd dist/working/ && wget https://raw.githubusercontent.com/IfcOpenShell/IfcOpenShell/v0.7.0/src/ifcbimtester/patch/runner_util.patch
	cd dist/working/ && patch ../blenderbim/libs/site/packages/behave/model_core.py < model_core.patch
	cd dist/working/ && patch ../blenderbim/libs/site/packages/behave/runner_util.py < runner_util.patch
	rm -rf dist/working

	# Required by ids - uh, not any more, but I'm trying it out in the drawing module
	mkdir dist/working
	cd dist/working && wget $(LXML_URL)
	cd dist/working && cp *.whl lxml.zip && unzip lxml.zip
	cp -r dist/working/lxml dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by behave
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/f4/65/220bb4075fddb09d5b3ea2c1c1fa66c1c72be9361ec187aab50fa161e576/parse-1.15.0.tar.gz
	cd dist/working && tar -xzvf parse*
	cd dist/working/parse-1.15.0/ && cp parse.py ../../blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by behave
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/2e/79/81bebd1b0446d46733db99d74543b4bb80646ef4c988584bae0862e706bc/parse_type-0.5.2.tar.gz
	cd dist/working && tar -xzvf parse_type*
	cd dist/working/parse_type-0.5.2/ && cp -r parse_type ../../blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by IFCCOBie for XLSX support
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/0c/bc/82d6783f83f65f56d8b77d052773c4a2f952fa86385f0cd54e1e006658d7/XlsxWriter-1.2.9.tar.gz
	cd dist/working && tar -xzvf XlsxWriter*
	cd dist/working/XlsxWriter-1.2.9/ && cp -r xlsxwriter ../../blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by IFCCOBie for ODS support
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/97/73/8ade73f6749177003f7ce3304f524774adda96e6aaab30ea79fd8fda7934/odfpy-1.4.1.tar.gz
	cd dist/working && tar -xzvf odfpy*
	cd dist/working/odfpy-1.4.1/ && cp -r odf ../../blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by odfpy
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/a4/5f/f8aa58ca0cf01cbcee728abc9d88bfeb74e95e6cb4334cfd5bed5673ea77/defusedxml-0.6.0.tar.gz
	cd dist/working && tar -xzvf defusedxml*
	cd dist/working/defusedxml-0.6.0/ && cp -r defusedxml ../../blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by augin
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/76/b4/b7baffbda025efd5dc8fcd8d2e953e3aa939c236a484084fa8f4c3588ee9/boto3-1.17.17.tar.gz
	cd dist/working && tar -xzvf boto3*
	cd dist/working/boto3-1.17.17/ && cp -r boto3 ../../blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by boto3
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/7f/2e/e02fdfd0f0377c4e44e61de27b05d5cfe93575770661ef9ded80ed90fa88/botocore-1.20.17.tar.gz
	cd dist/working && tar -xzvf botocore*
	cd dist/working/botocore-1.20.17/ && cp -r botocore ../../blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by boto3
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/3c/56/3f325b1eef9791759784aa5046a8f6a1aff8f7c898a2e34506771d3b99d8/jmespath-0.10.0.tar.gz
	cd dist/working && tar -xzvf jmespath*
	cd dist/working/jmespath-0.10.0/ && cp -r jmespath ../../blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by boto3
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/08/e1/3ee2096ebaeeb8c186d20ed16c8faf4a503913e5c9a0e14cd6b8ffc405a3/s3transfer-0.3.4.tar.gz
	cd dist/working && tar -xzvf s3transfer*
	cd dist/working/s3transfer-0.3.4/ && cp -r s3transfer ../../blenderbim/libs/site/packages/
	rm -rf dist/working

	# Provides IFCJSON functionality
	mkdir dist/working
	cd dist/working && wget https://github.com/IFCJSON-Team/IFC2JSON_python/archive/master.zip
	cd dist/working && unzip master.zip
	cp -r dist/working/IFC2JSON_python-master/file_converters/ifcjson dist/blenderbim/libs/site/packages/
	rm -rf dist/working

	# Provides OpenLCA fucntionality
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/85/33/f91b96e9e8608ff65a003b692e8a9cdd60f2178f60617e5b1d21334c009c/olca-ipc-0.0.10.tar.gz
	cd dist/working && tar -xzvf olca-ipc*
	cd dist/working/olca-ipc-0.0.10/ && cp -r olca ../../blenderbim/libs/site/packages/
	rm -rf dist/working

	# Provides Brickschema fucntionality
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/ca/37/8309da9a72407d2f5eb5489c197ac3cfe96ee3ccba1902d2a0ecc7843f92/brickschema-0.5.1.tar.gz
	cd dist/working && tar -xzvf brickschema*
	# This is an evil hack because we don't want to bundle flask
	echo "" > dist/working/brickschema-0.5.1/brickschema/web.py
	cd dist/working/brickschema-0.5.1/ && cp -r brickschema ../../blenderbim/libs/site/packages/
	# For now lets bundle the latest nightly schema
	cd dist/working && wget https://github.com/BrickSchema/Brick/releases/download/nightly/Brick.ttl
	cd dist/working && cp Brick.ttl ../../blenderbim/bim/schema/Brick.ttl
	rm -rf dist/working

	# Required by brickschema
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/c7/22/37bb938be8e5c20d443b0c9ba0a243573b671b01739efb0a19f81bc5b470/pyshacl-0.17.2.tar.gz
	cd dist/working && tar -xzvf pyshacl*
	cd dist/working/pyshacl-0.17.2/ && cp -r pyshacl ../../blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by brickschema
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/d2/a7/be8244688bfcee37c23733ab4fe8e6afa6d4403bd2674a3ae7bd2cecc77b/rdflib-6.0.2.tar.gz
	cd dist/working && tar -xzvf rdflib*
	cd dist/working/rdflib-6.0.2/ && cp -r rdflib ../../blenderbim/libs/site/packages/
	rm -rf dist/working

	# Required by brickschema
	mkdir dist/working
	cd dist/working && wget https://files.pythonhosted.org/packages/7d/c7/208aece36279e4f1236e437119358786e39530ecc1719d4e1afeddba5288/owlrl-6.0.2.tar.gz
	cd dist/working && tar -xzvf owlrl*
	cd dist/working/owlrl-6.0.2/ && cp -r owlrl ../../blenderbim/libs/site/packages/
	rm -rf dist/working

	cd dist/blenderbim && sed -i "s/999999/$(VERSION)/" __init__.py
	cd dist && zip -r blenderbim-$(VERSION)-$(PYVERSION)-$(PLATFORM).zip ./*
	rm -rf dist/blenderbim

.PHONY: test
test:
	make test-core
	make test-tool
	make test-bim

.PHONY: test-core
test-core:
	pytest -p no:pytest-blender test/core

.PHONY: test-bim
test-bim:
	pytest test/bim

.PHONY: test-tool
test-tool:
	pytest test/tool

.PHONY: qa
qa:
	black .
	pylint ./* --output-format=colorized --disable all --enable E --disable import-error

.PHONY: coverage
coverage:
	coverage run --source blenderbim.core -m pytest -p no:pytest-blender test/core
	coverage html
	xdg-open htmlcov/index.html

.PHONY: license
license:
	copyright-header --license GPL3 --copyright-holder "Dion Moult <dion@thinkmoult.com>" --copyright-year "2022" --copyright-software "BlenderBIM Add-on" --copyright-software-description "OpenBIM Blender Add-on" -a ./ -o ./

.PHONY: clean
clean:
	rm -rf dist
	rm -rf htmlcov

.PHONY: dev
dev:
	blender -p setup_pytest.py
