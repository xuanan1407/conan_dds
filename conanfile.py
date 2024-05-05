from conans import ConanFile, CMake, tools
import xml.etree.ElementTree as ET
import os

class IMSF_AlarmConan(ConanFile):
    name = "dds_An"
    version = "1.0.0"
    homepage = "project"
    license = "<Put the package license here>"
    author = "<Tran Xuan An> <xuanan.crkh1407@gmail.com>"
    url = "<https://sourcecode.socialcoding.bosch.com/scm/fsp/>"
    description = "Wrapper dds library"
    topics = ("dds")
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    generators = "cmake"
    exports = ["PackageConfig.cmake.in", "PkgConfig.pc.in"]
    exports_sources = ["src/*","lib/*","include/*","CMakeLists.txt","cmake/*", "etc/*", "examples/*"
                        ,"compat/*","docs/*", "tools/*", "fuzz/*", "hooks/*", "ports/*", "scripts/*", "WiX/*"]

    def config_options(self):
        self.settings.compiler.libcxx= 'libstdc++11'
        if self.settings.os == "Windows":
            del self.options.fPIC

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder='.')
        cmake.build()

    def package(self):
        self.copy("*", dst="include", src="src/core/ddsc/include/dds", keep_path=True)
        self.copy("*.lib", dst="lib", src="lib", keep_path=False)
        self.copy("*.dll", dst="bin", src="bin", keep_path=False)
        self.copy("*.so", dst="lib", src="lib", keep_path=False)
        self.copy("*.dylib", dst="lib", src="lib", keep_path=False)
        self.copy("*.a", dst="lib", src="lib", keep_path=False)
        self.copy("PackageConfig.cmake.in", dst=".", keep_path=False)
        self.copy("PkgConfig.pc.in", dst=".", keep_path=False)

    def package_info(self):
        self.cpp_info.libs = ["dds"]