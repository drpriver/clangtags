from distutils.core import setup

setup(
    name='clangtags',
    version='0.1dev',
    packages=['clangtags', 'clangtags/clang'],
    package_data = {
        'clangtags/clang': ['clangtags/clang/py.typed', 'py.typed'],
        'clangtags': ['clangtags/py.typed'],
        }
)

