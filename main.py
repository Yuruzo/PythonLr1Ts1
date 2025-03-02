

def find_unused_latin_chars(s):

    # ������� 7: ����� ����������������� �������� �������� � ������.
    # :param s: ������� ������.
    # :return: ��������� ����������������� �������� ��������.

    used_chars = set(s.lower())  # �������� �������������� �������
    latin_chars = set('abcdefghijklmnopqrstuvwxyz')  # ��� ������� ��������
    return latin_chars - used_chars  # ������� ����� ����� ��������� � ���������������

s = "Hello world"
print("����������������� ������� ��������:", find_unused_latin_chars(s))
