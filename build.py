import platform
from conan.packager import ConanMultiPackager


if __name__ == "__main__":
    builder = ConanMultiPackager(username="dbely")
    if platform.system() == "Windows":
        builder.add(settings={}, options={}, env_vars={}, build_requires={})
    else:
        builder.add_common_builds()
        filtered_builds = []
        for settings, options, env_vars, build_requires in builder.builds:
            if settings["build_type"] == "Release":
                filtered_builds.append([settings, options, env_vars, build_requires])
        builder.builds = filtered_builds
    builder.run()
