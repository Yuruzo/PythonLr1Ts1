
def sort_by_length():

    # ������� 9: �������������� ����� �� �����.
    # :return: ��������������� ������ �����.

    # ������ ����� � ����������
    lines = []
    print("������� ������ (��� ���������� ������� ������ ������):")
    while True:
        line = input()
        if line == "":
            break
        lines.append(line)
    
    # ���������� ����� �� �����
    sorted_lines = sorted(lines, key=len)
    return sorted_lines

# ������ �������������
print("��������������� ������ �� �����:", sort_by_length())
