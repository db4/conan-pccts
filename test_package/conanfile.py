from conans import ConanFile, CMake, tools
import os

class PcctsConan(ConanFile):
    settings = "os", "arch", "compiler"
    generators = "cmake"

    def build(self):
        if not tools.cross_building(self.settings):
            cmake = CMake(self)
            # Current dir is "test_package/build/<build_id>" and CMakeLists.txt is in "test_package"
            cmake.configure()
            cmake.build()

    def test(self):
        if not tools.cross_building(self.settings):
            os.chdir("bin")
            tools.save("input.txt", "2*2\n\n");
            self.run(".%scalc < input.txt" % os.sep)
