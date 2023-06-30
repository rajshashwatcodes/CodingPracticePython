def is_valid_tag(tag):
    stack = []
    i = 0

    while i < len(tag):
        if tag[i] == '<':
            if i + 1 < len(tag) and tag[i + 1] == '<':
                return False
            stack.append(tag[i])
        elif tag[i] == '>':
            if len(stack) == 0 or stack[-1] != '<':
                return False
            stack.pop()
        i += 1

    return len(stack) == 0

# Test cases
tags = ["<aa><bb>", "<<zz>>", "<xx>>", "<<yy", "<bb><cc>>>"]

for tag in tags:
    if is_valid_tag(tag):
        print(f"{tag} is a valid tag.")
    else:
        print(f"{tag} is an invalid tag.")
