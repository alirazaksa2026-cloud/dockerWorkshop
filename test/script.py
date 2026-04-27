from pathlib import Path

# current_dir1 = Path(__file__).parent
# current_dir2 = Path(__file__).absolute().parent
# current_file0 = Path(__file__)
# current_file1 = Path(__file__).absolute()
# current_file2 = Path(__file__).resolve()
# current_file3 = Path(__file__).absolute().resolve()
# current_file4 = Path(__file__).resolve().absolute()
# current_file5 = Path(__file__).absolute().resolve().absolute()
# print(f"current_dir1={current_dir1}")
# print(f"current_file0={current_file0}")
# print(f"current_dir2={current_dir2}")
# print(f"current_file1={current_file1}")
# print(f"current_file2={current_file2}")
# print(f"current_file3={current_file3}")
# print(f"current_file4={current_file4}")
# print(f"current_file5={current_file5}")

current_dir = Path.cwd()
current_file= Path(__file__).name
print(f"current_dir={current_dir}")

print(f"current_file={current_file}")


for filepath in current_dir.iterdir():
    if filepath.name == current_file:
        continue
    print(f"    -{filepath}")

    if filepath.is_file():
        content = filepath.read_text(encoding="utf-8")
        print(f"        content1={content}")