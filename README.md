# conan-pccts

[Conan.io](https://conan.io) package for [PCCTS](http://www.antlr2.org/pccts133.html)

| Appveyor | Travis |
|-----------|--------|
|[![Build Status](https://ci.appveyor.com/api/projects/status/github/db4/conan-pccts?branch=master&svg=true)](https://ci.appveyor.com/project/db4/conan-pccts)|[![Build Status](https://travis-ci.org/db4/conan-pccts.svg?branch=master)](https://travis-ci.org/db4/conan-pccts)|

## Build packages

Download conan client from [Conan.io](https://conan.io) and run:

    $ python build.py

## Upload packages to server

    $ conan upload pccts/1.33@dbely/stable --all

## Reuse the packages

### Basic setup

    $ conan install pccts/1.33@dbely/stable

### Project setup

If you handle multiple dependencies in your project, it would be better to add a *conanfile.txt*

    [requires]
    pccts/1.33@dbely/stable

    [generators]
    txt
    cmake


