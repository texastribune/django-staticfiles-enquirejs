PACKAGE_NAME = enquirejs
STATIC_DIR = $(PACKAGE_NAME)/static/$(PACKAGE_NAME)
VERSION = $(shell cat VERSION)
WGET = wget -N
GIT_TAG = v$(VERSION)
# GIT_TAG = master


all: clean build


clean:
	rm -rf $(STATIC_DIR)
	rm -rf *.egg-info
	rm -rf build
	rm -rf dist


build:
	mkdir -p $(STATIC_DIR)
	cd $(STATIC_DIR) && $(WGET) https://raw.github.com/WickyNilliams/enquire.js/$(GIT_TAG)/dist/enquire.js
	cd $(STATIC_DIR) && $(WGET) https://raw.github.com/WickyNilliams/enquire.js/$(GIT_TAG)/dist/enquire.min.js


.PHONY: all clean build
