# day_02_part_02.py

def find_common_letters(box_ids):
    for i in range(len(box_ids)):
        for j in range(i+1, len(box_ids)):
            differ_count = 0
            common_letters = ''
            for k in range(len(box_ids[i])):
                if box_ids[i][k] != box_ids[j][k]:
                    differ_count += 1
                    if differ_count > 1:
                        break
                else:
                    common_letters += box_ids[i][k]
            if differ_count == 1:
                return common_letters

    return None
