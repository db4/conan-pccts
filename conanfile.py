import os, shutil
from conans import ConanFile, tools


class PcctsConan(ConanFile):
    name = "pccts"
    version = "1.33MR33"
    settings = "os_build", "compiler", "arch_build"
    generators = "gcc"
    description = "PCCTS toolkit"
    license = "public domain"
    url = "https://github.com/db4/conan-pccts"

    def build(self):
        if self.settings.os_build == "Windows":
            tools.get("http://www.polhode.com/win32.zip", sha1="db910f4397b2f77a58980e9ab3ba2603c42ba50e")
        else:
            tools.get("http://www.polhode.com/pccts133mr.zip", sha1="5b3417efd5f537434b568114bcda853b4975d851")
            if tools.cross_building(self.settings):
                shutil.copytree("pccts", "pccts-host")
                self.run("cd pccts-host && make COPT=-DPCCTS_USE_STDARG")
                tools.replace_in_file("pccts/sorcerer/makefile", "$(BIN)/antlr", "../../pccts-host/bin/antlr")
                tools.replace_in_file("pccts/sorcerer/makefile", "$(BIN)/dlg", "../../pccts-host/bin/dlg")
            tools.replace_in_file("pccts/support/genmk/makefile", "$(CC) -o", "$(CC) $(COPT) -o")
            self.run("cd pccts && make CC=\"gcc @{0}\" COPT=-DPCCTS_USE_STDARG".format(
                os.path.join(self.build_folder, "conanbuildinfo.gcc")))

    def package(self):
        tmp = tools.load("pccts/h/antlr.h")
        license_contents = tmp[tmp.find(" * SOFTWARE RIGHTS"):tmp.find("*/")]
        tools.save("LICENSE", license_contents)
        self.copy("LICENSE")
        self.copy("*.h", dst="include", src="pccts/h")
        self.copy("*.cpp", dst="include", src="pccts/h")
        self.copy("*", dst="bin", src="pccts/bin", excludes="*.txt")

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))

    def package_id(self):
        self.info.include_build_settings()
        if self.info.settings.os_build == "Windows":
            del self.info.settings.arch_build
        del self.info.settings.compiler
