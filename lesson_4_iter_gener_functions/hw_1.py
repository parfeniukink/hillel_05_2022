FILENAME = "rockyou.txt"
SEARCH_KEYWORD = "user123"


def read_lines_find_admin_generator() -> list[str]:

    results = []

    with open(FILENAME, encoding="utf-8") as file:
        # line := file.readline()  # 'user123\n'  -> True
        # bool(line := file.readline())  # '' -> False

        while line := file.readline():
            if SEARCH_KEYWORD in line:
                filtered_line = line.replace("\n", "")
                user_input = input(f"Do you want to save - {filtered_line} ?[yes/no]")

                if user_input == "yes":
                    results.append(filtered_line)
        return results


results: list[str] = read_lines_find_admin_generator()

print(results)
