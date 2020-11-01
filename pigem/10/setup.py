import cx_Freeze

executa = [cx_Freeze.Executable("10.py")]

cx_Freeze.setup(
    name="Dodging car",
    options={"build_exe": {"packages": ["pygame"],
                           "include_files": ["im"]}},
    executables=executa)
