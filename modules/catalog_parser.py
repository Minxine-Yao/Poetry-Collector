def catalogParser(filepath):
    catalog = []

    author = ""
    title = ""
    with open(filepath,encoding="ANSI") as f:
        for line in f:
            if len(line.strip()) == 0:
                # 跳过空行
                continue
            elif "…" not in line:
                # 可能是作者名或者过长标题的分段之一
                if len(line) < 10:
                    author = line.strip()
                else:
                    title += line.strip()
            else:
                # 标题行或者过长标题的最后一个分段
                title += line[:line.find("…")]
                poem = {
                    "title": title,
                    "author": author
                }
                title = ""
                catalog.append(poem)

    return catalog
