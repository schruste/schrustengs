import setuptools

setuptools.setup(
    name='schrustengs',
    version='0.1',
    author = "Christoph Lehrenfeld",
    author_email = "schrustup@gmail.com",
    description = ("Changes and monkey patches to NGSolve that are not general and polished enough to go in the main code."),
    license = "BSD",
    packages=['schrustengs/patchvtk'],
    install_requires=[
        'meshio>=4.2.2',
    ],
    extras_require={
    },
    python_requires='>=3.6,<4.0',
)
