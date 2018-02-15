import os
from conans import ConanFile, tools


class PcctsConan(ConanFile):
    name = "pccts"
    version = "1.33"
    settings = "os", "compiler", "arch"
    description = "PCCTS toolkit"
    license = "public domain"
    url = "http://git.rt.local/conan/pccts"

    def build(self):
        if self.settings.os == "Windows":
            url = "http://www.polhode.com/win32.zip"
            tools.get(url)
        else:
            url = "http://www.polhode.com/pccts133mr.zip"
            tools.get(url)
            tools.patch(base_path="pccts/sorcerer/lib",
                        patch_string="""
--- a/makefile\t2000-09-10 03:57:13.000000000 +0300
+++ b/makefile\t2018-02-15 12:04:17.869441600 +0300
@@ -5,7 +5,7 @@
 OBJ = astlib.o sstack.o sorlist.o sintstack.o
 CC=cc
 COPT=-g
-CFLAGS=$(COPT) -I../../h -I../h
+CFLAGS=$(COPT) -I../../h -I../h -DPCCTS_USE_STDARG

 libs : $(OBJ) $(SRC)

""")
            self.run("cd pccts && make")

    def package(self):
        self.copy("*.h", dst="include", src="pccts/h")
        self.copy("*.cpp", dst="include", src="pccts/h")
        self.copy("*", dst="bin", src="pccts/bin", excludes="*.txt")

    def package_info(self):
        self.env_info.path.append(os.path.join(self.package_folder, "bin"))

    def package_id(self):
        if self.settings.os == "Windows":
            self.info.settings.compiler = "Any"
            self.info.settings.arch = "Any"
