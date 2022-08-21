from setuptools import setup, find_namespace_packages

with open("README.md", "r") as freadme:
    readme = freadme.read()

setup(name="ItsUtils",
      version="0.2.0",
      author="ItsNameless",
      description="A Package containing utils created by ItsNameless",
      long_description=readme,
      long_description_content_type="text/markdown",
      license="MIT",
      license_files=["LICENSE"],
      python_requires=">=3.8.0",
      classifiers=[
          "Programming Language :: Python :: 3",
          "License :: OSI Approved :: MIT License",
          "Operating System :: OS Independent"
      ],
      project_urls={
          "Homepage": "https://github.com/TheItsProjects/ItsUtils",
          "Issue Tracker": "https://github.com/TheItsProjects/ItsUtils/issues"
      },
      packages=find_namespace_packages(where=".",
                                       include=[
                                           "its_utils",
                                           "its_utils.string_math",
                                           "its_utils.debug_prompt",
                                           "its_utils.word_math"
                                       ]),
      package_dir={"": "."},
      package_data={"": ["py.typed"]})
