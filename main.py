
def sort_by_word_count():

    # ������� 10: �������������� ����� �� ���������� ����.
    # :return: ��������������� ������ �����.

    # ������ ����� � ����������
    lines = []
    print("������� ������ (��� ���������� ������� ������ ������):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    # ���������� ����� �� ���������� ����
    sorted_lines = sorted(lines, key=lambda x: len(x.split()))
    return sorted_lines

# ������ �������������
print("��������������� ������ �� ���������� ����:", sort_by_word_count())

