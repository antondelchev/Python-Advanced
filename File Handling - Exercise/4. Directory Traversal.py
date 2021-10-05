import os


def traverse_dir(dir_path, result):
    for item in os.listdir(dir_path):
        file_and_path = os.path.join(dir_path, item)
        if os.path.isfile(file_and_path):
            extension = item.split(".")[-1]
            if extension not in result:
                result[extension] = []
            result[extension].append(file_and_path)


final_result = {}
traverse_dir(os.getcwd(), final_result)

with open("report.txt", "w") as result_file:
    for ext, files in sorted(final_result.items()):
        result_file.write(f"{ext}")
        result_file.write("\n")
        for file in sorted(files):
            result_file.write(f"---{file}")
            result_file.write("\n")
