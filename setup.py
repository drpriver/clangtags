from distutils.core import setup

setup(
    name='clangtags',
    version='0.1dev',
    description='Tags file generator based on libclang',
    author = 'David Priver',
    author_email = 'david@davidpriver.com',
    license = 'Public Domain',
    classifiers = [
        'Development Status :: 4 - Beta',
        'License :: Public Domain',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3 :: Only',
    ],
    python_requires='>=3.8, <4',
    packages=['clangtags', 'clangtags/clang'],
    package_data = {
        'clangtags/clang': ['clangtags/clang/py.typed', 'py.typed'],
        'clangtags': ['clangtags/py.typed'],
    },
    install_requires = [ ],
)

